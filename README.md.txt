# 📚 Linguistic Tracker Project

This project analyzes language changes over time and across dialects using English text corpora. It helps track how word usage, structure, and style evolve in literature and written works.

---

## 📁 Project Structure

linguistic_tracker_project/
├── data_time/
│   ├── 1800s/              # e.g., Pride and Prejudice
│   └── 1900s/              # e.g., The Great Gatsby
│
├── data_dialects/
│   ├── british/
│   ├── american/
│   └── african/
│
├── modules/
│   └── corpus_loader.py    # Python modules (more will be added)
│
├── main.py                 # Main script to run the analysis
└── README.md               # Project documentation

---

## ▶️ How to Use

1. Put your text files into the appropriate folders (time or dialect).
2. Run this in your terminal to start the analysis:

   python main.py

---

## 🔧 Dependencies

You can run the basic version with just Python.

Optional (for more features later):
- textstat
- nltk
- spacy

Install extras with:

   pip install textstat nltk spacy

---

## 🧠 Features Coming Soon

- Word frequency analysis
- Readability comparison
- Language change tracking
- Report generation
