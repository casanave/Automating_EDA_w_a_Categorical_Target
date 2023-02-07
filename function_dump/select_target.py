def select_target(df):    
    
    """
    HELPER FUNCTION TO: deploy_categorical_target_EDA()
    
    DOCSTRING: inputs a 'df' and promps user for target column. 
    Casts all other features as dependent variables. 
    
    Returns: X (dependent variables in a df), 
    y (target feature as a series) and "target_column" (the name of the target column.) 
    
    Also displays distribution of target variable in a pandas series/barplot, 
    aggrigated so each row is a variation of the target. 
    """
    try: 
        target_column = input('Target column: ')
        y = df[f'{target_column}']
        X = df.drop(columns = target_column)
        display(df[target_column].value_counts().to_frame().style.bar())

        return X, y, target_column

    except Exception as e_2: 
        print('ERROR at select_target', {e_2})