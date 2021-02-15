fpl-predictor
==============================

Using machine learning to predict Fantasy Premier League scores and pick the *playable* team with highest predicted score

General Idea
- clean data from FPL directly
- add predictions from FiveThirtyEight to provide team-level features (e.g. what's the probability Arsenal will win next weekend)
- predict points players will earn each gameweek
- use an optimizer  to determine best possible squad to field, given budget constraints
- use a transfer optimizer to determine best ways to use weekly transfer window

To-do's

- use FPL api to grab data directly, so data is always current
- make predictions on upcoming fixtures
- import my team to make transfer predictions for my current team (or any other team with teamid provided)

Further Ideas
- add in expected goals data from understat. This would help determine whether a player performed well but didn't earn points (signifying that they might still be a good pick, just got unlucky that week), or whether the player's underlying performance was poor. FPL has its own expected points stat -- I have no idea where this comes from or how effective it is.



Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
