# coding: utf-8
from itertools import groupby
from collections import Counter


def scatters(source):
    source_items = ''.join(sorted(source))
    list_ = [''.join(i.split()) for i in source_items]
    result = []

    def redex(list_):
        scatter = [i[0] for i in groupby(list_)]
        if len(scatter) > 1:
            result.extend(scatter)
        c1 = Counter(list_)
        c2 = Counter(scatter)
        diff = c1 - c2
        intersection = list(diff.elements())
        if (len(set(intersection)) == 1) or not intersection:
            result.extend(intersection)
            return result
        else:
            return redex(intersection)

    redex(list_)
    return result


if __name__ == "__main__":
    print(scatters('CBBCCCB'))   # ===> ['B', 'C', 'C', 'B', 'C', 'B', 'C']