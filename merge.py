import os
from PyPDF2 import PdfReader, PdfWriter

def list_pdf_files(pdf_dir):
    """List PDF files in the given directory."""
    return [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]

def get_ordered_files(pdf_files):
    """Ask the user to choose the order of files one-by-one."""
    ordered_files = []
    remaining_files = pdf_files.copy()

    while remaining_files:
        print("\nRemaining files:")
        for i, file in enumerate(remaining_files, start=1):
            print(f"{i}. {file}")
        try:
            choice = int(input("Enter the number of the PDF file you want to add next: "))
            if 1 <= choice <= len(remaining_files):
                # Remove the chosen file from remaining_files and add to ordered_files
                chosen_file = remaining_files.pop(choice - 1)
                ordered_files.append(chosen_file)
            else:
                print("Invalid choice. Please choose a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return ordered_files

def merge_pdfs(ordered_files, pdf_dir, output_path):
    """Merge the PDFs in the order given and write to the output file."""
    pdf_writer = PdfWriter()

    for file in ordered_files:
        pdf_path = os.path.join(pdf_dir, file)
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
    
    with open(output_path, 'wb') as out_file:
        pdf_writer.write(out_file)
    print(f"Merged PDF saved as: {output_path}")

def main():
    pdf_dir = "pdfs"
    output_dir = "output"

    # Ensure the pdf directory exists
    if not os.path.exists(pdf_dir):
        print(f"Directory '{pdf_dir}' does not exist.")
        return

    pdf_files = list_pdf_files(pdf_dir)
    if not pdf_files:
        print("No PDF files found in the 'pdfs' directory.")
        return

    print("PDF files found:")
    for idx, file in enumerate(pdf_files, start=1):
        print(f"{idx}. {file}")

    ordered_files = get_ordered_files(pdf_files)

    # Ask for the output merged PDF name
    merged_pdf_name = input("Enter the name for the merged PDF (without .pdf extension): ").strip()
    if not merged_pdf_name.endswith('.pdf'):
        merged_pdf_name += '.pdf'
    output_path = os.path.join(output_dir, merged_pdf_name)

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    merge_pdfs(ordered_files, pdf_dir, output_path)

if __name__ == '__main__':
    main()
