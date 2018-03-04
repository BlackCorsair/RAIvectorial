import nltk
from nltk.tokenize import word_tokenize
from pathlib import Path
from dbmanager import DBManager
import sys

nltk.download('punkt')


class Controller:
        directory = ""

        def __init__(self):
                print("Controller init")
                self.directory = "docrepository"
                manager = DBManager()
                manager.sayHello("fer")

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
                print("Start of Controller setup method...")
                print("Found the following files:")
                p = Path(self.directory)
                for i in p.glob('*.*'):
                        print(i.name)
                text = """Mis viejas preguntas no son nada
                 comparadas con una buena preguntas"""
                print(word_tokenize(text))

        def displayResults(self):
                print("display Results Method!")


controller = Controller()
controller.main()
