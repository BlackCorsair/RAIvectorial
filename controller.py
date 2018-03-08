import nltk
from nltk.tokenize import word_tokenize
from pathlib import Path
from dbmanager import DBManager
from htmlparser import HTMLParser

nltk.download('punkt')


class Controller:
        directory = ""
        manager = DBManager
        parser = HTMLParser

        def __init__(self):
                print("Controller init")
                self.directory = "docrepository"
                manager = DBManager()
                parser = HTMLParser()

        def main(self):
                print('Options: 1-setup 2-run 3-exit')
                while True:
                        text = input("> ")
                        if(text == '1'):
                                self.setup()
                        elif(text == '2'):
                                self.displayResults()
                        elif(text == '3'):
                                break
                        else:
                                print("Invalid input")

        def setup(self):
                print("Found the following files:")
                p = Path(self.directory)
                for i in p.iterdir():  # glob('*.*'):
                        print("Working on file:", i.name)
                        path = Path.cwd().joinpath(self.directory +
                                                   "\\" + i.name)
                        with path.open('r', encoding='utf-8',
                                       errors='replace') as file:
                                # Parser
                                filetext = self.parser.parse(self, file)
                                # Normalizer
                                # Tokenizer
                                # Save to DB
                                print(filetext)
                                fdist = nltk.FreqDist(word_tokenize(filetext))
                                print(fdist)
                                # for term in fdist:
                                # self.manager.save(self, term)
                queryfile = open('queryfile.txt', 'r')
                queryArray = queryfile.read().splitlines()
                print(queryArray)

        def displayResults(self):
                print("display Results Method!")


controller = Controller()
controller.main()
