def input_csv():
    
    """
    HELPER FUNCTION TO: deploy_categorical_target_EDA()
    
    DOCSTRING: inputs a csv as prompted and displays the first five rows, 
    and information about each column and it's data type, gives option of 
    changing columns into 'snake_case' from 'Title Case'. 
    
    Returns: df.  
    """
    
    display("What CSV file would you like to use? Make sure it's in this repository!")
    file_name = input('Filename: ')
    try:
        df = pd.read_csv(file_name)
        display(df.columns)
        
        y_n_snake_case = input("Would you like to reformat the columns from 'Title Case' to 'snake_case':  y/n ")
        if y_n_snake_case.lower() == 'y':
    
            column_names = [x.lower().translate(str.maketrans('', '', string.punctuation)) \
                                .replace(' ', '_') for x in df]
            df.columns = column_names
            display('columns reformatted')
        else:
            pass 
        display(df.head(), df.info())

    except Exception as e_1: 
        print('ERROR at input_csv()', {e_1})

    return df