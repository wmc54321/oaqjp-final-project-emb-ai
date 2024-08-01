import requests, json

API_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
API_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze: str) -> dict:
    # request and get response
    input = { "raw_document": { "text": text_to_analyze } }
    r = requests.post(API_URL, json=input, headers=API_HEADERS);
    json_text = json.loads(r.text)

    emotions = json_text['emotionPredictions'][0]['emotion']
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': max(emotions, key=emotions.get)
    }
