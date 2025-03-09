import os
import tempfile
import shutil
import pytest
from PyPDF2 import PdfWriter, PdfReader
from merge import list_pdf_files, merge_pdfs
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def create_dummy_pdf(path, num_pages=1):
    """Creates a dummy PDF file with a specified number of blank pages."""
    writer = PdfWriter()
    for _ in range(num_pages):
        # Adds a blank page of default size
        writer.add_blank_page(width=72, height=72)
    with open(path, "wb") as f:
        writer.write(f)

def test_list_pdf_files():
    # Create a temporary directory and add dummy PDF and non-PDF files.
    temp_dir = tempfile.mkdtemp()
    try:
        pdf1 = os.path.join(temp_dir, "file1.pdf")
        pdf2 = os.path.join(temp_dir, "file2.PDF")  # Testing case-insensitivity
        txt_file = os.path.join(temp_dir, "notes.txt")
        create_dummy_pdf(pdf1)
        create_dummy_pdf(pdf2)
        with open(txt_file, "w") as f:
            f.write("This is a text file.")
        
        pdf_files = list_pdf_files(temp_dir)
        # Expecting only the two PDF files.
        assert len(pdf_files) == 2
        assert any("file1.pdf" == file.lower() for file in pdf_files)
        assert any("file2.pdf" == file.lower() for file in pdf_files)
    finally:
        shutil.rmtree(temp_dir)

def test_merge_pdfs():
    # Create temporary directories for PDFs and output.
    temp_pdf_dir = tempfile.mkdtemp()
    temp_output_dir = tempfile.mkdtemp()
    try:
        # Create two dummy PDFs with 1 and 2 pages respectively.
        pdf1 = "test1.pdf"
        pdf2 = "test2.pdf"
        pdf1_path = os.path.join(temp_pdf_dir, pdf1)
        pdf2_path = os.path.join(temp_pdf_dir, pdf2)
        create_dummy_pdf(pdf1_path, num_pages=1)
        create_dummy_pdf(pdf2_path, num_pages=2)
        
        ordered_files = [pdf1, pdf2]
        output_pdf = os.path.join(temp_output_dir, "merged.pdf")
        merge_pdfs(ordered_files, temp_pdf_dir, output_pdf)
        
        # Verify that the merged PDF has 3 pages in total.
        reader = PdfReader(output_pdf)
        assert len(reader.pages) == 3
    finally:
        shutil.rmtree(temp_pdf_dir)
        shutil.rmtree(temp_output_dir)
