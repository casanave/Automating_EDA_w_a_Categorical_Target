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
        counter = 0
        ### itterate to make all the histograms 
        for col in X[num_cols]:
            fig, ax = plt.subplots()
            distributions = sns.histplot(data = X, x = col)
            distributions.set_title(f'{labels_dict[col]} Distributions in the Data')
            distributions.set_xlabel(f'{labels_dict[col]}')
            plt.xticks(rotation = 45)

            counter += 1;
            
    except Exception as e_7:
           print('ERROR at histogram_jam', {e_7})
        