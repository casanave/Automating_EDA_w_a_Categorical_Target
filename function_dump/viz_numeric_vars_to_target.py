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
        counter = 0
        for index, col in enumerate(pivot_table.columns,start=1):
            fig, ax = plt.subplots()
            figure = sns.barplot(data = pivot_table,
                                 x = pivot_table.index,
                                 y = pivot_table[col])

            figure.set_title(f"{labels_dict[col]} Averaged by Class")
            figure.set_ylabel(f"{labels_dict[col]}")
            figure.set_xlabel(target_column.replace("_", " ").title())
            plt.xticks(rotation = 45)

            #    plt.savefig(f"{title_labels[counter]}")
            counter += 1;
        
    except Exception as e_9:
        print('ERROR at viz_numeric_vars_to_target', {e_9})