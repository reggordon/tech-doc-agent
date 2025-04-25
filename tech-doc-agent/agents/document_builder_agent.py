import ollama
from jinja2 import Environment, FileSystemLoader

class DocumentBuilderAgent:
    def __init__(self):
        # Initialize the Ollama client to use LLaMA model
        self.model = ollama.Client()

        # Set up Jinja2 environment for template rendering
        self.template_env = Environment(loader=FileSystemLoader('tools/templates'))

    def run(self, doc_type, topic, context):
        # Print the context and prompt for debugging purposes
        print("Context fetched from Google Docs:", context)
        
        # Construct the prompt for the LLaMA model
        prompt = f"Write a {doc_type} for the topic '{topic}' using the following information:\n\n{context}"

        print("Generated Prompt:", prompt)  # Debugging the prompt
        
        try:
            print("Sending request to LLaMA model...")
            # Call the LLaMA model via Ollama's client
            response = self.model.chat(model="llama3", messages=[
                {"role": "user", "content": prompt}
            ])
            
            # Check if the model responds correctly
            if 'message' in response:
                print("LLaMA Response:", response['message']['content'])
            else:
                print("Error: No valid response from model")
                return None

        except Exception as e:
            print(f"Error interacting with Ollama: {e}")
            return None

        # After receiving model output, use the template to structure the document
        print("Rendering document with template...")
        return self.render_template(doc_type, response['message']['content'])

    def render_template(self, doc_type, content):
        # Load the appropriate template based on document type (e.g., PRD, implementation plan)
        template = self.template_env.get_template(f"{doc_type.lower()}_template.md")
        
        # Render the template with the model content as the body of the document
        return template.render(body=content)
