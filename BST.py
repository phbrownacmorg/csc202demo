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
            leftChild:BST[T] = cast(BST[T], self._left)
            valid = valid and leftChild._invariant()
            # Ensure that self._data > the maximum element in the left subtree
            maxChild:BST[T] = leftChild
            while maxChild.hasRightChild():
                maxChild = cast(BST[T], maxChild.rightChild())
            valid = valid and (cast(T, self._data) > cast(T, maxChild._data))
        if self.hasRightChild():
            valid = valid and cast(BST[T], self._right)._invariant()
            # Ensure that self._data > the maximum element in the left subtree
            minChild:BST[T] = cast(BST[T], self._right)
            while minChild.hasLeftChild():
                minChild = cast(BST[T], minChild.leftChild())
            valid = valid and (cast(T, self._data) < minChild._data)
        return valid

    def __init__(self, value:Optional[T]) -> None:
        self._parent = None
        super().__init__(value)
        

    def __contains__(self, value:T) -> bool:
        result:bool = False
        if self._data == value:
            result = True
        elif (cast(T, self._data) > value) and self.hasLeftChild():
            result = (value in self._left)
        elif self._data < value and self.hasRightChild():
            result = (value in self._right)
        return result

    def findSucccessor(self) -> Optional['BST[T]']:
        """Given a node, find the next node afte rit in an inorder traversal of the tree."""
        successor:BST[T] = None
        if self.hasRightChild(): # Successor is in the right subtree.  Find the smallest node there.
            successor = self.rightChild()
            while successor.hasLeftChild():
                successor = successor.leftChild()
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
        if value < self._data:
            # Second base case: value < self._data and self has no left child.
            if not self.hasLeftChild():
                self._left = BST[T](value)
                self._left._parent = self
            # First recursive case: add value to left subtree
            else: 
                self._left.add(value)
        elif value > self._data:
            # Third base case: value > self._data and self has no right child
            if not self.hasRightChild():
                self._right = BST[T](value)
                self._right._parent = self
            # Second recursive case: adsd value to right subtree
            else:
                self._right.add(value)
        # Post
        assert self._invariant() and value in self

    def remove(self, value:T) -> None:
        """Remove the node with data VALUE if it exists in the BST."""
        # Cases:
        #   1.  Node isn't in tree at all
        #   2.  This is the node, and:
        #       a.  This node has no children
        #       b.  This node has one child
        #       c.  This node has two children
        if value == self._data:
            # Behold the node!  Fill in later.
            if not self.hasRightChild() and not self.hasRightChild(): # No children
                if self._parent.leftChild() == self:
                    self._parent._left = None
                elif self._parent.rightChild() == self:
                    self._parent._right = None
            elif self.hasLeftChild(): # One child, on the left
                if self._parent.leftChild() == self:
                    self._parent._left = self.leftChild()
                    self.leftChild()._parent = self._parent
                elif self._parent.rightChild() == self:
                    self._parent._right = self.leftChild()
                    self.rightChild()._parent = self._parent
            elif self.hasRightChild(): # One child, on the right
                if self._parent.leftChild() == self:
                    self._parent._left = self.rightChild()
                    self.rightChild()._parent = self._parent
                elif self._parent.rightChild() == self:
                    self._parent._right = self.rightChild()
                    self.rightChild()._parent = self._parent
            else: # Two children
                succ:BST[T] = findSuccessor(self)
                # Remove the successor node from its place in the right subtree (if any)
                self.rightChild().remove(succ._data)
                succ._left = self._left
                succ._right = self._right
                succ._parent = self._parent
                if self._parent.leftChild() == self:
                    self._parent._left = succ
                elif self._parent.rightChild() == self:
                    self._parent._right = succ

        elif value > self._data and self.hasLeftChild():
            # Delete from left subtree.  If there is no left subtree, do nothing.
            self.leftChild().remove(value)
        elif value < self._data and self.hasRightChild():
            # Delete from right subtree.  If there is no right subtree, do nothing.
            self.rightChild().remove(value)

        # Post
        assert self._invariant() and value not in self
        