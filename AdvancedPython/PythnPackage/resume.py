from PyPDF2 import PdfReader, PdfWriter

# Load the PDF file
reader = PdfReader("RushikeshKakde (1) (1).pdf")
writer = PdfWriter()

# Copy pages from the original PDF
for page in reader.pages:
    writer.add_page(page)

# Remove metadata
writer.metadata = {}

# Save the updated PDF
with open("RushikeshKakde.pdf", "wb") as output_pdf:
    writer.write(output_pdf)

print("Metadata removed and saved as updated_resume.pdf")
