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

    It retruns nothing. 

    Each function has it's own docstring.
    
    WARNINGS: Not for use if selecting more than 10 or 12 numeric features at
    a time, or the barplots are going to be rendered useless. Not for producing 
    deliverables to clients, just for EDA purposes. 
    """
    
    try:
        df = input_csv()
        X, y, target_column = select_target(df)
        num_cols = select_numeric_cols(X)
        cat_cols = select_cat_cols(X)
        other_output = output_viz(X, y, num_cols, target_column)

    except Exception as deploy_exception:
        print({deploy_exception})