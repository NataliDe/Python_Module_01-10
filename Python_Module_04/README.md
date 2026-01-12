*This project has been created as part of the 42 curriculum by <ndemkiv>.*

# Description
**Data Archivist — Digital Preservation in the Cyber Archives** is a small training
project focused on Python fundamentals around file operations and stream management.

It contains 5 missions (Exercise 0–4) covering:
- Reading from a file vault (basic extraction)
- Writing a new archive (preservation mode)
- Using stdin/stdout/stderr correctly (3-channel communication)
- Safe resource management with `with` (vault security)
- Robust error handling with `try/except` (crisis response)

The subject requires specific filenames and output formats to simulate real archival
procedures.

# Instructions

## 1) Generate training files
Some exercises expect predefined files (e.g. `ancient_fragment.txt`,
`classified_data.txt`, `standard_archive.txt`).

Run the provided generator:
```bash
python3 tools/data_generator.py
```
This will create multiple .txt files and sample_data.json in the current directory.

## 2) Run exercises
```bash
    python3 ex0/ft_ancient_text.py
```

## Resources

Python docs: File I/O (open/read/write), context managers (with)
Python docs: sys module (stdin/stdout/stderr)
Exception handling: try/except/finally
Reference files used in this project:
tools/data_generator.py (training data generator)
sample_data.json (example metadata & test scenarios; reference-only)

## AI usage

AI was used to:
Turn the subject requirements into clean, minimal Python scripts for each exercise.
Match the expected output formatting shown in the subject examples.