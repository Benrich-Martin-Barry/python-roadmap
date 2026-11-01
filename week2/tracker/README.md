# Expense Tracker

A command-line program that records expenses and shows totals.
Data is saved to a JSON file, so it is still there after you close the program.

## How it works

- `main.py`: the menu (add, view, total, total by category, quit)
- `logic.py`: adds expenses and calculates totals
- `storage.py`: loads and saves the expenses to `expenses.json`

## Run it

    cd week2/tracker
    python main.py

## What I practised

Lists and dictionaries, functions, loops, JSON file handling,
splitting code into modules, and testing by hand.