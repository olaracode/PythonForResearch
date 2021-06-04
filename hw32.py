# DO NOT EDIT THIS CODE!
import os
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt



def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })

    data.loc[data["count"] > 10, "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1, "frequency"] = "unique"

    data["length"] = data["word"].apply(len)

    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent", "infrequent", "unique"],
        "mean_word_length": data.groupby(by="frequency")["length"].mean(),
        "num_words": data.groupby(by="frequency").size()
    })

    return (sub_data)

def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts


def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)


d = pd.read_csv("asset-v1_HarvardX+PH526x+2T2019+type@asset+block@hamlets.csv", index_col=[0])
language, text = d.iloc[0]
german, textman = d.iloc[1]
portuguese, textuguese = d.iloc[2]

counted_words = count_words_fast(text)
counted_words2 = count_words_fast(textman)
counted_words3 = count_words_fast(textuguese)

colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")
nu, cu = word
plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")
plt.plot()






# data = pd.DataFrame(columns=("word", "count", "length", "frequency"))
# index_item = 1
# for i in counted_words:
#     x = len(i)
#     if counted_words[i] > 10:
#         freq = "Frequent"
#     elif counted_words[i] == 1:
#         freq = "Unique"
#     else:
#         freq = "Infrequent"
#     data.loc[index_item] = i, counted_words[i], x, freq
#     index_item += 1

# sub_data = pd.DataFrame({"Language": language,
#                          "Frequency": ["Frequent", "Infrequent", "Unique"],
#                          "mean_word_length": data.groupby(by="frequency")[length].mean,
#                          "num_words": data.group(by="Frequency").size()})
#
# print(data[data.frequency == "Unique"])
# print(sub_data)

for i in [0,1,2]:
    language, text = d.iloc[i]
    (summarize_text(language, text))

print()