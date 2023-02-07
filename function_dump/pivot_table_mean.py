def pivot_table_mean(X, num_cols, y, target_column):
    
    """
    HELPER FUNCTION TO: output_viz(X, y, num_cols, target_column)
    
    DOCSTRING: inputs X (dependent variables as a df), 'num_cols' (a list of 
    numeric columns), y (a series of the target variable), and 'target_column',
    (the name of the target). 
    
    Displays a pivot table of all numeric feature's mean, grouped by the variations
    (categorical outcomes) in the target. 
    
    Returns: pivot_table
    """
    
    try: 
        # aggregating the df to group by target category
        num_cols_df = pd.concat([X[num_cols], y], axis = 1)
        pivot_table = num_cols_df.groupby(by = num_cols_df[target_column]).mean()
        display(pivot_table)

        return pivot_table

    except Exception as e_8:
        print ('ERROR at pivot_table_mean', {e_8})
        