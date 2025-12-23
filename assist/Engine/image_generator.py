import requests
import os
from PIL import Image
from io import BytesIO
import urllib.parse

# Function to send a prompt to Pollinations.ai and generate images (FREE, no API key needed)
def generate_image(prompt: str, output_path=None):

    folder_path = r"assist/Engine/Data"
    os.makedirs(folder_path, exist_ok=True)

    if output_path is None:
        output_path = os.path.join(folder_path, f"{prompt.replace(' ', '_')[:50]}.jpg")
    
    print(f"Generating image for prompt: '{prompt}'...")

    try:
        # Pollinations.ai - Free AI image generation API
        # Encode prompt for URL
        encoded_prompt = urllib.parse.quote(prompt)
        api_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
        
        # Get the image
        response = requests.get(api_url, timeout=30)
        
        if response.status_code != 200:
            raise Exception(f"Failed to generate image: {response.status_code}")
        
        # Load image from response
        image = Image.open(BytesIO(response.content))
        
        # Save the generated image
        image.save(output_path)
        print(f"Image saved as {output_path}")

        # Open the generated image
        image.show()
        
    except Exception as e:
        raise Exception(f"Image generation failed: {str(e)}")
    



