fpl-predictor
==============================

Using machine learning to predict Fantasy Premier League scores and pick the *playable* team with highest predicted score

General Idea
- clean data from FPL directly
- engineer features using rolling windows on past player and team performance. Add in the opponents plast performance as well.
- predict points players will earn each gameweek
- use an optimizer  to determine best possible squad to field, given budget constraints
- use a transfer optimizer to determine best ways to use weekly transfer window

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


--------

<p><small>Project structure based loosely on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.</small></p>
