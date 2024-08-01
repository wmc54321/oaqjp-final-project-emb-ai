"""Server APIs of the webapp"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Return the index page"""
    return render_template('index.html')


@app.route('/emotionDetector')
def response_script_query():
    """Return response of emotion detector API"""
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return ("For the given statement, the system response is 'anger': " + str(result['anger']) +
        ", 'disgust': " + str(result['disgust']) +
        ", 'fear': " + str(result['fear']) +
        ", 'joy': " + str(result['joy']) +
        " and 'sadness': " + str(result['sadness']) +
        ". The dominant emotion is " + result["dominant_emotion"] + ".")
