from typing import Generic, Optional, TypeVar
T = TypeVar('T')

class LList(Generic[T]):

    def _invariant(self) -> bool:
        """Class invariant: if _next points to None, _data must also be None."""
        return (self._next is not None) or (self._next is None and self._data is None) # type: ignore

    def __init__(self) -> None:
        """Create an empty list (sentinel node)."""
        self._data:Optional[T] = None
        self._next:Optional[LList] = None
        assert self._invariant()

    # -------------------- QUERY METHODS ---------------------------------------------

    def isEmpty(self) -> bool:
        # Pre:
        assert self._invariant()
        return self._next is None and self._data is None # type: ignore

    def size(self) -> int:
        """Return the number of nodes on the list."""
        result:int = 0
        if self.isEmpty():
            result = 0
        else:
            result = 1 + self._next.size()  # type: ignore
        return result

    def __len__(self) -> int:
        return self.size()

    def __str__(self) -> str:
        result:str = '∅' # Value if list is empty
        if not self.isEmpty():
            # Representation of current node + representation of the rest of the list
            result = '❬' + str(self._data) + '❭➞' + str(self._next) # type: ignore
        return result

    def search(self, val:T) -> bool:
        result:bool = False # Value if list is empty
        if not self.isEmpty():
            if self._data == val: # Value for current node
                result = True
            else:                 # Value for the rest of the list
                result = self._next.search(val) # type: ignore
        return result

    # -------------------- MUTATOR METHODS ---------------------------------------

    def add(self, newval:T) -> None:
        """Add a new value to the beginning of the LList."""
        # Pre:
        assert self._invariant
        newnode:LList[T] = LList[T]()
        newnode._data = self._data
        newnode._next = self._next
        self._data = newval
        self._next = newnode
        # Post:
        assert not self.isEmpty()

    def pop(self, pos:int = -1) -> T:
        """Remove the value at the given position POS.  POS defaults to the end of the list."""
        # Pre:
        assert (not self.isEmpty()) and -1 <= pos < self.size() and self._invariant
        returnval:T
        if pos == -1: # Take the last node on the list
            pos = self.size() - 1
        
        if pos == 0: # This is the node to take
            returnval = self._data            # type: ignore
            self._data = self._next._data     # type: ignore
            self._next = self._next._next     # type: ignore
        else: # take node number (pos-1) in the rest of the list
            returnval = self._next.pop(pos-1)  # type: ignore
        # Post:
        assert self._invariant
        return returnval
    