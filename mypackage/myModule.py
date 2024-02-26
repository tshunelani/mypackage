def top_n(items, n):
    """Return the top n items in an array, in descending order.

    Args:
        Items (array): list or array-like object
        n (int): number of items to return

    Return:
        array: top n items, in desc order

    Egs:
        >>> top_n([8,3,2,7,4], 3)
        [8,7,4]
    """

    for i in range(n):  # keep sorting until we have the top n items
        for j in range(len(items) - 1 - i):

            if items[j] > items[j + 1]:  # if this is bigger than next item ..
                items[j], items[j + 1] = items[j + 1], items[j]  # swap the two!

    # ge the last two items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]
