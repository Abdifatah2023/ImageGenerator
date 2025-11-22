import os
import base64
from openai import OpenAI
from PIL import Image
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_image(prompt: str) -> str:
    # Generate the image
    img = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    # Decode base64
    image_bytes = base64.b64decode(img.data[0].b64_json)

    # Save file
    output_path = "output.png"
    with open(output_path, "wb") as f:
        f.write(image_bytes)

    return output_path


def handle_input(text: str):
    # Generate + get file path
    path = generate_image(text)

    # Open and return PIL image
    image = Image.open(path)
    
    return image
