#!venv/bin/python
from pathlib import Path
from dbmanager import DBManager
from htmlparser import HTMLParser
from normalizer import Normalizer
from tabulate import tabulate
from random import randint
from collections import OrderedDict


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
                            relation = {'doc': i.name,
                                        'term': term}
                            self.manager.saveRelation(
                                relation, normalized[term])
        self.manager.updateIDF()

    def computeTable(self, queryArray, table, method):
        p = Path(self.directory)
        table['Files'] = p.iterdir()
        count = 1
        for query in queryArray:
            index = 'Q' + str(count)
            normalized = self.normalizer.normalize(query)
            array = []
            for file in p.iterdir():
                # Llamar a método de Producto escalar
                array.append(randint(0, 9))  # PETF.sim(file.name, normalized))
            table[index] = array
            count = count + 1
        return table

    def displayResults(self):
        queryfile = open('queryfile.txt', 'r')
        queryArray = queryfile.read().splitlines()
        table = OrderedDict()

        print("RELEVANCIA: ProductoEscalarTF")
        table = self.computeTable(queryArray, table, 1)
        print(tabulate(table, headers="keys"))
        print()

        print("RELEVANCIA: ProductoEscalarTFIDF")
        table = self.computeTable(queryArray, table, 2)
        print(tabulate(table, headers="keys"))
        print()

        print("RELEVANCIA: CosenoTF")
        table = self.computeTable(queryArray, table, 3)
        print(tabulate(table, headers="keys"))
        print()

        print("RELEVANCIA: CosenoTFIDF")
        table = self.computeTable(queryArray, table, 4)
        print(tabulate(table, headers="keys"))


controller = Controller()
controller.main()
