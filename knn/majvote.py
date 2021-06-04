from knn import distance
import numpy as np
import random
import scipy.stats as ss


def majority_vote(votes):
    """
    :param text: the string that you are going to use
    :return: Return dictionary where keys are unique words and values many time they appear
    """
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
    return random.choice(winners)


def majority_vote_mode(votes):
    """
    :param votes: Array
    :return: mode of the array
    """
    mode, count = ss.mstats.mode(votes)
    return mode



# votes = [1, 2, 2, 2, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 3, 3]
#
# winner = majority_vote(votes)
# print(winner)
# print(majority_vote_mode(votes))
