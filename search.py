#!venv/bin/python
from math import sqrt
'''
    Name:
    Input:
    Output:
    Function:
'''

'''
    Name: calcTF
    Input: query, which is an array of the words from the query
           relation, which is a DBManager object which can access
            the collection relations from the DB
           docs, which is a DBManager object which can access
            the collection documents from the DB
    Output: TF scalar product (float)
    Function: the function run the following calculation
             (sim(dj,q) = dj * q = Σ Wij * Wiq),
             getting the TF values for earch term in the given
             query from the database.
'''


def calcTF(query, relations, docs):
    tf_total = []
    query_cos_div = sqrt(len(query))
    for doc in docs:
        tf_sum = 0
        tf_cos_sum = 0
        terms = list(relations.find({'doc': doc}))
        for term in terms:
            if term['term'] in query:
                tf_sum = tf_sum + int(term['tf'])
                tf_cos_sum = tf_cos_sum + int(term['tf']) ** 2
        tf_cos_div = sqrt(tf_cos_sum)
        cosTF = tf_sum / (tf_cos_div * query_cos_div)

        tf_total.append({'doc': doc, 'cosTF': cosTF})
    return tf_total
