def is_palindrome(string):
    string = str.join("", (s for s in string if s.isalnum())).lower()
    for i in range(0, len(string) - 1):
        if string[i] != string[len(string) - 1 - i]:
            return False

    return True


if __name__ == "__main__":
    print(is_palindrome('hello world'))
    print(is_palindrome('Go hang a salami, I’m a lasagna hog.'))
    print(is_palindrome("racecar"))
    print(is_palindrome("palindrome"))
