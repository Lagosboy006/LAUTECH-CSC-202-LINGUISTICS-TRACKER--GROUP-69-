# 📦 Imports
import os
import re
from collections import Counter
from modules.azura_loader import load_texts_from_folder  # ✅ Import from modules

# 📝 To collect output for the report
output_lines = []

# 🧠 Function: Readability Analysis
def simple_readability(text, label, output_list):
    sentences = re.split(r'[.!?]', text)
    sentences = [s for s in sentences if s.strip()]
    words = text.split()

    avg_sentence_length = len(words) / len(sentences) if sentences else 0
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0

    summary = (
        f"\n🧠 Readability for {label}:\n"
        f"📏 Avg Sentence Length: {avg_sentence_length:.2f} words\n"
        f"🔠 Avg Word Length: {avg_word_length:.2f} characters\n"
    )
    print(summary)
    output_list.append(summary)

# 📊 Function: Word Usage Tracking
def track_word_usage(text, word_list, label, output_list):
    text_lower = text.lower()
    word_counts = Counter(text_lower.split())

    section = f"\n📊 Word Usage in {label}:\n"
    print(section)
    output_list.append(section)

    for word in word_list:
        count = word_counts[word.lower()]
        line = f"🔹 {word}: {count}"
        print(line)
        output_list.append(line)

# 📂 Load Texts from Folders (✅ correct paths)
text_1800s = load_texts_from_folder("datatime/1800s")[0]
text_1900s = load_texts_from_folder("datatime/1900s")[0]
text_british = load_texts_from_folder("datadialects/british")[0]
text_american = load_texts_from_folder("datadialects/american")[0]
text_african = load_texts_from_folder("datadialects/african")[0]

# 🎯 Target Words to Track
target_words = ["honour", "color", "civilisation", "labour", "thee", "freedom"]

# ▶️ Readability Analysis
simple_readability(text_1800s, "1800s", output_lines)
simple_readability(text_1900s, "1900s", output_lines)
simple_readability(text_british, "British", output_lines)
simple_readability(text_american, "American", output_lines)
simple_readability(text_african, "African", output_lines)

# 📊 Word Usage Analysis
track_word_usage(text_british, target_words, "British", output_lines)
track_word_usage(text_american, target_words, "American", output_lines)
track_word_usage(text_african, target_words, "African", output_lines)
track_word_usage(text_1800s, target_words, "1800s", output_lines)
track_word_usage(text_1900s, target_words, "1900s", output_lines)

# 💾 Write Output to Report File
with open("analysis_report.txt", "w", encoding="utf-8") as f:
    for line in output_lines:
        f.write(line + "\n")

print("\n✅ Report saved to analysis_report.txt")

