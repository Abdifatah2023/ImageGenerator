**AI Image Generator** (Gradio + OpenAI)

This project is a simple but powerful AI Image Generator application built using Gradio for the UI and OpenAI’s GPT-Image-1 model for backend image generation.
Users can enter a text prompt, and the app generates a high-quality AI image displayed directly in the browser.

**Installation & Setup**

1. Clone the project
git clone https://github.com/Abdifatah2023/ImageGenerator.git

2. Create and activate a virtual environment
   python -m venv venv
  source venv/bin/activate      # Mac/Linux
  venv\Scripts\activate         # Windows

4. Install dependencies
   pip install -r requirements.txt

6. Create a .env file
   Inside the root folder:
   OPENAI_API_KEY=your_api_key_here

**Running the App**

Start the Gradio interface:

gradio gradio_ui.py


Gradio will open in your browser, allowing you to type prompts and generate AI images.

