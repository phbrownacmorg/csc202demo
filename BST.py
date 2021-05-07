from BinTree import BinTree
from typing import cast, List, Generic, Optional, TypeVar

T = TypeVar('T')

class BST(BinTree[T]):
    """Class to represent a generic binary search tree, based on BinTree.
    Data values in the tree are not duplicated; that is, a given data value
    can occur in the tree at most once."""
    
    def _invariant(self) -> bool:
        """Class invariant."""
        #print(self._data, self, self._parent)
        #if self._parent is not None:
        #    print(self._parent.leftChild(), self._parent.rightChild())
        valid:bool = (self._parent is None) or (self == self._parent.leftChild()) \
                    or (self == self._parent.rightChild())
        if self.hasLeftChild():
            leftChild:BinTree[T] = self.leftChild()
            valid = valid and leftChild._invariant()
            # Ensure that self._data > the maximum element in the left subtree
            maxChild:BinTree[T] = leftChild
            while maxChild.hasRightChild():
                maxChild = maxChild.rightChild()
            valid = valid and (self.data() > maxChild.data())               # type: ignore
        if self.hasRightChild():
            valid = valid and self.rightChild()._invariant()
            # Ensure that self._data > the maximum element in the left subtree
            minChild:BinTree[T] = self.rightChild()
            while minChild.hasLeftChild():
                minChild = minChild.leftChild()
            valid = valid and (self.data() < minChild.data())               # type: ignore
        return valid

    def __init__(self, value:Optional[T]) -> None:
        self._parent:Optional[BST[T]] = None
        super().__init__(value)
        
    def isRoot(self) -> bool:
        return self._parent is None

    def parent(self) -> BST[T]:
        assert not self.isRoot()
        return cast(BST[T], self._parent)

    def __contains__(self, value:T) -> bool:
        result:bool = False
        if self._data == value:
            result = True
        elif (self.data() > value) and self.hasLeftChild():                 # type: ignore
            result = (value in cast(BST[T], self.leftChild()))
        elif (self.data() < value) and self.hasRightChild():                # type: ignore
            result = (value in cast(BST[T], self.rightChild()))
        return result

    def findSuccessor(self) -> Optional['BST[T]']:
        """Given a node, find the next node afte rit in an inorder traversal of the tree."""
        successor:Optional[BST[T]] = None
        if self.hasRightChild(): # Successor is in the right subtree.  Find the smallest node there.
            successor = cast(BST[T], self.rightChild())
            while successor.hasLeftChild():
                successor = cast(BST[T], successor.leftChild())
        # If we get here, self has no right child
        elif self._parent is not None:
            if self._parent.leftChild() == self:
                successor = self._parent
            else:
                # Self is in its parent's right subtree.  Since self has no right child,
                # self is the biggest item in its parent's right subtree.  The successor
                # will therefore be the parent's successor, *excluding* self (and any
                # descendants of self, which would have to be smaller than self anyway
                # because self has no right subtree).
                
                # Temporarily remove self (and any descendants) from the tree
                self._parent._right = None
                # Now, find the parent's successor
                successor = self._parent.findSuccessor()
                # Now put self back to avoid fouling up the tree
                self._parent._right = self

        return successor

    # --------------- Mutators ---------------------

    def add(self, value:T) -> None:
        """Add a node containing the value VALUE to the tree.  If VALUE is
        already in the tree, do nothing."""
        # First base case: value == self._data.  Do nothing in that case.
        if value < self.data():                           # type: ignore
            # Second base case: value < self._data and self has no left child.
            if not self.hasLeftChild():
                self._left = BST[T](value)
                self._left._parent = self
            # First recursive case: add value to left subtree
            else: 
                cast(BST[T], self.leftChild()).add(value)
        elif value > self._data:                          # type: ignore
            # Third base case: value > self._data and self has no right child
            if not self.hasRightChild():
                self._right = BST[T](value)
                self._right._parent = self
            # Second recursive case: adsd value to right subtree
            else:
                cast(BST[T], self.rightChild()).add(value)
        # Post
        assert self._invariant() and value in self

    def remove(self, value:T) -> None:
        """Remove the node with data VALUE if it exists in the BST."""
        # Cases:
        #   1.  Value isn't in tree at all.  Do nothing.
        #   2.  Value is in the tree, and:
        #       a.  Node with value has two children
        #       b.  Node with value has one children
        #       c.  Node with value has no children
        if value == self.data():         # This is the node we are looking for.
            # Two children, case a.  Copy up the successor.
            if self.hasRightChild() and self.hasLeftChild(): 
                # With two children, the successor will be in the right subtree
                succ:BST[T] = cast(BST[T], self.findSuccessor())
                self._data = succ.data() # Copy in the data
                # Remove the successor node from its place in the right subtree
                cast(BST[T], self.rightChild()).remove(succ.data())

            # One child, case b.  Copy up the child.
            elif self.hasRightChild() or self.hasLeftChild(): 
                # Copy the child's data up into self
                if self.hasLeftChild():
                    self._data = self.leftChild().data()
                    self._right = self.leftChild()._right  # Must be done before self._left!
                    self._left = self.leftChild()._left
                else: # self.hasRightChild()
                    self._data = self.rightChild().data()
                    self._left = self.rightChild()._left  # Must be done before self._right!
                    self._right = self.rightChild()._right
                # Fix parent links (because any children now were grandchildren before)
                if self.hasLeftChild():
                    cast(BST[T], self.leftChild())._parent = self
                if self.hasRightChild():
                    cast(BST[T], self.rightChild())._parent = self

            # No children, case c.  Just delete this node.                    
            else: 
                if not self.isRoot() and self.parent().leftChild() == self:
                    self.parent()._left = None
                elif not self.isRoot() and self.parent().rightChild() == self:
                    self.parent()._right = None

        elif value > self._data and self.hasLeftChild():   # type: ignore
            # Delete from left subtree.  If there is no left subtree, do nothing.
            cast(BST[T], self.leftChild()).remove(value)
        elif value < self._data and self.hasRightChild():  # type: ignore
            # Delete from right subtree.  If there is no right subtree, do nothing.
            cast(BST[T], self.rightChild()).remove(value)

        # Post
        assert self._invariant() and value not in self
        