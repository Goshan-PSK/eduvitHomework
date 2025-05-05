import re

def is_palindrome(text: str) -> bool:
    cleaned = re.sub(r'[^a-zа-я0-9]', '', text.lower(), flags=re.IGNORECASE)
    return cleaned == cleaned[::-1]

assert is_palindrome("Я иду с мечем судия") == True

assert is_palindrome("казак") == True

assert is_palindrome("Madam In Eden, I'm Adam") == True

assert is_palindrome("Скоро экзамен по математике") == False

assert is_palindrome("а") == True

print("All tests passed.")