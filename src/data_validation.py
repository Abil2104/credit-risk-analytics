import pandas as pd

def run_continuous_audit(df):
    """
    Executes automated continuous auditing to catch sequence errors 
    and duplicate entries in incoming data streams.
    """
    audit_results = {
        "success": True,
        "duplicate_count": 0,
        "sequence_errors": 0,
        "logs": []
    }
    
    # 1. Catch Duplicate Entries
    duplicates = df.duplicated(subset=['member_id'], keep='first')
    df_cleaned = df[~duplicates]
    audit_results["duplicate_count"] = duplicates.sum()
    
    if audit_results["duplicate_count"] > 0:
        audit_results["logs"].append(f"⚠️ Caught {audit_results['duplicate_count']} duplicate member entries. Automatically dropped.")
    
    # 2. Catch Sequence/Format Errors (Out-of-bounds metrics)
    invalid_loans = df_cleaned['loan_amnt'] <= 0
    invalid_rates = (df_cleaned['int_rate'] < 0) | (df_cleaned['int_rate'] > 100)
    
    sequence_errors = invalid_loans.sum() + invalid_rates.sum()
    audit_results["sequence_errors"] = sequence_errors
    
    if sequence_errors > 0:
        audit_results["logs"].append(f"❌ Caught {sequence_errors} mathematical/sequence format anomalies.")
        df_cleaned = df_cleaned[~invalid_loans & ~invalid_rates]
    else:
        audit_results["logs"].append("✅ All sequence format and integrity checks passed.")
        
    if audit_results["duplicate_count"] > 0 or sequence_errors > 0:
        audit_results["success"] = False
        
    return df_cleaned, audit_results