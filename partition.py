# -*- coding: utf-8 -*-
import codecs


def partition_file(input_path, output_path, line_size):
    print "Partition is started!"
    _file = codecs.open(input_path, encoding='utf-8')
    count = 0
    o = None
    for line in _file:
        if count % line_size == 0:  # new file
            if o:
                o.close()
                print "%s is done!" % str(count/line_size-1)
            filename = output_path + 'file_%s.txt' % str(count / line_size)
            o = codecs.open(filename, mode='w', encoding='utf-8')
            o.write(line)
        else:
            if o:
                o.write(line)
        o.flush()
        count += 1
    o.close()
    print "Partition is done!"


if __name__ == '__main__':
    _input = 'unshared_data/all_small_tweets_filtered.txt'
    _output = 'unshared_data/'
    partition_file(_input, _output, 1000000)
