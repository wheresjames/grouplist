#!/usr/bin/env python3

import grplist as gl
import numpy as np

try:
    import sparen
    Log = sparen.log
except Exception as e:
    Log = print

def showBreak():
    print('\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')

def test_1():

    showBreak()

    tests = [
        [1, 6, 3],
        [10, 20, 30, 40, 50],
        [1, 3, 6, 10, 12, 14, 21, 35],
        [1, 3, 6, 10, 12, 14, 21, 35, 7, 23],
        [1, 10, 20, 5, 15, 3, 7],
        [1, 10, 20, 30, 40, 35, 32, 5, 11, 2, 3, 16, 17, 12, 33, 34, 35, 33, 3, 42],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    for t in tests:

        def cmpVal(a, b):
            test_1.c += 1
            return 3 >= abs(a-b)

        test_1.c = 0
        m = gl.groupList(t, cmpVal, True)
        Log(test_1.c, " : ", t, " -> ", m)

        test_1.c = 0
        m = gl.groupList2(t, cmpVal, True)
        Log(test_1.c, " : ", t, " -> ", m)

def test_2():

    showBreak()
    a = {'k0': 1, 'k1': 3, 'k2': 6, 'k3': 10, 'k4': 12, 'k5': 14, 'k6': 21, 'k7': 35, 'k8': 7, 'k9': 23}

    m = gl.groupDict(a, lambda a, b: 3 >= abs(a-b), False)
    Log(a, " -> ", m) # [['k0', 'k1', 'k2', 'k3', 'k4', 'k5', 'k8'], ['k6', 'k9'], ['k7']]

    m = gl.groupDict(a, lambda a, b: 3 >= abs(a-b), True)
    Log(a, " -> ", m) # [['k0', 'k1', 'k2'], ['k3', 'k4', 'k5', 'k8'], ['k6', 'k9'], ['k7']]


# Group letters
def test_3():

    showBreak()

    def anyLetters(a, b):
        for l in a:
            if 0 <= b.find(l):
                return True
        return False

    t = ['on', 'tw', 'th', 'fo', 'fi', 'si', 'te', 'zk']
    Log(t, " -> ", gl.groupList2(t, anyLetters, True))


# Group factors
def test_4():

    showBreak()

    t = [3, 4, 5, 6, 7, 8, 9, 10]
    Log(t, " -> ", gl.groupList2(t, lambda a, b: not (a % b), True))


# Group overlapping tracks
def test_5():

    showBreak()

    def showTracks(t, bs, es):
        n = 0
        print(' : 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8')
        for i in t:
            s = (' ' * i[bs]) + ('-' * (i[es] - i[bs] + 1))
            s = '|'.join(s.replace('-', '|', 1).rsplit('-', 1))
            print("%s: %s" % (n, s))
            n += 1

    t = [
        {'beg': 2,  'end': 10},
        {'beg': 20, 'end': 25},
        {'beg': 4,  'end': 7},
        {'beg': 30, 'end': 35},
        {'beg': 8,  'end': 17},
        {'beg': 22, 'end': 28},
        {'beg': 33, 'end': 45},
        {'beg': 1,  'end': 4},
        # {'beg': 0,  'end': 74},
    ]

    print("\n--- INPUT ---")
    showTracks(t, 'beg', 'end')

    g = gl.groupList2(t, lambda a, b: a['beg'] <= b['end'] and a['end'] >= b['beg'], True)

    i = 0
    for t in g:
        i += 1
        print("\n--- GROUP %s ---" % i)
        showTracks(t, 'beg', 'end')


def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()


if __name__ == '__main__':
    main()
