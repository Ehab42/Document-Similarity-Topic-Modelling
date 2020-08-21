from doc_to_syns import doc_to_synsets


def similarity_score(s1, s2):
    """
    Calculate the normalized similarity score of s1 onto s2

    For each synset in s1, finds the synset in s2 with the largest similarity value.
    Sum of all of the largest similarity values and normalize this value by dividing it by the
    number of largest similarity values found.

    Args:
        s1, s2: list of synsets from doc_to_synsets

    Returns:
        normalized similarity score of s1 onto s2

    Example:
        synsets1 = doc_to_synsets('I like cats')
        synsets2 = doc_to_synsets('I like dogs')
        similarity_score(synsets1, synsets2)
        Out: 0.73333333333333339
    """
    # Your Code Here

    # Get the largest similarity values
    largest_similarity_values = []

    num_of_scores = 0

    for s in s1:
        # Get similarity values between each synset in s1 with all synsets in s2
        similarity_values = [s.path_similarity(synset) for synset in s2]

        # Remove None values
        similarity_values = [s for s in similarity_values if s]
        num_of_scores += len(similarity_values)
        if len(similarity_values):
            largest_similarity_values.append(max(similarity_values))

    similarity_score = sum(largest_similarity_values) / \
        len(largest_similarity_values)
    return similarity_score
