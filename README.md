Orientation
- all work is contained in predictor.ipynb

General Idea
- clean data from FPL directly
- add predictions from FiveThirtyEight to provide team-level features (e.g. what's the probability Arsenal will win next weekend)
- predict points players will earn each gameweek
- use an optimizer to determine best possible squad to field, given budget constraints
- use a transfer optimizer to determine best ways to use weekly transfer window

To-do's

- use FPL api to grab data directly, so data is always current
- make predictions on upcoming fixtures
- import my team to make transfer predictions for my current team (or any other team with teamid provided)

Further Ideas
- add in expected goals data from understat. This would help determine whether a player performed well but didn't earn points (signifying that they might still be a good pick, just got unlucky that week), or whether the player's underlying performance was poor. FPL has its own expected points stat -- I have no idea where this comes from or how effective it is.


