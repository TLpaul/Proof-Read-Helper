Reads a text file, counts word frequencies, and suggests synonyms (via NLTK WordNet) for words used above a configurable threshold to help reduce repetition.

## Requirements
- Python 3.8+
- nltk (and WordNet data if you want synonyms)

## Install
Open PowerShell/CMD:
```powershell
python -m pip install --upgrade pip
python -m pip install nltk
python -m nltk.downloader wordnet
```

## Usage
1. Put text to analyze in Text.txt (or edit the `path` variable in the script).
2. Run:
```powershell
python "Proof Read Helper.py"
```
3. Change `THRESHOLD` in the script to adjust when synonyms are shown.

## Example output (terminal)

With WordNet installed:
```
Here are some suggestions for improving your writing. Words that appear more than 8 times are listed with their synonyms (if available).
the: 25
data: synonyms -> information, facts
analysis: synonyms -> examination, study
python: 9
and: 7
```

Without WordNet installed:
```
Here are some suggestions for improving your writing. Words that appear more than 8 times are listed with their synonyms (if available).
data: used 12 times — install NLTK WordNet to get synonyms (pip install nltk; then run python -m nltk.downloader wordnet)
the: 25
python: 9
```

## Notes
- The script prints the top results sorted by frequency (first 20 by default).
- Commit images to the repo and reference them in this README if you want screenshots.

## License
Unlicensed — adapt as needed.
