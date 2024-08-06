import pytest
from jar import Jar

def test_init():
    # Create a new instance of Jar with a valid capacity
    jar = Jar(10)

    # Assert that the jar has the given capacity
    assert jar.capacity == 10

def test_raises_value_error():
    # Create a new instance of Jar with a negative capacity
    # This should raise a ValueError
    with pytest.raises(ValueError):
        jar = Jar(-5)

def test_empty_str():
    # Create a new instance of Jar
    jar = Jar()

    # Assert that the string representation is empty initially
    assert str(jar) == ""

def test_full_str():
    # Create a new instance of Jar
    jar = Jar()

    # Deposit 3 cookies and assert the string representation
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_too_full():
    # Create a new instance of Jar
    jar = Jar()

    # Deposit 10 cookies to reach the capacity (12)
    jar.deposit(10)

    # Try to deposit more cookies than the capacity (3)
    # This should raise a ValueError
    with pytest.raises(ValueError):
        jar.deposit(3)

def test_withdraw():
    # Create a new instance of Jar
    jar = Jar()

    # Deposit 5 cookies
    jar.deposit(5)

    # Withdraw 2 cookies and assert the jar's size
    jar.withdraw(2)
    assert jar.size == 3

def test_empty():
    # Create a new instance of Jar
    jar = Jar()

    # Try to withdraw a cookie from an empty jar
    # This should raise a ValueError
    with pytest.raises(ValueError):
        jar.withdraw(1)

# Run your tests with pytest test_jar.py.
