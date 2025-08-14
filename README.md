Linguistics Tracker (CLI)

A Python-based tool for analyzing text readability and tracking specific word usage across different time periods and dialects.
Ideal for linguistic research, historical text comparison, and dialect variation studies.

 About the Project

This project was developed as part of the LAUTECH CSC 202 coursework to demonstrate practical applications of Python in text processing and computational linguistics.
It allows users to explore how language changes over time and across regions, providing quantitative metrics and word frequency counts.
The tool is simple, lightweight, and works entirely via the command line — no extra libraries required.

 Features

Readability Analysis — calculates:

Average sentence length (in words)

Average word length (in characters)

Word Usage Tracking for predefined target words

Supports Multiple Datasets:

Time-based (e.g., 1800s vs. 1900s)

Dialect-based (e.g., African, American, British)

Generates a Detailed Report (analysis_report.txt)

Simple Command-Line Interface (CLI) for quick usage

 Dataset Structure
datatime/
 ├── 1800s/
 │    └── sample.txt
 ├── 1900s/
 │    └── sample.txt

datadialects/
 ├── african/
 │    └── sample.txt
 ├── american/
 │    └── sample.txt
 ├── british/
 │    └── sample.txt

modules/
 └── azura_loader.py

run_tracker.py
analysis_report.txt
README.md

 How to Run
1️⃣ Clone the Repository
git clone https://github.com/Lagosboy006/LAUTECH-CSC-202-LINGUISTICS-TRACKER--GROUP-69-.git
cd LAUTECH-CSC-202-LINGUISTICS-TRACKER--GROUP-69-

2️⃣ Run the Program
python run_tracker.py

 Output

The program will:

Display results in the terminal

Save a full report as analysis_report.txt

Example:

 Readability for British:
 Avg Sentence Length: 14.25 words
 Avg Word Length: 5.12 characters

 Word Usage in British:
🔹 honour: 3
🔹 color: 0
🔹 civilisation: 1
...
 Report saved to analysis_report.txt

 Example Target Words

honour

color

civilisation

labour

thee

freedom

 Requirements

Python 3.7+

No external libraries required (uses built-in Python modules)

Notes

Ensure that dataset folder structure is maintained for the script to work properly.

You can replace the sample text files with your own datasets.









