import pypandoc
from docx import Document
import pdfkit

def convert_markdown_to_pdf(markdown_content, output_path):
    """Convert Markdown content to PDF using pdfkit and wkhtmltopdf."""
    try:
        # Convert markdown to HTML first
        html_content = pypandoc.convert_text(markdown_content, 'html', format='md')
        
        # Then convert HTML to PDF
        pdfkit.from_string(html_content, output_path)
        print(f"Document saved as PDF at {output_path}")
    except Exception as e:
        print(f"Error converting Markdown to PDF: {e}")

def convert_markdown_to_docx(markdown_content, output_path):
    """Convert Markdown content to DOCX using python-docx."""
    try:
        # Create a new Document
        doc = Document()
        
        # Add the markdown content as a paragraph (simple approach)
        doc.add_paragraph(markdown_content)
        
        # Save the DOCX file
        doc.save(output_path)
        print(f"Document saved as DOCX at {output_path}")
    except Exception as e:
        print(f"Error converting Markdown to DOCX: {e}")
