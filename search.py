#!venv/bin/python
from math import sqrt
from pymongo import DESCENDING
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
    Output: a list of dict {'doc': docname, 'cosTF': value, 'scalarTF': value}
    Function: the function run the following calculation
             (sim(dj,q) = dj * q = Σ Wij * Wiq),
             getting the TF values for earch term in the given
             query from the database.
'''


def calcTF(query, relations, docs):
    tf_total = []
    query_cos_div = sqrt(len(query))
    for doc in docs.find():
        tf_sum = 0
        tf_cos_sum = 0
        terms = list(relations.find(
            {'doc': doc['name']}))
        for term in terms:
            if term['term'] in query:
                tf_sum = tf_sum + int(term['tf'])
                tf_cos_sum = tf_cos_sum + int(term['tf']) ** 2
                print("match: " + term['term'])
        try:
            tf_cos_div = sqrt(tf_cos_sum)
            cosTF = tf_sum / (tf_cos_div * sqrt(query_cos_div))
        except ZeroDivisionError:
            tf_cos_div = 0
            cosTF = 0
        tf_total.append({'doc': doc['name'], 'cosTF': cosTF,
                         'scalarTF': tf_sum})
    return tf_total


'''
    Name: calcAll
    Input: query, which is an array of the words from the query
           relation, which is a DBManager object which can access
            the collection relations from the DB
           docs, which is a DBManager object which can access
            the collection documents from the DB,
           terms, which is a DBManager object which can access
           the collection terms from the DB
    Output: a list of dict {'doc': docname,'cosTF': value,'scalarTF': value,
                            'cosTF_IDF': value, 'scalarTF_IDF': value}
    Function: the function runs all the calculations MUAJAJAJAJAJA
'''


def calcAll(query, relations, docs, terms):
    tf_total = []
    query_cos_div_tf = sqrt(len(query))
    query_cos_div_tf_idf = calcQueryCosDiv(query, terms)
    for doc in docs.find():
        scalarTF = 0
        scalarTF_IDF = 0
        tf_cos_sum = 0
        tf_idf_cos_sum = 0
        query_cos_div = 0
        terminus = list(relations.find({'doc': doc['name']}))
        for term in terminus:
            if term['term'] in query:
                termIDF = terms.find_one({'term': term['term']})['idf']
                scalarTF = scalarTF + int(term['tf'])
                tf_cos_sum = tf_cos_sum + int(term['tf']) ** 2
                weightIDF = int(term['tf']) * termIDF
                tf_idf_cos_sum = tf_idf_cos_sum + weightIDF ** 2
                scalarTF_IDF = scalarTF_IDF + weightIDF * termIDF
                query_cos_div = query_cos_div + termIDF ** 2
        try:
            tf_cos_div = sqrt(tf_cos_sum)
            tf_idf_cos_div = sqrt(tf_idf_cos_sum)
            cosTF = scalarTF / (tf_cos_div * sqrt(query_cos_div_tf))
            cosTF_IDF = scalarTF_IDF / \
                (tf_idf_cos_div / sqrt(query_cos_div_tf_idf))
        except ZeroDivisionError:
            tf_cos_div = 0
            cosTF = 0
        tf_total.append({'doc': doc['name'], 'cosTF': cosTF,
                         'scalarTF': scalarTF, 'cosTF_IDF': cosTF_IDF,
                         'scalarTF_IDF': scalarTF_IDF})
    return tf_total


def calcQueryCosDiv(query, terms):
    query_cos_div_tf_df = 0
    for q in query:
        query_cos_div_tf_df = query_cos_div_tf_df\
            + terms.find_one({'term': q})['idf'] ** 2
    return query_cos_div_tf_df
