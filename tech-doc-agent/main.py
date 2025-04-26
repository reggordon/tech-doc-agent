from tools.gdocs_loader import get_doc_text
from agents.document_builder_agent import DocumentBuilderAgent
from tools.formatter import convert_markdown_to_pdf, convert_markdown_to_docx

# Replace this with a real Google Doc ID (just the ID, not the full URL)
doc_id = "1BnSYnvSBX67QMn6Zs3R3bo0_1dQFcS_MPWbMIBbZ3VY"
topic = "explain guolds theory of evolution"
doc_type = "PRD"

# Fetch the context from the Google Doc
context = get_doc_text(doc_id)

# Initialize the agent and generate the document
agent = DocumentBuilderAgent()
generated_doc = agent.run(doc_type, topic, context)

# If the document is generated successfully, save it in different formats
if generated_doc:
    markdown_file = f"data/output_docs/{topic.replace(' ', '_')}_{doc_type}.md"
    
    # Save as Markdown
    with open(markdown_file, "w") as f:
        f.write(generated_doc)
    print(f"Document saved as Markdown at {markdown_file}")
    
    # Convert to PDF and DOCX
    convert_markdown_to_pdf(generated_doc, f"data/output_docs/{topic.replace(' ', '_')}_{doc_type}.pdf")
    convert_markdown_to_docx(generated_doc, f"data/output_docs/{topic.replace(' ', '_')}_{doc_type}.docx")
else:
    print("Failed to generate document.")
