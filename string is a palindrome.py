def is_strinpalindrome(s):
    return s == s[::-1]

string = "racecar"

if is_strinpalindrome(string):
    print(f" {string} is a palindrome")
else:
    print(f" {string} is not a palindrome")

