import pandas as pd
import numpy as np
from document_path_similarity import document_path_similarity

paraphrases = pd.read_csv('paraphrases.csv')
paraphrases.head()


def most_similar_docs():

    # Your Code Here

    # Store D1 & D2 pairs with their document_path_similarity correspondaly
    d1_d2_pairs = []
    path_similarities = []
    for row in paraphrases.iterrows():
        d1_d2_pairs.append((row[1]['D1'], row[1]['D2']))
        path_similarities.append(
            document_path_similarity(row[1]['D1'], row[1]['D2']))

    # Get the index of the largest document_path_similarity
    ind = path_similarities.index(max(path_similarities))
    max_d1_d2_pair = d1_d2_pairs[ind]

    return max_d1_d2_pair[0], max_d1_d2_pair[1], path_similarities[ind]


# print(most_similar_docs())


def label_accuracy():
    from sklearn.metrics import accuracy_score

    # Your Code Here
    label = []

    for row in paraphrases.iterrows():
        similar_val = document_path_similarity(row[1]['D1'], row[1]['D2'])
        label.append(1 if similar_val > 0.75 else 0)

    return accuracy_score(paraphrases['Quality'], label)


print(label_accuracy())
