
from flair.models import TextClassifier
from flair.data import Sentence

def spamcleaner(text):
    classifier = TextClassifier.load('./utils/model/best-model.pt')
    sentence = Sentence(text)
    classifier.predict(sentence)
    print(sentence.labels)
    return(str(sentence.labels))