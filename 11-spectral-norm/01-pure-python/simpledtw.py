"""
simpledtw is a Python Dynamic Programming implementation using NumPy, of the classic Dynamic Time Warping algorithm.
https://github.com/talcs/simpledtw
"""
import numpy as np


def dtw(series_1, series_2, norm_func=np.linalg.norm):
    """
    dynamic time warping
    The library enables computing DTW on sequences of scalars or on sequences of vectors.
    :param series_1: an iterable object of numbers or vectors
    :param series_2: an iterable object of numbers or vectors
    :param norm_func: Optional. a function that computes vector norm or real number absolute value
    (default is numpy.linalg.norm)

    :return matches: a list of tuples, where each tuple's first member
     is an index from series_1 and the second member is an index from series_2
    :return cost: the cost of the warping, which is the value at the (n,m) cell of the Dynamic Programming 2D array
    :return mapping_1: 	a list that contains at each index i,
    the list of indices j in series_2, to which index i in series_1 has been matched
    :return mapping_2: 	a list that contains at each index i,
    the list of indices j in series_1, to which index i in series_2 has been matched
    :return matrix: the Dynamic Programming (nxm) Numpy matrix,
    where n is the length of series_1 and m is the length of series_2,
    which can be used in order to visualize the computations and the selected path
    """
    matrix = np.zeros((len(series_1) + 1, len(series_2) + 1))
    matrix[0, :] = np.inf
    matrix[:, 0] = np.inf
    matrix[0, 0] = 0
    for i, vec1 in enumerate(series_1):
        for j, vec2 in enumerate(series_2):
            cost = norm_func(vec1 - vec2)
            matrix[i + 1, j + 1] = cost + min(matrix[i, j + 1], matrix[i + 1, j], matrix[i, j])
    matrix = matrix[1:, 1:]
    i = matrix.shape[0] - 1
    j = matrix.shape[1] - 1
    matches = []
    mappings_series_1 = [list() for v in range(matrix.shape[0])]
    mappings_series_2 = [list() for v in range(matrix.shape[1])]
    while i > 0 or j > 0:
        matches.append((i, j))
        mappings_series_1[i].append(j)
        mappings_series_2[j].append(i)
        option_diag = matrix[i - 1, j - 1] if i > 0 and j > 0 else np.inf
        option_up = matrix[i - 1, j] if i > 0 else np.inf
        option_left = matrix[i, j - 1] if j > 0 else np.inf
        move = np.argmin([option_diag, option_up, option_left])
        if move == 0:
            i -= 1
            j -= 1
        elif move == 1:
            i -= 1
        else:
            j -= 1
    matches.append((0, 0))
    mappings_series_1[0].append(0)
    mappings_series_2[0].append(0)
    matches.reverse()
    for mp in mappings_series_1:
        mp.reverse()
    for mp in mappings_series_2:
        mp.reverse()

    return matches, matrix[-1, -1], mappings_series_1, mappings_series_2, matrix
