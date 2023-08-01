# Image-to-Text and Text-to-Speech Pipeline

This project demonstrates a Python pipeline that utilizes Hugging Face's transformers library to perform image-to-text and text-to-speech conversions. The pipeline allows you to provide an image URL, extract text from the image, and then convert that text to speech using the ESPnet text-to-speech model. 

## Requirements

- Python 3.x
- dotenv
- transformers
- requests

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your_username/your_project.git
cd your_project
````
2. Create a .env file in the root directory and add your Hugging Face Hub API token

HUGGINGFACEHUB_API_TOKEN=your_api_token_here

3. Run the image-to-text and text-to-speech pipeline:
```bash 
python main.py
```


