from wordcount import count_words


def word_stats(word_counts):
    """
    :param word_counts: Function previously defined
    :return: number of unique words and word frequency
    """
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)


def read_book(title_path):
    """
    Read a book and return it as a string
    :param title_path: the path to the book you want to read
    :return: a string containing the book
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

#
# amnsd = read_book("Books\English\shakespeare\Romeo and Juliet.txt")
# es = read_book("Books/German/shakespeare/Romeo und Julia.txt")
# word_counts = count_words(amnsd)
# german_count = count_words(es)
# len(amnsd)
# sample_text = amnsd[450:500]
# print(sample_text)
# (num_unique, counts) = word_stats(word_counts)
# (num_unique2, counts2) = word_stats(german_count)
# print(num_unique, counts)
# print("Sum", sum(counts))
# print(num_unique2, counts2)
# print("Ein Sum", sum(counts2))
