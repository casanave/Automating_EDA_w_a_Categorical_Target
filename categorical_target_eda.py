# Imports: pandas as pd, matplotlib.pyplot as plt, seaborn as sns, string

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string


def input_csv():
    
    """
    HELPER FUNCTION TO: deploy_categorical_target_EDA()
    
    DOCSTRING: inputs a csv as prompted and displays the first five rows, 
    and information about each column and it's data type, gives option of 
    changing columns into 'snake_case' from 'Title Case'. 
    
    Returns: df.  
    """
    
    # asking the user which file to use, must be a CVS
    display("What CSV file would you like to use? Make sure it's in this repository!")
    file_name = input('Filename: ')

    # reading in the file and displaying all the columns 
    try:
        df = pd.read_csv(file_name)
        display([f'{x}' for x in df.columns])

    # asking the user if the columns should be transformed from 'Title Case' to 'snake_case'
       
        y_n_snake_case = input("Would you like to reformat the columns from 'Title Case' to 'snake_case':  y/n ")
        if y_n_snake_case.lower() == 'y':
    
            column_names = [x.lower().translate(str.maketrans('', '', string.punctuation)) \
                                .replace(' ', '_') for x in df]
            df.columns = column_names
            display('columns reformatted')
        else:
            pass 

        # either way, displaying the information about the features and the first five rows of the data
        display(df.head(), df.info())

    except Exception as e_1: 
        print('ERROR at input_csv()', {e_1})

    # spitting out a df at the end of this function
    return df

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
        # asking the user which column will be the target, must be categorical
        # seperating the target as 'y' from the dependant variables df 'X'
        target_column = input('Target column: ')
        y = df[f'{target_column}']
        X = df.drop(columns = target_column)
        display(df[target_column].value_counts().to_frame().style.bar())

        # making sure we end up with X, y and the name of the target feature
        return X, y, target_column

    except Exception as e_2: 
        print('ERROR at select_target', {e_2})


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
        # asking the user to input categorical dependent features like: <column_one column_two>, no parenthesis, separated by a space
        # saving those categorical columns to a list 

        cat_cols = input('Categorical dependent features: ').split()
        cat_df = X[cat_cols]

        # for each column in the list of categorical columns, show the distribution
        for x in cat_df.columns:
            display(x, cat_df[x].value_counts().to_frame().style.bar())
            
    except Exception as e_3: 
        print('ERROR at select_cat_cols', {e_3})        
    
    # making sure we keep our list of categorical columns 
    return cat_cols


def select_numeric_cols(X):
    
    """
    HELPER FUNCTION TO: deploy_categorical_target_EDA()
    
    DOCSTRING: inputs 'X' (dependent variables in a df) and promps user to 
    select which of the numeric dependent variables to keep in analysis. 
    
    Converts these variables to numeric using pd.to_numeric(). 
    
    Returns a list of these as 'num_columns'
    """
    
    try: 
        # asking the user to input numeric dependent features like: <column_one column_two>, no parenthesis, separated by a space
        # saving those numeric columns to a list 

        num_columns = input('Numeric dependent features: ').split()

        # for each column in this list of numeric columns, transform them into numeric if they are not already
        for x in (num_columns):
            X[x] = pd.to_numeric(X[x])
        display('converted')

    except Exception as e_6:
            print('ERROR at select_numeric_cols', {e_6})

    # making sure we keep our list of numeric columns saved       
    return num_columns


def histogram_jam(X, num_cols, labels_dict):
    
    """
    HELPER FUNCTION TO: output_viz(X, y, num_cols, target_column)
    
    DOCSTRING: inputs X (dependent variables as a df), 'num_cols', (list of 
    numeric columns), and labels_dict (dictionary of labels for vizualization,
    provided by output_viz.)
    
    Displays histogram of each numeric feature saved in "num_cols", 
    with proper labels on plots. 
    
    Returns nothing.
    """
    try: 
        # itterate to make all the histograms for each column in the dependant variables that are numeric columns:
        # make a histogram and label them in 'Title Case' from 'snake_case' 
        for col in X[num_cols]:
            fig, ax = plt.subplots()
            distributions = sns.histplot(data = X, x = col)
            distributions.set_title(f'{labels_dict[col]} Distributions in the Data')
            distributions.set_xlabel(f'{labels_dict[col]}')
            plt.xticks(rotation = 45)

    except Exception as e_7:
           print('ERROR at histogram_jam', {e_7})

           # returns NOTHING 
        

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
        # aggregating the df to group by target category by making a new df with all the numeric columns and y attached 
        # make a pivot table by grouping all the rows by the target outcomes, and getting the mean of each numeric column for aggrigation
        num_cols_df = pd.concat([X[num_cols], y], axis = 1)
        pivot_table = num_cols_df.groupby(by = num_cols_df[target_column]).mean()
        display(pivot_table)

        # saving our pivot table by returning it and saving it to a variable 
        return pivot_table

    except Exception as e_8:
        print ('ERROR at pivot_table_mean', {e_8})
        

def viz_numeric_vars_to_target(pivot_table, labels_dict, target_column):
    
    """
    HELPER FUNCTION TO: output_viz(X, y, num_cols, target_column)
    
    DOCSTRING: inputs 'pivot_table' (output from pivot_table_mean, a pivot table
    of the numeric features means as distributed by the categorical outcomes of 
    the target,) 'labels_dict' (a dictionary of labels for plotting), and 
    'target_column'(the name of the target column.)
    
    Displays a barplot for each numeric feature, with each categorical target outcome
    as a bar on the X axis. 
    """
    
    try: 

        # itterate to show relationships between the target and numeric dependant variables
        # for each column in the pivot table, make a barplot with the target outcome on the x axis
        # and the numeric feature on the y axis and make sure the plots are properly labeled with 'Title Case' labels

        for col in pivot_table.columns:
            fig, ax = plt.subplots()
            figure = sns.barplot(data = pivot_table,
                                 x = pivot_table.index,
                                 y = pivot_table[col])

            figure.set_title(f"{labels_dict[col]} Averaged by Class")
            figure.set_ylabel(f"{labels_dict[col]}")
            figure.set_xlabel(target_column.replace("_", " ").title())
            plt.xticks(rotation = 45)

        
    except Exception as e_9:
        print('ERROR at viz_numeric_vars_to_target', {e_9})
        # returns NOTHING 


def output_viz(X, y, num_cols, target_column):
    
    """
    HELPER FUNCTION TO: deploy_categorical_target_EDA()
    
    DEPLOY FUNCTION OF: histogram_jam, pivot_table_mean, and viz_vars_to_target
    
    DOCSTRING: 'X' (dependent variables in a df), 'y' (target feature), 'num_cols'
    (a list of the numerical dependent features), and 'target_column' as the name
    of the target feature. 
    
    Makes: 'labels_dict' for these visualizations
    
    Displays: histograms, pivot_table and accompanying barplots
    
    Returns nothing.
    """
    try: 
        # making labels for our plots by replacing '_' for ' ' and using 'upper()' 
        # making a dictionary to hold our labels 
        basic_labels = X.columns
        title_labels = [x.replace("_", " ").title() for x in basic_labels]
        labels_dict  = { basic_label:title_label for (basic_label,title_label) in zip(basic_labels, title_labels)} 

        # deploying histogram_jam and saving the output to 'histograms' 
        # deploying pivot_table_mean and saving the output as 'pivot_table' 
        # deploying viz_vars_to_target and saving the the output as viz_vars_to_target
        histogram_jam(X, num_cols, labels_dict)
        pivot_table = pivot_table_mean(X, num_cols, y, target_column)
        viz_numeric_vars_to_target(pivot_table, labels_dict, target_column)
        
    except Exception as e_10:
        print('ERROR at output_viz', {e_10})
        # returns NOTHING 


def deploy_categorical_target_EDA():
    
    """
    DEPLOY FUNCTION OF: select_target, select_numeric_cols, 
    select_cat_cols, other_output
    
    DOCSTRING: 
    
    The purpose of this functional protocol is to DEPLOY a semi-automated
    set of tables and visualizations to quickly get a first look at the data, 
    and become acquainted with the target and dependent variables.

    It's not designed to do any cleaning at the moment.

    It expects a categorical target, and dependent features to be either 
    categorical or numeric. It inputs a CSV.

    It displays:
    1) the target variable distribution, and distribution of all 
    other categorical features
    2) pivot table with the target as the index and the mean of each numeric feature
    3) histograms of each numeric feature's distribution
    4) barplot of the mean of each numeric column's mean on the x axis by each target category

    Returns: DF

    Each function has it's own docstring.
    
    WARNINGS: Not for use if selecting more than 10 or 12 numeric features at
    a time, or the barplots are going to be rendered useless. Not for producing 
    deliverables to clients, just for EDA purposes. 
    """
    # this big deploy function to all mini functions
    # 1) assign the return of input_csv to 'df'
    # 2) assign 'X', 'y' and 'target column' to be the return of select_target
    # 3) assinging num_cols and cat_cols to the functions that select them
    # 4) deploying the other visualizations and tables with 'other_output'
    try:
        df = input_csv()
        X, y, target_column = select_target(df)
        num_cols = select_numeric_cols(X)
        cat_cols = select_cat_cols(X)
        output_viz(X, y, num_cols, target_column)

        # saving the df as a return from this function so the user can continue on with their 
        # process without having to go back and redo and work 
        return df

    except Exception as deploy_exception:
        print({deploy_exception})