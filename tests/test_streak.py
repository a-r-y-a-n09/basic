import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test a list with no positive numbers returns a streak of 0."""
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_all_positive_numbers():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    """Test a simple case with one streak."""
    assert longest_positive_streak([1, 2, 0, -1, 3]) == 2

def test_multiple_streaks_longest_first():
    """Test multiple streaks where the longest streak is first."""
    assert longest_positive_streak([1, 2, 3, 0, 1, 2]) == 3

def test_multiple_streaks_longest_last():
    """Test multiple streaks where the longest streak is last."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3]) == 3

def test_streaks_with_zeros():
    """Test streaks separated by zeros."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6, 0, 8]) == 3

def test_streaks_with_negatives():
    """Test streaks separated by negative numbers."""
    assert longest_positive_streak([1, -2, 4, 5, -6, 8, 9, 10]) == 3

def test_streak_at_the_beginning():
    """Test a list where the longest streak is at the beginning."""
    assert longest_positive_streak([1, 2, 3, 4, 0, 5, -1, 2]) == 4

def test_streak_at_the_end():
    """Test a list where the longest streak is at the end."""
    assert longest_positive_streak([1, 0, 5, -1, 2, 3, 4, 5, 6]) == 5

def test_list_with_single_elements():
    """Test a list with single positive elements creating streaks of 1."""
    assert longest_positive_streak([1, 0, 2, 0, 3]) == 1

def test_list_with_one_number():
    """Test lists with a single number."""
    assert longest_positive_streak([5]) == 1
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0