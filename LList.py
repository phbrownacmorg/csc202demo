from typing import Generic, Optional, TypeVar
T = TypeVar('T')

class LList(Generic[T]):

    def _invariant(self) -> bool:
        """Class invariant: if _next points to None, _data must also be None."""
        return (self._next is not None) or (self._next is None and self._data is None)

    def __init__(self) -> None:
        """Create an empty list (sentinel node)."""
        self._data:Optional[T] = None
        self._next:Optional[LList] = None
        assert self._invariant()

    # -------------------- QUERY METHODS ---------------------------------------------

    def isEmpty(self) -> bool:
        # Pre:
        assert self._invariant()
        return self._next is None and self._data is None

    def size(self) -> int:
        """Return the number of nodes on the list."""
        result:int = 0
        if self.isEmpty():
            result = 0
        else:
            result = 1 + self._next.size()
        return result

    def __len__(self) -> int:
        return self.size()

    def __str__(self) -> str:
        result:str = '∅'
        if not self.isEmpty():
            result = '❬' + str(self._data) + '❭➞' + str(self._next)
        return result

    def search(self, val:T) -> bool:
        result:bool = False
        if not self.isEmpty():
            if self._data == val:
                result = True
            else:
                result = self._next.search(val)
        return result

    # -------------------- MUTATOR METHODS ---------------------------------------

    def add(self, newval:T) -> None:
        # Pre:
        assert self._invariant
        if self.isEmpty():
            # if this is the end of the list, add it here
            self._data = newval
            self._next = LList[T]()
        else:
            # Otherwise, add it to the rest of the list
            self._next.add(newval)
        # Post:
        assert not self.isEmpty()

    def pop(self, pos:int = -1) -> T:
        # Pre:
        assert (not self.isEmpty()) and -1 <= pos < self.size() and self._invariant
        returnval:T
        if pos == -1: # Take the last node on the list
            pos = self.size() - 1
        
        if pos == 0: # This is the node to take
            returnval = self._data
            self._data = self._next._data
            self._next = self._next._next
        else:
            returnval = self._next.pop(pos-1)
        # Post:
        assert self._invariant
        return returnval
    