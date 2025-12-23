import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file in root directory
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
load_dotenv(os.path.join(root_dir, ".env"))

# API configuration for code generation
api_key = os.getenv("groq_api_key")
if not api_key:
    raise ValueError("Groq API key not found in .env file")

# Initialize Groq client
client = Groq(api_key=api_key)

def generate_code(task_prompt: str):
    print(f"Generating code for prompt: '{task_prompt}'...")
    
    try:
        # Use Groq's chat completion with code-focused model
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert Python programmer. Generate clean, well-commented Python code. Return only the code without explanations."
                },
                {
                    "role": "user",
                    "content": f"Write Python code for: {task_prompt}"
                }
            ],
            model="llama-3.3-70b-versatile",  # Great for code generation
            temperature=0.5,
            max_tokens=512
        )
        
        generated_code = response.choices[0].message.content
        
        # Clean up markdown code blocks if present
        if "```python" in generated_code:
            generated_code = generated_code.split("```python")[1].split("```")[0].strip()
        elif "```" in generated_code:
            generated_code = generated_code.split("```")[1].split("```")[0].strip()
        
        return generated_code
    except Exception as e:
        raise Exception(f"Code generation failed: {str(e)}")
