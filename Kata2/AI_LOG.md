# AI Collaboration Log

## Overview
Throughout this assignment, I used AI as a technical reference, debugging assistant, and conceptual explainer while building a Python module that interacts with a SQLite database and using Git for version control. This log documents how I used AI, what I adopted or modified, and what I learned from the process.

---

## Interaction 1 – Git Feature Branch Workflow

**What I asked:**  
Whether `git checkout -b kata-02-sqlite` was enough to create a feature branch and begin working.

**What the AI provided:**  
Explained that the command creates and switches to a new branch, how commits behave on a branch, and how to verify the current branch.

**What I used, modified, or rejected:**  
Used the command and proceeded with development on the feature branch.

**Why I made those choices:**  
I needed to confirm I was following correct Git workflow before starting development.

**Where AI was wrong or unhelpful:**  
No issues; the explanation was accurate.

---

## Interaction 2 – Docstrings and Stretch Requirement

**What I asked:**  
What docstrings are and what the stretch requirement about indexes and EXPLAIN QUERY PLAN meant.

**What the AI provided:**  
Explained Python docstrings, public functions, database indexing, and how query plans demonstrate performance changes.

**What I used, modified, or rejected:**  
Used the explanation to structure functions and understand indexing requirements.

**Why I made those choices:**  
I needed to meet assignment requirements and ensure I understood the purpose of the stretch task.

**Where AI was wrong or unhelpful:**  
No issues; the explanation clarified both concepts well.

---

## Interaction 3 – Python Module Structure

**What I asked:**  
For a barebones Python module that met the assignment requirements.

**What the AI provided:**  
A minimal SQLite module structure with table creation, CRUD functions, seed function, join queries, and docstrings.

**What I used, modified, or rejected:**  
Used the structure but customized implementation details, naming, and data.

**Why I made those choices:**  
I needed a starting template but wanted the final code to reflect my own design decisions.

**Where AI was wrong or unhelpful:**  
No issues; the structure was helpful as a starting point.

---

## Interaction 4 – Seed Data Expansion

**What I asked:**  
How to expand seed data to include 10 airports and 20 flights.

**What the AI provided:**  
An example using lists and `executemany()` for batch insertion.

**What I used, modified, or rejected:**  
Used the pattern and adjusted data values.

**Why I made those choices:**  
More realistic data made join queries and indexing demonstrations clearer.

**Where AI was wrong or unhelpful:**  
No issues.

---

## Interaction 5 – Running the Module

**What I asked:**  
How to create a place to call my module functions.

**What the AI provided:**  
A minimal runner file with a main function and database calls.

**What I used, modified, or rejected:**  
Used the approach and kept the module separate from execution logic.

**Why I made those choices:**  
This allowed me to test functions cleanly while keeping the module reusable.

**Where AI was wrong or unhelpful:**  
Initial explanations were slightly more detailed than necessary but still useful.

---

## Interaction 6 – Preventing Seed Data Duplication

**What I asked:**  
How to make seed data run only once.

**What the AI provided:**  
Suggested checking whether records already exist before inserting.

**What I used, modified, or rejected:**  
Used this approach to prevent duplicate records.

**Why I made those choices:**  
I needed to safely rerun the program without duplicating rows.

**Where AI was wrong or unhelpful:**  
No issues.

---

## Interaction 7 – Debugging Function Calls

**What I asked:**  
Why `insert_airport()` was failing when I called it.

**What the AI provided:**  
Explained that the connection argument was missing and showed the correct usage.

**What I used, modified, or rejected:**  
Corrected the function calls accordingly.

**Why I made those choices:**  
I needed to resolve runtime errors and understand the cause.

**Where AI was wrong or unhelpful:**  
No issues.

---

## Interaction 8 – Preventing Duplicate Inserts and Overriding Records

**What I asked:**  
How to prevent duplicate inserts and how to override existing records on insert.

**What the AI provided:**  
Explained UNIQUE constraints and SQLite UPSERT using `ON CONFLICT DO UPDATE`.

**What I used, modified, or rejected:**  
Used UPSERT logic to handle existing airport codes.

**Why I made those choices:**  
This approach ensured predictable behavior and avoided silent failures.

**Where AI was wrong or unhelpful:**  
No issues.

---

## Interaction 9 – Understanding Query Plans

**What I asked:**  
What EXPLAIN QUERY PLAN output meant and what changed after indexing.

**What the AI provided:**  
Explained the difference between table scans and indexed searches and how SQLite executes queries.

**What I used, modified, or rejected:**  
Used this information to confirm that indexing was working correctly.

**Why I made those choices:**  
I needed to verify that the stretch requirement was correctly implemented.

**Where AI was wrong or unhelpful:**  
No issues.

---

## Interaction 10 – Repository Cleanup

**What I asked:**  
Whether the `__pycache__` folder was necessary.

**What the AI provided:**  
Explained that it is auto-generated and should not be committed, and how to ignore it in Git.

**What I used, modified, or rejected:**  
Ignored the directory in version control.

**Why I made those choices:**  
To keep the repository clean and follow standard practices.

**Where AI was wrong or unhelpful:**  
No issues.

---

## Interaction 11 – Git Merge Error

**What I asked:**  
Why a Git command using `&&` failed in PowerShell.

**What the AI provided:**  
Explained that PowerShell does not support `&&` as a command separator and showed the correct approach.

**What I used, modified, or rejected:**  
Ran commands separately and completed the merge.

**Why I made those choices:**  
I needed to complete the final merge step of the assignment.

**Where AI was wrong or unhelpful:**  
No issues.

---

## Reflection

Using AI during this assignment helped me move faster through setup steps and debugging while still requiring me to understand how the code worked. I found AI most useful for explaining unfamiliar concepts, such as query plans and UPSERT behavior, and for providing starting templates that I could modify rather than copy directly.  

One pattern I noticed is that asking very specific questions produced much better answers than asking broad ones. I also learned that it is important to verify and adapt AI-generated code instead of assuming it is immediately correct or perfectly suited to the assignment.  

Overall, AI functioned best as a collaborator and reference tool rather than a replacement for my own problem-solving. I became more efficient at identifying exactly what I needed help with and integrating those solutions into my own work.
