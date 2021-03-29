from typing import List
from Q2Stacks import Queue
from Stack import Stack

def interesting(ch:str) -> bool:
    """Take a one-letter string CH and tell if it's interesting (letter or digit)."""
    return ch.isalpha() or ch.isdigit()

def palindrome(s:str) -> bool:
    """Determine whether the string S is a palindrome or not.  Ignore
    case, spaces, and punctuation."""
    isPalindrome:bool = True

    # Run through S and push everything interesting onto both a stack and a queue
    stack:Stack[str] = Stack[str]()
    queue:Queue[str] = Queue[str]()

    for ch in s: # type: str
        if interesting(ch):
            stack.push(ch.lower())
            queue.enqueue(ch.lower())

    # Pop the stack and the queue, and verify that they match.  If they're both empty before
    # any mismatch is found, then S is a palindrome.

    while isPalindrome and (not stack.isEmpty()):
        c1:str = stack.pop()
        c2:str = queue.dequeue()
        isPalindrome = isPalindrome and (c1 == c2)
    # The queue had better be empty, as well as the stack
    isPalindrome = isPalindrome and queue.isEmpty()

    return isPalindrome

def main(args:List[str]) -> int:
    inputStr:str = input('Please enter a string: ')
    print('The string \"' + inputStr + '\" is', end='')
    if not palindrome(inputStr):
        print(' NOT', end='')
    print(' a palindrome.')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))