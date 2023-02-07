def select_cat_cols(X):
    
    """
    HELPER FUNCTION TO: deploy_categorical_target_EDA()
    
    DOCSTRING: 
    inputs 'X' (dependent variables in a df) and prompts user to 
    select which of the categorical dependent variables to keep in analysis.
    
    Assumes these variables are already cast as strings.
    
    Displays the distribution of each categorical features as a pandas series/barplot,
    aggrigated so each row is a variation of each categorical feature. Does not 
    return anything.
    """
    
    try:
        cat_cols = input('Categorical dependant variables:').split()
        cat_df = X[cat_cols]
        for x in cat_df.columns:
            display(x, cat_df[x].value_counts().to_frame().style.bar())
            
    except Exception as e_3: 
        print('ERROR at select_cat_cols', {e_3})        
    return cat_cols