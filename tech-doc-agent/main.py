from tools.gdocs_loader import get_doc_text

# Replace this with a real Google Doc ID (just the ID, not the full URL)
doc_id = "1GgTfHcQcDQyj4flsv1Ywtd196OCQ9DWneLw4I9OvWyA"

print("Fetching content from Google Docs...")
doc_text = get_doc_text(doc_id)
print("Doc contents:\n")
print(doc_text)
