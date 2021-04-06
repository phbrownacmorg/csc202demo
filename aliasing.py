from typing import List
from copy import copy, deepcopy

def check_same(obj1:object, obj2:object) -> None:
    print(id(obj1), id(obj2))

    print(str(obj1), 'and', str(obj2), 'are', end=' ')
    if not obj1 == obj2:
        print('NOT', end=' ')
    print('equal using ==.')

    print(str(obj1), 'and', str(obj2), 'are', end=' ')
    if not obj1 is obj2:
        print('NOT', end=' ')
    print('the same object (aliases).')

def two_copies() -> None:
    '''Illustrate the difference between shallow and deep copies.'''
    a:List[List[int]] = [[1], [2], [3]]
    b:List[List[int]] = a[:]       # Shallow copy: a[0] == b[0] and a[0] is b[0]
    check_same(a[0], b[0])

    c:List[List[int]] = a.copy()   # Shallow copy: a[0] == c[0] and a[0] is c[0]
    check_same(a[0], c[0])

    d:List[List[int]] = copy(a)    # Shallow copy: a[0] == d[0] and a[0] is d[0]
    check_same(a[0], d[0])

    e:List[List[int]] = deepcopy(a) # Deep copy: a[0] == e[0] and a[0] is e[0]
    check_same(a[0], e[0])

def aliasing_demo() -> None:
    a:List[List[int]] = [[1, 2], [3, 4], [5]]
    print('a =', a)
    b = a   # Aliased!
    print('b =', b)
    print('a is b is', (a is b))

    c = a[:]  # Shallow copy: contents are aliased
    print('c =', c)
    print('a is c is', (a is c))  # Not aliased
    print('a[0] is c[0] is', (a[0] is c[0])) # Aliased

    d = deepcopy(a)
    print('d =', d)
    print('a is d is', (a is d))  # Not aliased
    print('a[0] is d[0] is', (a[0] is d[0])) # Not aliased


    c[2].append(6)
    print('c =', c)  # OK
    print('b =', b)  # This changed too!  How did that happen?
    # Note that b and c never occur together in a statement!
    print('d =', d)  # No change because of the deep copy


def main(args:List[str]) -> int:
    two_copies()
    aliasing_demo()
    return 0


if __name__ == '__main__':
    import sys
    main(sys.argv)