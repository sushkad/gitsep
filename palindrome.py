def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


s = "A man a plan a canal Panama"

print(is_palindrome(s))
