# -*- coding: utf-8 -*-
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
