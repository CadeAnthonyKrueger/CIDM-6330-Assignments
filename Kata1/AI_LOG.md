# AI Collaboration Log – Weather Data Filtering Script

## Assignment Goal
Create a Python script that:
- Reads weather station data
- Filters records based on command-line thresholds
- Writes filtered results to a CSV file
- Logs operations (records read, records written, timestamp)
- Stretch goal: Support both CSV and JSON input formats

---

## Step 1 – Planning Program Structure

**What I asked AI**
- What components a script like this should include
- Whether I needed functions like `parse_args()`, a logger, and `main()`

**What AI provided**
- Suggested structuring the program with:
  - `parse_args()` for CLI arguments  
  - `main()` for orchestration  
  - Helper functions for reading, filtering, and writing data  

**What I used**
- I adopted this structure and built the script around it.

**What I modified or decided myself**
- I chose which filters to implement (TMAX and PRCP) and how thresholds should behave.

**Why**
- Separating responsibilities makes the script easier to read and maintain.

---

## Step 2 – Designing Command-Line Arguments

**What I asked AI**
- How `argparse` maps argument names to variables
- How to design threshold arguments

**What AI provided**
- Explained that hyphenated arguments like `--temp-threshold-max` become `args.temp_threshold_max`.

**What I used**
- I used this naming convention when referencing parsed arguments in the code.

**What I modified**
- I chose argument names and made both thresholds optional.

**Why**
- Optional thresholds allow filtering by temperature, precipitation, or both.

---

## Step 3 – Implementing Filtering Logic

**What I asked AI**
- How to handle cases where thresholds are optional
- How to avoid errors when comparing values to `None`

**What AI provided**
- Suggested conditional checks before parsing and comparing values.

**What I used**
- I implemented conditional parsing and filtering logic.

**What I modified**
- I changed the logic so temperature and precipitation are parsed only when their filters are active.

**Why**
- Prevents rows from being skipped unnecessarily and avoids runtime errors.

---

## Step 4 – Supporting CSV and JSON Input (Stretch Goal)

**What I asked AI**
- Where to add functionality to interpret CSV vs JSON input

**What AI provided**
- Suggested creating helper functions:
  - `read_records()`
  - `read_csv()`
  - `read_json()`

**What I used**
- I implemented these helper functions and used file extension detection.

**What I modified**
- I simplified assumptions about JSON structure to expect a list of records.

**Why**
- Keeps the implementation simple while still meeting the stretch requirement.

---

## Step 5 – Program Flow and Separation of Concerns

**What I asked AI**
- Whether logging should be inside filtering functions or handled elsewhere

**What AI provided**
- Recommended keeping filtering logic separate from logging and handling logging in `main()`.

**What I used**
- I kept filtering functions pure and handled file writing and logging in `main()`.

**Why**
- Improves modularity and keeps functions focused on single responsibilities.

---

## Step 6 – Error Handling and Robustness

**What I asked AI**
- How to gracefully handle missing files and invalid numeric values

**What AI provided**
- Suggested:
  - Checking file existence using `pathlib`
  - Catching `ValueError` and `TypeError` when parsing floats

**What I used**
- I implemented these error-handling practices.

**Why**
- Prevents crashes and meets assignment requirements for graceful failure.

---

## Where AI Was Wrong or Less Helpful

- AI initially assumed different argument names than I used, which caused confusion until corrected.
- Some suggestions were more complex than necessary for the assignment, so I simplified them to match requirements.

---

## Reflection

AI was most useful for:
- Explaining `argparse` behavior
- Suggesting program structure
- Helping refine filtering logic
- Reviewing error handling and modular design

I made the final decisions about:
- Which filters to implement
- How thresholds behave
- How records are processed and written
- How helper functions are structured

The development process was iterative: I wrote code, tested it, asked targeted questions, and refined the implementation step by step.