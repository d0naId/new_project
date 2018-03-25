__author__ = 'yush'
from sklearn.externals import joblib


class SentimentClassifier(object):
    def __init__(self):
        self.pipeline = joblib.load('pipeline_log.pkl')
        self.classes_dict = {0: "negative", 1: "positive", -1: "prediction error"}

    @staticmethod
    def get_probability_words(probability):
        if probability < 0.55:
            return "neutral or uncertain"
        elif probability < 0.7:
            return "probably"
        elif probability > 0.95:
            return "certain"
        else:
            return ""

    def predict_text(self, text):
        try:
            for s in r'1234567890!@#$%ˆ&,*(.)?/><"[]{}|\-_+=' + "'":
                text = text.replace(s,' ')
            intermediate_text = ' '.join(text.split())
     
            return(self.pipeline.predict([intermediate_text])[0],
                       self.pipeline.predict_proba([intermediate_text])[0])
            
        except:
            print ("prediction error")
            return -1, 0.8

    def get_prediction_message(self, text):
        prediction = self.predict_text(text)
        class_prediction = prediction[0]
        prediction_probability = prediction[1][class_prediction]
        return self.get_probability_words(prediction_probability) + " " + self.classes_dict[class_prediction]