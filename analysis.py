# -*- coding: utf-8 -*-
from util import lower_line
import util
import codecs


def add_word_to_dictionary(word, dictionary, limit_size=3):
    if len(word) >= limit_size:
        count = dictionary.get(word)
        dictionary[word] = 1 if count is None else 1 + count


def add_line_to_dictionary(line, dictionary):
    line = line.strip()
    line = lower_line(line)
    for word in line.split(" "):
        add_word_to_dictionary(word, dictionary, 3)


def add_file_to_dictionary(file, dictionary):
    with codecs.open(file, encoding='utf-8') as _file:
        for _line in _file:
            add_line_to_dictionary(_line, dictionary)


def weed_dictionary_out(dictionary, lower_frequency=3):
    delete_key = []
    for key in dictionary:
        if dictionary[key] < lower_frequency:
            delete_key.append(key)
    for key in delete_key:
        del dictionary[key]


if __name__ == '__main__':
    _dictionary = {}

    # TODO: change below _files variable for operation on files
    _files = ['unshared_data/file_%d.txt' % i for i in range(23)]

    for i, _file in enumerate(_files):
        add_file_to_dictionary(_file, _dictionary)
        weed_dictionary_out(_dictionary, 3)
        print "file %d is done!" % i
    util.create_dictionary_file("data/dictionary.txt", _dictionary)
    util.create_dictionary_file("data/dictionary-sorted.txt", _dictionary, sorted_by_value=True)
