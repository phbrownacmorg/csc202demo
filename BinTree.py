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

    def isEmpty(self) -> bool:
        """An empty tree is represented by a node with no children and its data set to None."""
        return self._data is None and self._left is None and self._right is None

    def data(self) -> T:
        # Pre:
        assert self._data is not None
        return cast(T, self._data)

    def leftChild(self) -> 'BinTree[T]':
        assert self.hasLeftChild()
        return cast(BinTree[T], self._left)

    def rightChild(self) -> 'BinTree[T]':
        assert self.hasRightChild()
        return cast(BinTree[T], self._right)

    def hasLeftChild(self) -> bool:
        return (self._left is not None)

    def hasRightChild(self) -> bool:
        return (self._right is not None)

    def __len__(self) -> int:
        """Return the number of nodes in the tree."""
        count = 1 # Current node
        if self.hasLeftChild():
            count = count + len(self.leftChild())
        if self.hasRightChild():
            count = count + len(self.rightChild())
        return count

    # ----------- Traversals -----------------------

    def preorder(self) -> List[T]:
        """Do a depth-first preorder traversal, returning a list of the data values."""
        result:List[T] = [] # Result for empty tree
        if self._data is not None:
            result.append(self._data) # Parent comes before children
            if self.hasLeftChild():
                result.extend(self.leftChild().preorder())
            if self.hasRightChild():
                result.extend(self.rightChild().preorder())
        return result

    def inorder(self) -> List[T]:
        """Do a depth-first postorder traversal, returning a list of the data values."""
        result:List[T] = [] # Result for empty tree
        if self._data is not None:
            if self.hasLeftChild():
                result.extend(self.leftChild().inorder())
            result.append(self._data) # Parent comes after left and before right subtree
            if self.hasRightChild():
                result.extend(self.rightChild().inorder())
        return result

    def postorder(self) -> List[T]:
        """Do a depth-first postorder traversal, returning a list of the data values."""
        result:List[T] = [] # Result for empty tree
        if self._data is not None:
            if self.hasLeftChild():
                result.extend(self.leftChild().postorder())
            if self.hasRightChild():
                result.extend(self.rightChild().postorder())
            result.append(self._data) # Parent comes after children
        # print('postorder on (' + self._data + ') returning', result)
        return result

    # ----------- Mutator methods -------------------

    def addLeft(self, value:T) -> None:
        child:BinTree[T] = BinTree[T](value)
        if self.hasLeftChild():
            child._left = self.leftChild()
        self._left = child

    def addRight(self, value:T) -> None:
        child:BinTree[T] = BinTree[T](value)
        if self.hasRightChild():
            child._right = self.rightChild()       
        self._right = child
    

def main(args:List[str]) -> int:
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)