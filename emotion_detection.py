import requests

API_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
API_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze: str) -> str:
    input = { "raw_document": { "text": text_to_analyze } }
    r = requests.post(API_URL, json=input, headers=API_HEADERS);
    return r.text
