def main(s):
    """
    A string of length three is given. Check that it is a palindrome.
    Return True if the palindrome is False otherwise

    Args:
        s: str
    Returns:
        bool: answer
    """
    s1 = s[0]
    s2 = s[1]
    s3 = s[2]
    ans = False

    if (s3+s2+s1) == s:
        ans = True
    
    return ans