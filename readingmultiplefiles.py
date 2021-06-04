import os
from readingabook import word_stats, read_book
from wordcount import count_words
import pandas as pd
import matplotlib.pyplot as plt


book_dir = "./Books"
stats = pd.DataFrame(columns=("language", "author", "title", "length", "unique"))
# os.listdir(book_dir)  # This will print what the var folder contains. In this case, "English,French..."
title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            # print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
            title_num += 1

print(stats[stats.language == "French"])

# stats.head() -> gives us the first 5 lines of the table
# stats.tail() -> gives us the last 5 lines of the table
# To access data from the panda dataframe we use varname.columnname
# plt.plot(stats.length, stats.unique, "bo")
# # plt.show()
#
# plt.figure(figsize=(10, 10))
# subset = stats[stats.language == "English"]
# plt.loglog(subset.length, subset.unique, "o", label="English", color="crimson")
#
# subset = stats[stats.language == "French"]
# plt.loglog(subset.length, subset.unique, "o", label="French", color="forestgreen")
#
# subset = stats[stats.language == "German"]
# plt.loglog(subset.length, subset.unique, "o", label="German", color="orange")
#
# subset = stats[stats.language == "Portuguese"]
# plt.loglog(subset.length, subset.unique, "o", label="Portuguese", color="blueviolet")
#
# plt.legend()
# plt.xlabel("Book Length")
# plt.ylabel("Number of unique words")
# plt.savefig("lang_plot.pdf")
#
