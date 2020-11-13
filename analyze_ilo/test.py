# -*- coding: utf-8 -*-

def test1():
    for i in range(0,10):
        yield (i)
        for j in range(11,20):
            yield (j)

all = test1()
while True:

    info = all.next()
    print(info)