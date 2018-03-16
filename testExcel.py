#!venv/bin/python
from dbmanager import DBManager
import search
from operator import itemgetter

manager = DBManager()

print('Cleaning DB for tests...')
manager.cleanDB()

manager.saveDoc('d1')
manager.saveTerm('rojo')
manager.saveTerm('marca')
manager.saveTerm('citroen')

manager.saveDoc('d2')
manager.saveTerm('coche')
manager.saveTerm('rojo')
manager.saveTerm('blanco')
manager.saveTerm('madrid')
manager.saveTerm('ocasion')

manager.saveDoc('d3')
manager.saveTerm('rojo')
manager.saveTerm('blanco')
manager.saveTerm('marca')
manager.saveTerm('madrid')
manager.saveTerm('ocasion')
manager.saveTerm('auto')

'''
manager.saveTerm('coche')
manager.saveTerm('rojo')
manager.saveTerm('blanca')
manager.saveTerm('marca')
manager.saveTerm('citroen')
manager.saveTerm('blanco')
manager.saveTerm('madrid')
manager.saveTerm('ocasion')
manager.saveTerm('auto')
'''

manager.updateIDF()

print('Saving virtual relations')
manager.saveRelation({'doc': "d1", 'term': "marca"}, 1)
manager.saveRelation({'doc': "d1", 'term': "citroen"}, 1)
manager.saveRelation({'doc': "d1", 'term': "rojo"}, 1)

manager.saveRelation({'doc': "d2", 'term': "coche"}, 2)
manager.saveRelation({'doc': "d2", 'term': "rojo"}, 1)
manager.saveRelation({'doc': "d2", 'term': "blanco"}, 1)
manager.saveRelation({'doc': "d2", 'term': "madrid"}, 1)
manager.saveRelation({'doc': "d2", 'term': "ocasion"}, 1)

manager.saveRelation({'doc': "d3", 'term': "blanco"}, 1)
manager.saveRelation({'doc': "d3", 'term': "marca"}, 1)
manager.saveRelation({'doc': "d3", 'term': "rojo"}, 1)
manager.saveRelation({'doc': "d3", 'term': "madrid"}, 1)
manager.saveRelation({'doc': "d3", 'term': "ocasion"}, 1)
manager.saveRelation({'doc': "d3", 'term': "auto"}, 1)

query = {'coche', 'rojo', 'blanco'}

print("calculating query!")

print("\n\n____________________________\n\n")
print("calc")
result = sorted(search.calc(query, manager.docs, manager.relations,
                            manager.terms), key=itemgetter('doc'))
for r in result:
    print(r)

print("\n\n____________________________\n\n")
print("IDF")
for t in manager.terms.find():
    print(t)

print("\n\n____________________________\n\n")
print("TF")
for t in manager.relations.find():
    print(t)
print("\n\n____________________________\n\n")
print("DOCS")
for t in manager.docs.find():
    print(t)
