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
            cosTF_IDF = 0
        tf_total.append({'doc': doc['name'], 'cosTF': cosTF,
                         'scalarTF': scalarTF, 'cosTF_IDF': cosTF_IDF,
                         'scalarTF_IDF': scalarTF_IDF})
    return tf_total


def calc(query, docs, relations, terms):
    calcs = []
    qdivCosTF = sqrt(len(query))
    qdivCos = calcQueryCosDiv(query, terms)
    for doc in docs.find():
        # variable initialization
        scalarTF_IDF = 0
        scalarTF = 0
        divCosTF = 0
        divCosTF_DF = 0
        # middlecalc
        values = calcScalarDivCos(
            query, doc['name'], relations, terms)
        scalarTF_IDF = values[0]
        scalarTF = values[1]
        divCosTF = values[2]
        divCosTF_DF = values[3]
        # final calculations
        try:
            cosTF = scalarTF / (sqrt(divCosTF) / qdivCosTF)
            cosTF_IDF = scalarTF_IDF / (sqrt(divCosTF_DF) * sqrt(qdivCos))
        except ZeroDivisionError:
            cosTF = 0
            cosTF_IDF = 0
        # return the calculations
        calcs.append({'doc': doc['name'], 'cosTF': cosTF,
                      'scalarTF': scalarTF, 'cosTF_IDF': cosTF_IDF,
                      'scalarTF_IDF': scalarTF_IDF})
    return calcs


def calcScalarDivCos(query, doc, relations, terms):
    # all relations where appears doc
    rel = list(relations.find({'doc': doc}))
    # variable initialization
    scalarTF = 0
    scalarTF_IDF = 0
    divCosTF = 0
    divCosTF_DF = 0

    # this equals to term_tf * q
    for r in rel:
        # cosTF
        tf = r['tf']
        divCosTF = divCosTF + tf ** 2
        divCosTF_DF = divCosTF_DF + \
            (terms.find_one({'term': r['term']})['idf'] * tf) ** 2
        print('divCosTF ' + str(divCosTF))

        print('divCosTF_DF ' + str(divCosTF_DF))

        if r['term'] in query:
            print("match: " + r['term'])
            # cosTF
            scalarTF = scalarTF + tf
            # cosTF_IDF
            idf = terms.find_one({'term': r['term']})['idf']
            # idf ** 2 = weight (idf * tf) * query_idf
            weight = idf * tf
            scalarTF_IDF = scalarTF_IDF + weight * idf

            print('weight ' + str(weight))
            print('idf ' + str(idf))
            print('tf ' + str(tf))
            print('scalarTF: ' + str(scalarTF))
            print('scalarTF_IDF ' + str(scalarTF_IDF))
    print("Calc values for " + doc)
    print(scalarTF)
    print(divCosTF)
    print(scalarTF_IDF)
    print(divCosTF_DF)
    return [scalarTF, divCosTF, scalarTF_IDF, divCosTF_DF]


def calcQueryCosDiv(query, terms):
    query_cos_div_tf_df = 0
    for q in query:
        try:
            idf = terms.find_one({'term': q})['idf']
        except Exception as e:
            idf = 0
        query_cos_div_tf_df = query_cos_div_tf_df + idf ** 2
    return query_cos_div_tf_df
