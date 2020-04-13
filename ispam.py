
from flair.models import TextClassifier
from flair.data import Sentence

classifier = TextClassifier.load('./model/best-model.pt')
sentence = Sentence("Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's")
classifier.predict(sentence)
print(sentence.labels)
