### Description:
**FileTypeTreemap** is a Python script that analyzes the file types within a specified directory and visualizes their sizes using a treemap. This tool is useful for understanding the distribution of different file types and identifying which file types occupy the most space.

#### Features:
- **File Size Analysis**: Collects information about file types and their sizes within a specified directory.
- **Treemap Visualization**: Creates a treemap to visually represent the distribution of file sizes by file type.
- **Handles Zero-Size Entries**: Removes any entries with zero size to avoid errors in visualization.

#### Usage:
1. Clone the repository.
2. Modify the `folder_path` variable in the script to point to the directory you want to analyze.
3. Run the script to generate and display the treemap.

#### Dependencies:
- `pandas`
- `matplotlib`
- `squarify`

Install the required packages using:
```bash
pip install pandas matplotlib squarify
```
