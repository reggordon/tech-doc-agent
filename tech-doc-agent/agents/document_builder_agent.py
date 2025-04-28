import ollama
from jinja2 import Environment, FileSystemLoader

class DocumentBuilderAgent:
    def __init__(self):
        # Initialize the Ollama client to use LLaMA model
        self.model = ollama.Client()

        # Set up Jinja2 environment for template rendering
        self.template_env = Environment(loader=FileSystemLoader('tools/templates'))

    def run(self, doc_type, topic, template_data):
        try:
            print(f"Running agent with doc_type: {doc_type}, topic: {topic}")
            print(f"Template data being passed: {template_data}")

            # Ensure template_data is a dictionary
            if not isinstance(template_data, dict):
                raise ValueError(f"Expected template_data to be a dictionary, got {type(template_data)}")

            # Load the appropriate template based on doc_type (e.g., PRD, implementation plan)
            template_file = f"{doc_type.lower()}_template.md"  # Dynamically load based on doc_type
            print(f"Loading template: {template_file}")  # Debugging line
            template = self.template_env.get_template(template_file)

            # Render the template with the provided data
            rendered_doc = template.render(
                topic=topic,
                overview=template_data['overview'],
                features=template_data['features'],
                goals=template_data['goals'],
                timeline=template_data['timeline'],
                risks=template_data['risks']
            )

            # Debugging: Print the rendered document to check if rendering worked correctly
            print(f"Rendered document: {rendered_doc}")

            # Ensure LLaMA Model Call happens after template rendering
            model_input = f"Generate a document for {doc_type} about {topic}."
            print(f"Sending to LLaMA model: {model_input}")  # Debugging line

            # Send the input to the LLaMA model and get a response
            response = self.model.chat(model="llama3", messages=[{"role": "user", "content": model_input}])

            # Debugging: Print the response from the LLaMA model
            print(f"Response from LLaMA model: {response}")

            # Get the content from the response
            generated_content = response['message']['content']
            print(f"Generated content from model: {generated_content}")

            # Combine the rendered document and generated content
            final_document = f"{rendered_doc}\n\n{generated_content}"

            # Return the final document
            return final_document

        except Exception as e:
            print(f"Error in DocumentBuilderAgent: {e}")
            return None
        finally:
            # Ensure proper cleanup (e.g., closing resources, freeing memory)
            self.cleanup()

    def cleanup(self):
        # Optionally, you can add any cleanup logic here.
        # For example, closing files, releasing resources, etc.
        print("Cleaning up resources...")
        # No explicit 'disconnect' for Ollama client but ensure we manage resources properly.
        self.model = None  # Optionally set the model to None to release it

    def render_template(self, doc_type, content):
        try:
            # Load the appropriate template based on document type (e.g., PRD, implementation plan)
            template_file = f"{doc_type.lower()}_template.md"  # Dynamically load based on doc_type
            template = self.template_env.get_template(template_file)
            
            # Render the template with the model content as the body of the document
            rendered_content = template.render(body=content)
            
            return rendered_content
        except Exception as e:
            print(f"Error in render_template method: {e}")
            return None
