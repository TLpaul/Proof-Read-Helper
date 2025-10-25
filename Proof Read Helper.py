import os
import re

try:
    import nltk
    from nltk.corpus import wordnet as wn
    HAVE_WORDNET = True
except Exception:
    HAVE_WORDNET = False

def read_file(file_path):
    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return None
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

def get_synonyms(word, max_syn=2):
    """
    Return a list of synonyms for `word` using WordNet.
    If WordNet isn't available, return None.
    """
    if not HAVE_WORDNET:
        return None
    syns = []
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            name = lemma.name().replace("_", " ")
            if name.lower() != word.lower() and name not in syns:
                syns.append(name)
                if len(syns) >= max_syn:
                    return syns
    return syns

def words_to_dict(text):
    """
    Returns two dicts:
      - counts: word -> frequency
      - positions: word -> list of word indices (1-based)
    """
    if text is None:
        return {}, {}
    words = re.findall(r"\b[\w']+\b", text.lower())  # keeps apostrophes inside words
    counts = {}
    positions = {}
    for i, w in enumerate(words, start=1):
        counts[w] = counts.get(w, 0) + 1
        positions.setdefault(w, []).append(i)
    return counts, positions

path = r"C:\Users\supre\Desktop\projects\Proof Read Helper\Text.txt"

text = read_file(path)
counts, positions = words_to_dict(text)

THRESHOLD = 8
print("Here are some suggestions for improving your writing. Words that appear more than", THRESHOLD, "times are listed with their synonyms (if available).")
# show results (example: print first 20 entries by frequency)
for i, (w, c) in enumerate(sorted(counts.items(), key=lambda x: -x[1]), start=1):
    if c > THRESHOLD:
        syns = get_synonyms(w)
        if syns is None:
            print(f"{w}: used {c} times — install NLTK WordNet to get synonyms (pip install nltk; then run python -m nltk.downloader wordnet)")
        elif len(syns) == 0:
            print(f"{w}: used {c} times — no synonyms found")
        else:
            print(f"{w}: synonyms -> {', '.join(syns)}")
    else:
        print(f"{w}: {c}")
    if i >= 20:
        break