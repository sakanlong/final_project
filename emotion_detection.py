import json
import requests

def emotion_detector(text_to_analyze):
    # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json={ "raw_document": { "text": text_to_analyze} }
    response = requests.post(url, json=input_json, headers=header)
    # Send a POST request to the API with the text and headers 
    response_dict = response.json()

    emo = response_dict['emotionPredictions'][0]['emotion']
    anger_score = emo['anger']
    disgust_score = emo['disgust']
    fear_score = emo['fear']
    joy_score = emo['joy']
    sadness_score = emo['sadness']
    
    sorted_emo = sorted(emo.items(), key=lambda item: item[1], reverse=True)

    dom_emo = max(emo, key=emo.get)
    highest_score = sorted_emo[0]

    #response_string = print(f"{'anger': {anger_score},'disgust': {disgust_score},'fear': {fear_score},'joy': {joy_score}, 'sadness':{sadness_score},'dominant_emotion': 'joy'}")

    return {'anger':anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': highest_score[0] }
