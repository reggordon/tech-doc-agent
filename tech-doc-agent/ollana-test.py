import ollama

try:
    client = ollama.Client()

    response = client.chat(model="llama3", messages=[{"role": "user", "content": "Hello, how are you?"}])
    print(response)
except Exception as e:
    print(f"Error: {e}")
