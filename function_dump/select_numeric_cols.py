def select_numeric_cols(X):
    
    """
    HELPER FUNCTION TO: deploy_categorical_target_EDA()
    
    DOCSTRING: inputs 'X' (dependent variables in a df) and promps user to 
    select which of the numeric dependent variables to keep in analysis. 
    
    Converts these variables to numeric using pd.to_numeric(). 
    
    Returns a list of these as 'num_columns'
    """
    
    try: 
        
        num_columns = input('Numeric dependant values: ').split()
        for x in (num_columns):
            X[x] = pd.to_numeric(X[x])
        display('converted')

    except Exception as e_6:
            print('ERROR at select_numeric_cols', {e_6})
            
    return num_columns