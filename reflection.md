# Reflection — Data Cleaning with GitHub Copilot

## What Copilot Generated
To generate parts of my script, I wrote comments above the functions describing
what I wanted them to do. For example, above `load_data` and
`clean_column_names`, I added a short explanation and then paused to let
Copilot generate suggestions. Copilot produced a function that loaded a CSV
using pandas and another that standardized column names. These served as my
starting points. I accepted the general structure of the suggestions, then
rewrote parts so they better matched the assignment requirements.

## What I Modified
For `clean_column_names`, Copilot originally used a longer chain of replacements
and attempted to fix several patterns at once. I simplified the logic to only
lowercase the names, strip whitespace, and replace spaces with underscores.
For `handle_missing_values`, Copilot suggested filling missing prices with 0,
but I changed the logic to dropping those rows because replacing prices with 0
would distort the dataset. In `remove_invalid_rows`, Copilot included several
extra checks, so I rewrote the condition to only remove rows where price or
quantity is negative.

## What I Learned
This project helped me understand the importance of creating a clean pipeline
with small, modular functions. I also learned how helpful Copilot can be for
quickly generating boilerplate code, but it does not always choose the best
logic—for example, filling missing prices with 0 can create misleading data.
I learned that AI coding tools work best when I already know what the function
should do, and I can evaluate and refine the output. Overall, this project gave
me practice with responsible AI usage and a more professional approach to
structuring Python projects.
