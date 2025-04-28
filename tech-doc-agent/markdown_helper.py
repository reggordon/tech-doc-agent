from jinja2 import Environment, FileSystemLoader
import os

# Path to the templates directory
template_folder = 'tools/templates'

# Create a Jinja2 environment
env = Environment(loader=FileSystemLoader(template_folder))

def create_markdown_template(doc_type, topic, overview, features, goals, timeline, risks):
    """Generates a Markdown document based on doc_type and content."""
    try:
        # Load the template based on the document type
        template = env.get_template(f"{doc_type.lower()}_template.md")

        # Render the template with the provided data
        return template.render(
            topic=topic,
            overview=overview,
            features=features,
            goals=goals,
            timeline=timeline,
            risks=risks
        )
    except Exception as e:
        raise ValueError(f"Template generation failed: {e}")


def save_markdown_to_file(content, file_path):
    """Save the generated content to a Markdown file."""
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Markdown saved as {file_path}")
