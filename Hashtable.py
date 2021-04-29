from typing import Generic, List, Optional, TypeVar
from LList import LList

T = TypeVar('T')

class Hashtable(Generic[T]):
    """Class to implement a hashtable, using a Python list.  Hash collisions are handled with
    hash chaining."""

    # --------------------- Helper functions -----------------------------------------------

    def _hashFn(self, value:T) -> int:
        """Hash function, based on the string representation of the given VALUE."""
        valStr:str = repr(value)
        hashresult:int = 0
        for c in valStr:
            hashresult = ord(c)
        return hashresult % len(self._table)

    def _invariant(self) -> bool:
        """Class invariant.  Basically requires that every item is on the correct hash chain."""
        correctlyHashed:bool = True
        for i in range(len(self._table)): # type: int
            if not correctlyHashed:
                continue
            chain:LList[T] = self._table[i]
            while correctlyHashed and not chain.isEmpty():
                correctlyHashed = (self._hashFn(chain._data) == i)  # type: ignore
                chain = chain._next                                 # type: ignore
        return correctlyHashed

    # ----------------------- Constructor -----------------------------------------------------

    def __init__(self, initialSize:int = 31) -> None:
        self._table:List[LList[T]] = [LList[T]() for i in range(initialSize)]
        # Post
        assert self._invariant()

    # ----------------------- Query methods ---------------------------------------------------

    def __contains__(self, key:T) -> bool:
        hashval:int = self._hashFn(key)
        return self._table[hashval].search(key)

    def get(self, key:T) -> Optional[T]:
        """Returns the value associated with KEY.  In fact, this is cheating a bit, since in this
        implementation the keys *are* their values.  If KEY is not in the table, return None."""
        result:Optional[T] = None
        hashval:int = self._hashFn(key)
        if self._table[hashval].search(key):
            result = key
        return result

    # ------------------------ Mutator methods ------------------------------------------------

    def put(self, value:T) -> None:
        hashval:int = self._hashFn(value)
        if not self._table[hashval].search(value): # Only add the value once
            self._table[hashval].add(value)
        # Post
        assert self._invariant()
