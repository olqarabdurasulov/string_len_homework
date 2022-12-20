def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    ans = ""
    if len(s)%2 == 1:
        ans = s[len(s)//2]

    else:
        ans = s[len(s)//2 -1: len(s)//2 +1]
    return ans
