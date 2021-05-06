# Class to represent a binary tree
# Peter Brown <peter.brown@converse.edu>, 4 May 2021

from typing import cast, List, Generic, Optional, TypeVar

T = TypeVar('T')

class BinTree(Generic[T]):
    
    def _invariant(self) -> bool:
        """Class invariant, which actually validates the entire subtree."""
        # self._data is only None in the case of an empty tree
        valid:bool = self._data is not None or (self._left is None and self._right is None)
        if self._left is not None:                      
            valid = valid and self._left._invariant()   
        if self._right is not None:                     
            valid = valid and self._right._invariant()
        return valid

    def __init__(self, value:Optional[T]) -> None:
        """Constructs a node with no children and contents VALUE."""
        self._data:Optional[T] = value
        self._left:Optional[BinTree[T]] = None
        self._right:Optional[BinTree[T]] = None
        # Post:
        assert self._invariant()

    # ---------- Query methods ------------------------------------------

    def data(self) -> Optional[T]:
        return self._data

    def leftChild(self) -> Optional['BinTree[T]']:
        return self._left                        

    def rightChild(self) -> Optional['BinTree[T]']:
        return self._right 

    def hasLeftChild(self) -> bool:
        return (self._left is not None)

    def hasRightChild(self) -> bool:
        return (self._right is not None)

    def __len__(self) -> int:
        """Return the number of nodes in the tree."""
        count = 1 # Current node
        if self.hasLeftChild():
            count = count + len(cast(BinTree[T], self._left))
        if self.hasRightChild():
            count = count + len(cast(BinTree[T], self._right))
        return count

    # ----------- Mutator methods -------------------

    def addLeft(self, value:T) -> None:
        child:BinTree[T] = BinTree[T](value)
        if self.hasLeftChild():
            child._left = self._left
        self._left = child

    def addRight(self, value:T) -> None:
        child:BinTree[T] = BinTree[T](value)
        if self.hasRightChild():
            child._right = self._right           
        self._right = child
    

def main(args:List[str]) -> int:
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)