import ollama

# Create Ollama client
client = ollama.Client()

# Send a test prompt to LLaMA
response = client.chat(model="llama3", messages=[{"role": "user", "content": "Hello, how are you?"}])

# Print the response to check if it's working
print(response)
