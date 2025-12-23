import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from io import BytesIO
import base64
import urllib.parse

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        # Pollinations.ai - Free AI image generation API (no key needed)
        encoded_prompt = urllib.parse.quote(prompt)
        api_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
        
        response = requests.get(api_url, timeout=30)
        
        if response.status_code != 200:
            return jsonify({"error": "Failed to generate image"}), response.status_code
        
        # Load image from response
        image = Image.open(BytesIO(response.content))
    except Exception as e:
        return jsonify({"error": f"Failed to generate image: {str(e)}"}), 500

    # Convert image to base64
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    # Return the base64 image string
    return jsonify({"image": f"data:image/jpeg;base64,{img_str}"})

if __name__ == '__main__':
    app.run(debug=True)