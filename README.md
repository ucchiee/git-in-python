# git-in-python

PoC of Git in Python

Tested on Python 3.9.5

## how to test

```bash
python -m unittest discover tests
```

## measure test coverage

```
coverage run -m unittest discover tests
coverage report -m
```

## code size

```
--------------------------------------
Language  files  blank  comment   code
--------------------------------------
Python       30    223       43    775
Markdown      2     24        0     69
YAML          1      5        4     27
C             2      1        0      8
make          1      0        0      3
--------------------------------------
SUM:        181    253       47   1027
--------------------------------------
```

test:
```
-------------------------------------
Language  files  blank  comment  code
-------------------------------------
Python        6     78       13   240
C             1      1        0     5
-------------------------------------
SUM:          7     79       13   245
-------------------------------------
```

## todo

Commands to implement:

- [x] init
- [x] hash-object
- [x] cat-file
- [x] add
- [x] ls-files
- [x] write-tree
- [x] commit
