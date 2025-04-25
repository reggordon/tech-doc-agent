from tools.gdocs_loader import get_doc_text
from agents.document_builder_agent import DocumentBuilderAgent

# Replace this with a real Google Doc ID (just the ID, not the full URL)
doc_id = "1PIY-j10Wd3nrsHxk1CBzBzrpVugkbmPYj-ejiSs7WuI"
topic = "Netcetera 3DS Sandbox Integration"
doc_type = "PRD"


# Get the content from the Google Doc
context = get_doc_text(doc_id)

# Initialize the DocumentBuilderAgent
agent = DocumentBuilderAgent()

# Generate the document based on the context, doc type, and topic
generated_doc = agent.run(doc_type, topic, context)

# Print the generated document to check if the agent is returning valid output
print(generated_doc)

# Save the generated document to a file
with open(f"data/output_docs/{topic.replace(' ', '_')}_{doc_type}.md", "w") as f:
    f.write(generated_doc)

print(f"Document saved to data/output_docs/{topic.replace(' ', '_')}_{doc_type}.md")
