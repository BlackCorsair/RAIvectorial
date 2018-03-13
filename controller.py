#!venv/bin/python
from pathlib import Path
from dbmanager import DBManager
from htmlparser import HTMLParser
from normalizer import Normalizer


class Controller:
    directory = ""
    manager = DBManager()
    parser = HTMLParser()
    normalizer = Normalizer()

    def __init__(self):
        print("Controller init")
        self.directory = "docrepository"

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
        for i in p.iterdir():
            print("Working on file:", i.name)
            path = Path.cwd().joinpath(self.directory +
                                       "/" + i.name)
            with path.open('r') as file:
                # Parser
                filetext = self.parser.parse(file)
                # Normalizer
                normalized = self.normalizer.normalize(
                    filetext)
                # Save to DB
                if self.manager.saveDoc(i.name) == 1:
                    for term in normalized:
                        if self.manager.saveTerm(term) == 1:
                            relation = {'doc':i.name, 'term': term}
                            self.manager.saveRelation(relation, normalized[term])
        self.manager.updateIDF()

    def displayResults(self):
        queryfile = open('queryfile.txt', 'r')
        queryArray = queryfile.read().splitlines()
        print("RELEVANCIA: ProductoEscalarTF")
        for query in queryArray:
            print(query)
            normalized = self.normalizer.normalize(query)
            for term in normalized:
                print("Term ", term, " appears ", normalized[term])
        print("RELEVANCIA: ProductoEscalarTFIDF")

        print("RELEVANCIA: CosenoTF")

        print("RELEVANCIA: CosenoTFIDF")

controller = Controller()
controller.main()
