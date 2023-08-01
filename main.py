from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import requests
import os

load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# image to text
def img_to_text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    text = image_to_text(url)[0]["generated_text"]

    print(text)
    return text



# text to speech 
def text_to_speech(text):

    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}

    payloads = {
        "inputs":text
    }
    response = requests.post(API_URL, headers=headers, json=payloads)
    with open('audio.flac', 'wb') as file:
        file.write(response.content)

text_to_speech(img_to_text('test2.jpg'))