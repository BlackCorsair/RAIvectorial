class DBManager:
    def __init__(self):
        print("DBManager: Set up Database")

    '''
        Name: saveTerm
        Input: term (string)
        Ouput: if correct execution returns '1',
               if error returns '-1'
        Function: saves the term given
    '''

    def saveTerm(self, term):
        print("DBManager: asked me to save:", term)

    '''
        Name: saveDoc
        Input: doc (string)
        Ouput: if correct execution returns '1',
               if error returns '-1'
        Function: saves the doc given
    '''

    def saveDoc(self, doc):
        print("DBManager: asked me to save:", doc)

    '''
        Name: saveRelation
        Input: relation, where relation is a dict 'document:term'
        Ouput: if correct execution returns '1',
               if error returns '-1'
        Function: saves the relation given
    '''

    def saveRelation(self, relation):
        print("DBManager: asked me to save:", relation)

    '''
        Name: getIDF
        Input: term (string)
        Output: float value, if error returns '-1'
        Function: given a term, 'getIDF' will search in
                 the DB the term and return the IDF
    '''

    def getIDF(self, term):
        print("TF from " + str(term) + " is --IDF--")

    '''
        Name: getTF
        Input: relation, where relation is a dict 'document:term'
        Output: float value, if error returns '-1'
        Function: given a relation, 'getTF' will search in
                 the DB the relation and return the TF
    '''

    def getTF(self, relation):
        print("TF from " + str(relation) + " is --TF--")

    '''
        Name: getTerm
        Input: term
        Output: term dict, if error returns 'error':'-1'
        Function: given a term, 'getTerm' will return all
                 the information of the term
    '''

    def getTerm(self, term):
        print("Term data of " + str(term))
