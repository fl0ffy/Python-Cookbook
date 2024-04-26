""""Module for playing with words"""


def ispalindrome(s: str) -> bool:
    """Function to determine if provided string is a palindrome"""
    return s.replace(" ", "").lower() == s[::-1].replace(" ", "").lower()


def test_ispalindrome() -> None:
    """Unit test for ispalindrome function"""
    assert ispalindrome("Ten animals I slam in a net") is True
    assert ispalindrome("Eleven animals I slam in a net") is False


def isanagram(s1: str, s2: str) -> bool:
    """Function for determining if two given strings are anagrams of one another"""
    return sorted(s1.lower()) == sorted(s2.lower())


def test_isanagram() -> None:
    """Unit test for isanagram function"""
    assert isanagram("Listen", "Silent") is True
    assert isanagram("modern", "norman") is False


def main() -> None:
    """Main"""
    return


if __name__ == "__main__":
    main()
