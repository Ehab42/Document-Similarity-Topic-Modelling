import main as m


def doc_to_synsets(doc):
    """
    Returns a list of synsets in document.

    Tokenizes and tags the words in the document doc.
    Then finds the first synset for each word/tag combination.
    If a synset is not found for that combination it is skipped.

    Args:
        doc: string to be converted

    Returns:
        list of synsets

    Example:
        doc_to_synsets('Fish are nvqjp friends.')
        Out: [Synset('fish.n.01'), Synset('be.v.01'), Synset('friend.n.01')]
    """

    # First: tokenize the document
    tokens = m.nltk.word_tokenize(doc)

    # Second: Part of speech tag the document
    tags = m.nltk.pos_tag(tokens)
    tags_converted = [m.convert_tag(tag[1]) for tag in tags]

    # Combine both tokens and tags
    token_tags_combination = zip(tokens, tags_converted)
    # Skip tokens with unknown tags
    token_tags_combination = [(w, t) for (w, t) in token_tags_combination if t]

    # Then finds the first synset for each word/tag combination
    synsets = []
    for (token, tag) in token_tags_combination:
        try:
            synset = m.wn.synset('{}.{}.01'.format(token, tag))
        except:
            pass
        else:
            synsets.append(synset)

    return synsets


doc1 = 'Use this function to see if your code in doc_to_synsets \
    and similarity_score is correct!'
print(doc_to_synsets(doc1))
