class Jar:
    def __init__(self, capacity=12):
        # Initialize a cookie jar with the given capacity
        # If capacity is not a non-negative int, raise a ValueError
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        # Return a string representation of the cookie jar
        return "🍪" * self._cookies

    def deposit(self, n):
        # Add n cookies to the cookie jar
        # If adding that many would exceed the capacity, raise a ValueError
        if self._cookies + n > self._capacity:
            raise ValueError("Cannot deposit more cookies than the jar's capacity.")
        self._cookies += n

    def withdraw(self, n):
        # Remove n cookies from the cookie jar
        # If there aren't enough cookies, raise a ValueError
        if self._cookies < n:
            raise ValueError("Cannot withdraw more cookies than available in the jar.")
        self._cookies -= n

    @property
    def capacity(self):
        # Return the cookie jar's capacity
        return self._capacity

    @property
    def size(self):
        # Return the number of cookies actually in the cookie jar
        return self._cookies
