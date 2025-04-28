import os
import streamlit as st
import stat
from tools.gdocs_loader import get_doc_text
from agents.document_builder_agent import DocumentBuilderAgent
from tools.formatter import convert_markdown_to_pdf, convert_markdown_to_docx
from markdown_helper import create_markdown_template, save_markdown_to_file

# Title of the web app
st.title("AI-Powered Document Builder")

# Input fields for the Google Doc ID, Topic, and Document Type
doc_id = st.text_input("Enter Google Doc ID:")
topic = st.text_input("Enter Document Topic:")
doc_type = st.selectbox("Select Document Type:", ["PRD", "TechnicalSpecification", "Essay", "UserGuide"])

# Ensure the output directory exists and is writable
output_dir = 'data/output_docs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to parse raw context into structured sections
def parse_context(context):
    """Parses raw text context into sections based on predefined headings."""
    context_split = context.split("\n")
    
    # Initialize sections as empty strings
    overview = ""
    features = ""
    goals = ""
    timeline = ""
    risks = ""

    # Parse content based on keywords like 'Overview', 'Features', etc.
    for line in context_split:
        if "Overview" in line:
            overview = line
        elif "Features" in line:
            features = line
        elif "Goals" in line:
            goals = line
        elif "Timeline" in line:
            timeline = line
        elif "Risks" in line:
            risks = line

    # Return the parsed sections
    return overview, features, goals, timeline, risks

# Function to handle the document generation and export options
def generate_and_export_document(doc_id, topic, doc_type):
    """Handles the entire document generation process and export to formats."""
    # Fetch content from the Google Doc
    context = get_doc_text(doc_id)
    
    # Check if content is successfully fetched
    if not context:
        st.error("Failed to fetch content from Google Doc.")
        return
    
    # Parse the raw text context into structured sections
    overview, features, goals, timeline, risks = parse_context(context)

    # Ensure template_data is a dictionary
    template_data = {
        'overview': overview,
        'features': features,
        'goals': goals,
        'timeline': timeline,
        'risks': risks
    }

    print(f"Template Data: {template_data}")

    # Generate the document template using the agent
    agent = DocumentBuilderAgent()
    generated_doc = agent.run(doc_type, topic, template_data)

    print(f"Generated Document: {generated_doc}")  # Debugging: Check the generated content

    # If document generation is successful
    if generated_doc:
        # Show the generated document in the UI
        st.subheader("Generated Document:")
        st.text_area("Document Content:", generated_doc, height=300)

        # Example paths for generated files
        pdf_path = f"data/output_docs/{topic.replace(' ', '_')}_{doc_type}.pdf"
        docx_path = f"data/output_docs/{topic.replace(' ', '_')}_{doc_type}.docx"
        markdown_path = f"data/output_docs/{topic.replace(' ', '_')}_{doc_type}.md"

        print(f"Saving PDF to: {pdf_path}")  # Debugging
        convert_markdown_to_pdf(generated_doc, pdf_path)
        st.success(f"PDF saved to {pdf_path}")
        get_pdf_download_button(pdf_path, f"{topic}_generated.pdf")

        print(f"Saving DOCX to: {docx_path}")  # Debugging
        convert_markdown_to_docx(generated_doc, docx_path)
        st.success(f"DOCX saved to {docx_path}")
        get_docx_download_button(docx_path, f"{topic}_generated.docx")

        print(f"Saving Markdown to: {markdown_path}")  # Debugging
        save_markdown_to_file(generated_doc, markdown_path)
        st.success(f"Markdown saved to {markdown_path}")
        get_markdown_download_button(markdown_path, f"{topic}_generated.md")

    else:
        st.error("Failed to generate document.")

# Function for PDF download button
def get_pdf_download_button(pdf_path, filename="document.pdf"):
    """Returns a download button for a PDF file"""
    with open(pdf_path, "rb") as f:
        pdf_file = f.read()
    return st.download_button(
        label="Download PDF",
        data=pdf_file,
        file_name=filename,
        mime="application/pdf"
    )

# Function for DOCX download button
def get_docx_download_button(docx_path, filename="document.docx"):
    """Returns a download button for a DOCX file"""
    with open(docx_path, "rb") as f:
        docx_file = f.read()
    return st.download_button(
        label="Download DOCX",
        data=docx_file,
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

# Function for Markdown download button
def get_markdown_download_button(markdown_path, filename="document.md"):
    """Returns a download button for a Markdown file"""
    with open(markdown_path, "r") as f:
        markdown_file = f.read()
    return st.download_button(
        label="Download Markdown",
        data=markdown_file,
        file_name=filename,
        mime="text/markdown"
    )

# Main execution logic: Trigger document generation and export
if st.button("Generate Document"):
    if doc_id and topic:
        generate_and_export_document(doc_id, topic, doc_type)
    else:
        st.error("Please enter all fields.")
