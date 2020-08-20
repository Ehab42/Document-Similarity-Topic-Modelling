import numpy as np
import nltk
from nltk.corpus import wordnet as wn
import pandas as pd


def convert_tag(tag):
    """Convert the tag given by nltk.pos_tag to the tag used by wordnet.synsets"""

    tag_dict = {'N': 'n', 'J': 'a', 'R': 'r', 'V': 'v'}
    try:
        return tag_dict[tag[0]]
    except KeyError:
        return None


# def document_path_similarity(doc1, doc2):
#     """Finds the symmetrical similarity between doc1 and doc2"""

#     synsets1 = doc_to_synsets(doc1)
#     synsets2 = doc_to_synsets(doc2)

#     return (similarity_score(synsets1, synsets2) + similarity_score(synsets2, synsets1)) / 2


# # test_document_path_similarity
# def test_document_path_similarity():
#     doc1 = 'This is a function to test document_path_similarity.'
#     doc2 = 'Use this function to see if your code in doc_to_synsets \
#     and similarity_score is correct!'
#     return document_path_similarity(doc1, doc2)
