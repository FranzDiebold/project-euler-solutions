"""
Problem 59: XOR decryption
https://projecteuler.net/problem=59

Each character on a computer is assigned a unique code and the preferred standard is
ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte
with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message,
and the key is made up of random bytes. The user would keep the encrypted message and
the encryption key in different locations, and without both "halves",
it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use
a password as a key. If the password is shorter than the message, which is likely,
the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security,
but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing
the encrypted ASCII codes, and the knowledge that the plain text must contain common
English words, decrypt the message and find the sum of the ASCII values in the original text.
"""

from typing import Iterable, List, Tuple
from itertools import cycle

from src.common.files import get_items_from_file
from src.common.strings import sum_ascii_values


MOST_COMMON_ENGLISH_WORDS = {
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 'it', 'for', 'not', 'on',
    'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we',
    'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their',
    'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make',
    'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your',
    'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only',
    'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work',
    'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day',
    'most', 'us',
}


def read_file(file_name: str) -> List[int]:
    """Read the input cipher file."""
    return [int(character) for character in get_items_from_file(file_name)]


def get_possible_encryption_keys(
    length: int = 3,
    current_encryption_key: List[int] = []
) -> Iterable[List[int]]:
    """Get all possible encryption keys consisting of `length` lower case characters."""
    for encryption_character in range(ord('a'), (ord('z') + 1)):
        new_encryption_key = current_encryption_key + [encryption_character]
        if length == 1:
            yield new_encryption_key
        else:
            yield from get_possible_encryption_keys(length - 1, new_encryption_key)


def decrypt_text(encrypted_text: Iterable[int], encryption_key: List[int]) -> str:
    """
    Decrypt the given encrypted text `encrypted_text` using
    the encryption/decryption key `encryption_key`.
    """
    return ''.join(
        chr(character ^ encryption_char)
        for character, encryption_char in zip(encrypted_text, cycle(encryption_key))
    )


def score_decrypted_text(decrypted_text: str) -> int:
    """
    Calculate a score value to estimate the probability that the decrypted text contains common
    English words.
    """
    score = 0
    for word in decrypted_text.replace('.', ' ').split():
        if word.lower() in MOST_COMMON_ENGLISH_WORDS:
            score += len(word)
    return score


def bruteforce_decrypt_file(file_name: str) -> Tuple[str, str]:
    """
    Decrypt the given file with file name `file_name` by trying all possible encryption keys.
    Return the tuple `(<decrypted_text>, <encryption_key>)`.
    """
    max_score = -1
    encryption_key = None
    text = read_file(file_name)
    for current_encryption_key in get_possible_encryption_keys(3):
        decrypted_text = decrypt_text(text, current_encryption_key)
        score = score_decrypted_text(decrypted_text)
        if score > max_score:
            max_score = score
            encryption_key = current_encryption_key
    return decrypt_text(text, encryption_key), encryption_key


def main() -> None:
    """Main function."""
    file_name = 'src/p059_xor_decryption/p059_cipher.txt'
    decrypted_text, encryption_key = bruteforce_decrypt_file(file_name)
    ascii_sum = sum_ascii_values(decrypted_text)
    print(f'The sum of the ASCII values in the original text is {ascii_sum:,}.')
    print(f'The decrypted text begins with "{decrypted_text[:100]}".')
    print(f'The encryption key is {encryption_key}.')


if __name__ == '__main__':
    main()
