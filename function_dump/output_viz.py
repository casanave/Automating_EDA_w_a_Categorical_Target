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
        # making labels for our plots 
        basic_labels = X.columns
        title_labels = [x.replace("_", " ").title() for x in basic_labels]
        labels_dict  = { basic_label:title_label for (basic_label,title_label) in zip(basic_labels, title_labels)} 

        histograms = histogram_jam(X, num_cols, labels_dict)
        pivot_table = pivot_table_mean(X, num_cols, y, target_column)
        viz_vars_to_target = viz_numeric_vars_to_target(pivot_table, labels_dict, target_column)
        
    except Exception as e_10:
        print('ERROR at output_viz', {e_19})