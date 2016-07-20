# social-graph

## Asumptions
**Total lookups are from the root**</br>
Because it said so in the instructions. No visited protection based on this, nor are parent
nodes visited.

**Nodes are listed in CSV in order of dependency**</br>
No support for broken graphs.. No error handling at all.

## Run

Test on ```python 2.7.6```

Program accepts a postId from ```stdin``` and prints out the id followed by the follower total.

**tests**
```
$ python test.py
```

**program**
```
$ python main.py
```
