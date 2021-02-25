import abc
from typing import cast, List, Tuple

# @total_ordering
class AbstractCard(abc.ABC):
    """Abstract base class for kinds of playing cards."""

    _MIN_RANK:int = 0
    _MAX_RANK:int = -1 # Subclasses *must* override this
    _RANK_NAMES:List[str] = [] # Subclasses *must* override
    _SUITS:List[str] = [] # Subclasses *must* override

    def _invariant(self) -> bool:
        """Class invariant."""
        return (self._MIN_RANK <= self._rank <= self._MAX_RANK) \
            and self._suit in self._SUITS

    def __init__(self, suit:str, rank:int) -> None:
        """Constructs a playing card."""
        # Pre:
        assert (self._MIN_RANK <= rank <= self._MAX_RANK) and \
            suit.title() in self._SUITS
        self._suit = suit.title()
        self._rank = rank
        # Post: Class invariant (let the subclass do this)

    def rank(self) -> int:
        return self._rank
    
    def suit(self) -> str:
        return self._suit

    def __str__(self) -> str:
        """Return a string representation of a Card."""
        return str(self.suit() + ' ' + self._RANK_NAMES[self.rank()])

    def __eq__(self, other:object) -> bool:
        """Returns True iff the ranks and suits are equal."""
        equal:bool = True
        if not isinstance(other, AbstractCard):
            equal = False
        else:
            othercard:AbstractCard = cast(AbstractCard, other)
            equal = self.rank() == othercard.rank() and self.suit() == othercard.suit()
        return equal

    def __lt__(self, other:'AbstractCard') -> bool:
        """Return True iff self < other."""
        return self.rank() < other.rank() or \
            (self.rank() == other.rank() and self.suit() < other.suit())

    @staticmethod
    @abc.abstractmethod
    def makeDeck() -> List['AbstractCard']:
        """Static method to create a List of all the cards in a standard deck
        (of whatever concrete kind of cards)."""