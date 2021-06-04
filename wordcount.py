from collections import Counter


text = "This is my test text. We're keeping this text short to keep things manageable"


def count_words(text):
    """
    Count the number of times each word occurs in text(str).
    lower case all words to avoid double counting, and also define a list of non valid
    characters(skip)
    :param text: the string that you are going to use
    :return: Return dictionary where keys are unique words and values many time they appear
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def fast_counter(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts


# x = count_words(text)
# y = fast_counter(text)
# print(x is y)
#
#
