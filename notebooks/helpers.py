def score_model(df = None, predictions = None, y_test = None):
    '''function for scoring my fpl models, given just a dataframe with the predicted points as a column
    called 'predicted_points', or as an optional variable.'''
    #prep columns for scoring
    if df is None: #if not supplying a dataframe, create one from the given arrays
        import pandas as pd
        df = pd.DataFrame({'total_points': y_test.ravel(),
                           'predicted_points': predictions.ravel()})
    df['residuals'] = df['total_points'] - df['predicted_points']
    df['abs_error'] = abs(df['residuals'])

    #calculate score
    mae = df['abs_error'].mean()
    mae_over_5pts = df[df['total_points'] >= 6]['abs_error'].mean()
    score = (mae + mae_over_5pts*2)/3

    #return results
    print(f'Overall Score is: {score}')
    print(f'MAE over the entire dataset is: {mae}')
    print(f'MAE when a player earns more than 5pts is: {mae_over_5pts}')
    return df