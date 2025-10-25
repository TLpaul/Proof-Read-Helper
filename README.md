# Proof Read Helper

Small Python tool that reads a text file, counts word frequencies, and suggests synonyms for words used above a configurable threshold (via NLTK WordNet) to help reduce repetition.

## Requirements
- Python 3.8+
- nltk library and WordNet data

## Install
Open PowerShell or CMD:
```powershell
python -m pip install --upgrade pip
python -m pip install nltk
python -m nltk.downloader wordnet
```

## Usage
1. Put the text to analyze in Text.txt at the project path (default path used in the script).
2. Run:
```powershell
python "Proof Read Helper.py"
```
3. Adjust THRESHOLD in the script to change when synonyms are shown.

## Notes
- If NLTK or WordNet is missing the script will show instructions to install them.
- Designed for Windows paths; edit the `path` variable if you store the text elsewhere.

## License
Unlicensed — adapt as needed.
