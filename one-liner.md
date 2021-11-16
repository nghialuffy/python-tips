## One-Liners

### Simple Web Server

```shell
# Python 3
python -m http.server 8000
```

### Pretty Printing

```python
from pprint import pprint

pprint({'a': 1, 'b': [2, 3]})
```

Or

```shell
cat file.json | python -m json.tool
```
### Profiling a script

```shell
python -m cProfile my_script.py
```

### CSV to json

```shell
python3 -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"
```

### List Flattening

```python
from itertools import chain


def flatten(l):
    return list(chain.from_iterable(l))

flatten([[1, 2], [3, 4]])
```

### One-liner Constructors

```python
class A(object):
    def __init__(self, a, b, c, d, e, f):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})
```
