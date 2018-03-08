import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class Normalizer:
    stopWords = []
    symbols = "!@#$~%^&*()_-+={}[]/.,;|"
    def __init__(self):
        print("Normalizer init")
        nltk.download('punkt')
        nltk.download('stopwords')
        stopWords = set(stopwords.words('english'))

    def normalize(self, text):
        #Remove stopwords
        tokenizetext = word_tokenize(text)
        filteredWords = []

        for w in tokenizetext:
            if not self.isStoppedWord(self,w):
                filteredWords.append(w)

        print ("Normalized words",filteredWords)        
        fdist = nltk.FreqDist(filteredWords)
        print ("Normalizer FreqDist:",fdist)
        
        return filteredWords

    def isStoppedWord(self, word):
        return word in self.stopWords or word in self.symbols