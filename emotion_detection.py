import json
import requests

def emotion_detector(text_to_analyze):
    # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json={ "raw_document": { "text": text_to_analyze} }
    response = requests.post(url, json = input_json, headers=header)
    # Send a POST request to the API with the text and headers 
    return response.text # Return the response text from the API