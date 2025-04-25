import pypandoc
from weasyprint import HTML
from docx import Document

def convert_markdown_to_pdf(markdown_content, output_path):
    """Convert Markdown content to PDF using WeasyPrint."""
    try:
        # Convert markdown to HTML first using pypandoc
        html_content = pypandoc.convert_text(markdown_content, 'html', format='md')
        
        # Convert HTML to PDF using WeasyPrint
        HTML(string=html_content).write_pdf(output_path)
        
        print(f"Document saved as PDF at {output_path}")
    except Exception as e:
        print(f"Error converting Markdown to PDF: {e}")
        raise  # Reraise the exception for further handling in the main app


def convert_markdown_to_docx(markdown_content, output_path):
    """Convert Markdown content to DOCX using python-docx."""
    try:
        # Convert markdown to HTML first using pypandoc
        html_content = pypandoc.convert_text(markdown_content, 'html', format='md')
        
        # Create a new Document using python-docx
        doc = Document()
        
        # Add HTML content as a paragraph (simplified, you can add more complex parsing here)
        doc.add_paragraph(html_content)

        # Save the document as DOCX
        doc.save(output_path)
        print(f"Document saved as DOCX at {output_path}")
    except Exception as e:
        print(f"Error converting Markdown to DOCX: {e}")
        raise  # Reraise the exception for further handling in the main app
