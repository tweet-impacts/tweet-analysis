import numpy as np
import codecs
import util
import matplotlib.pyplot as plt
import math


def normal_distribution_analysis(sorted_dictionary, path, std_far=3):
    data = [item[1] for item in sorted_dictionary]
    mean, std = np.mean(data), np.std(data)
    threshold = mean + std_far * std
    new_dictionary = []
    for item in sorted_dictionary:
        if item[1] >= threshold:
            new_dictionary.append((item[0], item[1]))
    util.create_dictionary_file(path, new_dictionary, sorted_list_of_tuples=True)


def weed_outliers_out_analysis(sorted_dictionary, trim_percentage, std_far=3):
    leng = len(sorted_dictionary)
    trim_size = int(leng * trim_percentage / 100)
    trimmed_sorted_dictionary = sorted_dictionary[trim_size:leng - trim_size]
    normal_distribution_analysis(trimmed_sorted_dictionary,
                                 'data/dictionary-normal-distributed-analysis-trimmed.txt', std_far)


def choose_most_common_words(sorted_dictionary):
    normal_distribution_analysis(sorted_dictionary, 'data/dictionary-normal-distributed-analysis.txt', 2)
    weed_outliers_out_analysis(sorted_dictionary, 1, std_far=2)


def extract_data_with_threshold(sorted_dictionary, lower, upper):
    with open('data/dictionary_count_values_%d_%d.txt' % (upper, lower), 'w') as file:
        for item in sorted_dictionary:
            count = item[1]
            if lower <= count <= upper:
                file.write(str(count))
                file.write('\n')
        file.flush()


def statistics_of_words(sorted_dictionary):
    data = [item[1] for item in sorted_dictionary]
    _max, _min, count = max(data), min(data), sum(data)
    return _max, _min, count


def get_most_common_word_counts(sorted_dictionary, how_many=100):
    data = [item[1] for item in sorted_dictionary]
    return data[how_many]


if __name__ == '__main__':
    _sorted_dictionary = []
    with codecs.open('data/dictionary-sorted.txt', encoding='utf-8') as _file:
        for _line in _file:
            _line = _line.strip().split(" ")
            _word, _count = _line[0], int(_line[1])
            _sorted_dictionary.append((_word, _count))

    max_count, min_count, word_count = statistics_of_words(_sorted_dictionary)
    lower_limit = word_count / 100000
    upper_limit = get_most_common_word_counts(_sorted_dictionary, 100)
    upper_limit = 21847

    _func = 3
    if _func == 1:
        choose_most_common_words(_sorted_dictionary)
    elif _func == 2:
        extract_data_with_threshold(_sorted_dictionary, lower_limit, upper_limit)
