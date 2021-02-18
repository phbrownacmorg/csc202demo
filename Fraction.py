class Fraction(object):
    """Class to represent a fraction a/b, b != 0, in terms of two integers.
    Objects of the class are immutable once created."""

    @staticmethod
    def _gcd(a:int, b:int) -> int:
        """Find and return the greatest common divisor of two integers."""
        while a != 0:
            a, b = b % a, a
        return abs(b)
    
    def __init__(self, numerator:int, denominator:int):
        """Constructor for a Fraction object."""
        # Pre:
        assert denominator != 0
        self._numr:int = numerator
        self._denom:int = denominator
        self._reduce() # Reduce to lowest terms

        # Post:
        assert self._invariant()

    # Helper functions

    def _invariant(self) -> bool:
        """Class invariant for the Fraction class."""
        return self._denom > 0 and Fraction._gcd(self._numr, self._denom) == 1

    def _reduce(self) -> None:
        """Reduce the Fraction to its lowest terms."""
        # Pre:
        assert self._denom != 0
        if self._denom < 0:  # Get rid of negative sign in the denominator
            self._numr = -self._numr
            self._denom = -self._denom

        gcd:int = Fraction._gcd(self._numr, self._denom)
        if gcd > 1:
            self._numr = self._numr // gcd
            self._denom = self._denom // gcd

        # Post
        assert self._invariant()

    # Query functions

    def numerator(self) -> int:
        # Pre:
        assert self._invariant()
        return self._numr
    
    def denominator(self) -> int:
        # Pre:
        assert self._invariant()
        return self._denom

    def __str__(self) -> str:
        """String representation of a Fraction."""
        # Pre:
        assert self._invariant()
        return str(self._numr)+"/"+str(self._denom)

    def __eq__(self, other:object) -> bool:
        """Returns True iff self == other (representing the same fraction)."""
        # Satisfy the substitution principle, since Fraction extends object
        if not isinstance(other, Fraction):
            return NotImplemented
        # Else, other is a Fraction and we proceed from there
        # Pre:
        assert self._invariant() and isinstance(other, Fraction) and other._invariant()
        result:bool = self.numerator() == other.numerator() and self.denominator() == other.denominator()
        # Post: result == True iff self and other represent the same fraction
        return result


    # Type of the class currently being described must be in quotes.
    # Otherwise, python doesn't recognize the symbol and the code fails.
    def __add__(self, other:'Fraction') -> 'Fraction':
        """Add self to other, and return a new Fraction equal to their sum."""
        # Pre:
        assert self._invariant() and other._invariant()

        newdenom:int = self.denominator() * other.denominator()
        newnumr:int = self.numerator() * other.denominator() + other.numerator() * self.denominator()
        result:Fraction = Fraction(newnumr, newdenom)

        # Post: result == self + other and
        assert result._invariant()
        return result # Note this will be reduced to lowest terms


