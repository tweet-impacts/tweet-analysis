# -*- coding: utf-8 -*-
import codecs
import operator

__lower_map = {
    ord(u'I'): u'ı',
    ord(u'İ'): u'i',
    ord(u'Ü'): u'ü',
    ord(u'Ç'): u'ç',
    ord(u'Ş'): u'ş',
    ord(u'Ğ'): u'ğ',
    ord(u'Ö'): u'ö',
}

__lower_cheat_map = {
    ord(u'I'): u'i',
    ord(u'İ'): u'i',
    ord(u'Ü'): u'u',
    ord(u'Ç'): u'c',
    ord(u'Ş'): u's',
    ord(u'Ğ'): u'g',
    ord(u'Ö'): u'o',
    ord(u'ı'): u'i',
    ord(u'ü'): u'u',
    ord(u'ç'): u'c',
    ord(u'ş'): u's',
    ord(u'ğ'): u'g',
    ord(u'ö'): u'o',
}


def lower(word):
    """
    Lowers the word (as well as Turkish characters)
    :param word: that will be lowered
    :return: lowered version of word
    """
    try:
        word = word.decode('utf-8').translate(__lower_cheat_map)
    except UnicodeEncodeError:
        word = word.translate(__lower_cheat_map)
    word = word.lower()
    return word


def lower_line(line):
    return " ".join([lower(word) for word in line.split(" ")])


def create_dictionary_file(path, dictionary, sorted_by_value=False, sorted_list_of_tuples=False):
    with codecs.open(path, mode='w', encoding='utf-8') as _result_file:
        if sorted_list_of_tuples:
            for item in dictionary:
                _result_file.write("%s %d\n" % (item[0], item[1]))
                _result_file.flush()
        elif sorted_by_value:
            sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
            for item in sorted_dictionary:
                _result_file.write("%s %d\n" % (item[0], item[1]))
                _result_file.flush()
        else:
            for key in dictionary:
                value = dictionary[key]
                _result_file.write("%s %d\n" % (key, value))
                _result_file.flush()
        _result_file.flush()
