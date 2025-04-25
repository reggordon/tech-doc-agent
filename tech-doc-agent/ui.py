import streamlit as st
from tools.gdocs_loader import get_doc_text
from agents.document_builder_agent import DocumentBuilderAgent
from tools.formatter import convert_markdown_to_pdf, convert_markdown_to_docx


# Title of the web app
st.title("AI-Powered Document Builder")

# Input fields for the Google Doc ID, Topic, and Document Type
doc_id = st.text_input("Enter Google Doc ID:")
topic = st.text_input("Enter Document Topic:")
doc_type = st.selectbox("Select Document Type:", ["PRD", "Technical Specification", "User Guide"])

# Button to trigger document generation
if st.button("Generate Document"):
    if doc_id and topic:
        # Fetch content from the Google Doc
        context = get_doc_text(doc_id)
        
        # Check if content is successfully fetched
        if not context:
            st.error("Failed to fetch content from Google Doc.")
        else:
            # Generate the document using the agent
            agent = DocumentBuilderAgent()
            generated_doc = agent.run(doc_type, topic, context)

            # If document generation is successful
            if generated_doc:
                # Show the generated document in the UI (for reference)
                st.subheader("Generated Document:")
                st.text_area("Document Content:", generated_doc, height=300)

                # Allow export options
                export_pdf = st.button("Export as PDF")
                export_docx = st.button("Export as DOCX")

                if export_pdf:
                    convert_markdown_to_pdf(generated_doc, f"data/output_docs/{topic.replace(' ', '_')}_{doc_type}.pdf")
                    st.success(f"PDF saved to data/output_docs/{topic.replace(' ', '_')}_{doc_type}.pdf")
                
                if export_docx:
                    convert_markdown_to_docx(generated_doc, f"data/output_docs/{topic.replace(' ', '_')}_{doc_type}.docx")
                    st.success(f"DOCX saved to data/output_docs/{topic.replace(' ', '_')}_{doc_type}.docx")

            else:
                st.error("Failed to generate document.")
    else:
        st.error("Please enter all fields.")
