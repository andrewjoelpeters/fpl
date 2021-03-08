fpl-predictor
==============================

Using machine learning to predict Fantasy Premier League scores and pick the *playable* team with highest predicted score

General Idea
- Gather historic data, join with current season data pulled via the fantasy.premierleague.com API (notebook 1)
- Engineer features using rolling windows on past player and team performance. Add in the opponents past performance as well. (notebook 2)
- Develop and test a baseline, non-ML technique for predicting a player's scores using averages of past performance. I use this to see if the ML model I later develop is actually an improvement on a baseline heuristic. (notebook 3)
- Train ML model (notebooks 4 & 5)
- Used trained model to predict points players will earn in fixtures in the future (notebooks 6 & 7)
- use an optimizer to optimize predicted points earned, given budget constraints, constraints on positions, etc. (notebook 8)
- use a transfer optimizer to determine best ways to use weekly transfer window (notebook 9)

All of my original exploration, EDA, etc., is in the notebooks/archive/predictor.ipynb notebook. 

Further Ideas
- add in expected goals data from understat. This would help determine whether a player performed well but didn't earn points (signifying that they might still be a good pick, just got unlucky that week), or whether the player's underlying performance was poor. FPL has its own expected points stat -- I have no idea where this comes from or how effective it is.


Project Organization
------------

    ├── README.md          <- The top-level README
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, and model predictions
    │
    ├── notebooks          <- Jupyter notebooks. Helper programs are also in here for ease of use
    │
    ├── references       


**Models**

| Model     | Description | Overall Score | Performance with Players Getting Over 5 Pts
| ----------- | ----------- | ----------- | -----------
| xgb_256      | Model trained on all data except top .05% of single-game points | 2.56 | 3.04
| xgb_pts_per_min | Model trained on all data except top .05% of single-game points. Instead of target value being total # of pts, target value is the pts earned per minuted played. Predictions were multiplied by actual minutes played (model is assuming perfect forecast of minutes played) | 2.37 | 2.48
| xgb_254 | Same as 256, but with an optimized num_estimators (30) | 2.54 | 3.00
| xgb_forward_rolling_232 | model trained to predict aggregated scores over next 3 gws. Significantly improved scores when players earn over 5 pts in a gw  | 2.32 | 2.48

--------

<p><small>Project structure based loosely on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.</small></p>
