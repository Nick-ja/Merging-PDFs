import os
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger

# Create the main window (this won't appear to the user)
root = tk.Tk()
root.withdraw()  # Hide the main window

# Ask the user to select multiple PDFs
pdf_files = filedialog.askopenfilenames(title="Select PDFs to Merge", filetypes=[("PDF files", "*.pdf")])
if not pdf_files:
    print("No PDFs selected. Exiting program.")
    exit()

# Ask the user for the name of the output file
output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Save Output PDF as")
if not output_file:
    print("No output file selected. Exiting program.")
    exit()

# Merge the PDFs
merger = PdfMerger()
for pdf in pdf_files:
    merger.append(pdf)

# Save the merged PDF
merger.write(output_file)
merger.close()

print(f"Pdfs merged into {output_file}!")
