# PDF Merger

This project provides a Python script to merge PDF files locally. By processing PDFs on your own machine rather than using online services, your data remains private and secure.

## Features

- **Local Processing:** Merges PDF files without uploading them online.
- **Custom Order:** Allows you to specify the order in which PDFs are merged.
- **Simple Interface:** Interactively choose the PDF order and set the output filename.
- **Data Privacy:** This project performs all PDF merging locally, ensuring that your data remains private. Unlike online PDF merging tools, your files are not uploaded to any server, providing a secure way to handle sensitive documents.


## Setup

### 1. Create a Virtual Environment

Create a virtual environment to manage dependencies:
```bash
python -m venv myenv

Activate the virtual environment:

On Windows:
myenv\Scripts\activate
On macOS/Linux:
source myenv/bin/activate

2. Install Dependencies
Install the required package:
pip install PyPDF2

Project Structure
.
├── merge.py       # Main script for merging PDFs
├── pdfs/          # Directory containing PDF files to merge
├── output/        # Directory where the merged PDF will be saved
├── tests/         # Unit tests for the merging functionality
├── Makefile       # Makefile to run the script or tests
└── README.md      # Project documentation

Running the Script
To merge PDFs, place the PDF files in the pdfs/ directory and run:

make run
Follow the prompts to select the order of the PDFs and to name the merged file. The output will be saved in the output/ directory.

Running Tests
The tests are located in the tests/ directory. To run them, execute:

make test


---

### Usage Summary

1. **Set Up a Virtual Environment:**
   ```bash
   python -m venv myenv
   source myenv/bin/activate   # On Windows use: myenv\Scripts\activate
   pip install PyPDF2
Place your PDFs in the pdfs/ directory.
Run the Merge Script:
make run
Run Tests (optional):
make test