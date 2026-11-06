# PPML Lab Programs – VS Code

This folder contains Python programs arranged Assignment-wise, based on the uploaded PPML Lab manual (Assignments 1–10). Some programs have been cleaned up so they run correctly in current Python versions.

## Open in VS Code
1. Extract `PPML_Lab_VSCode.zip`.
2. Open VS Code.
3. Select **File → Open Folder** and choose `PPML_Lab_VSCode`.
4. Open any assignment folder and select a `.py` file.
5. Run it using the **Run Python File** button (top-right), or in the terminal:
   `python filename.py`

## Install required libraries
Open the VS Code terminal and run:
```bash
python -m pip install numpy pandas matplotlib
```
Programs using only Python's built-in features do not need extra libraries.

## Folder structure
- Assignment_01 to Assignment_07: core Python, lists, functions, dictionaries, sets, lambda, map
- Assignment_08: NumPy
- Assignment_09: Pandas
- Assignment_10: Matplotlib plots

## Note
For Assignment 9, Program 3, add your own `sample.csv` and `sample.json` files to that program's folder before running. Use only trusted input when running examples that use `eval()`.
