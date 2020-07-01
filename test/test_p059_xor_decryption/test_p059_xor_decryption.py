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

import pytest


def test_get_possible_encryption_keys_length_1():
    # arrange
    from src.p059_xor_decryption.p059_xor_decryption import get_possible_encryption_keys

    # act
    actual_result_iter = get_possible_encryption_keys(1)

    # assert
    expected_result = list([character] for character in range(97, 123))
    assert list(actual_result_iter) == expected_result


def test_get_possible_encryption_keys_length_3():
    # arrange
    from src.p059_xor_decryption.p059_xor_decryption import get_possible_encryption_keys

    # act
    actual_result_iter = get_possible_encryption_keys(3)

    # assert
    actual_result = list(actual_result_iter)
    expected_length = pow(26, 3)
    expected_result_start = [
        [97, 97, 97],
        [97, 97, 98],
        [97, 97, 99],
        [97, 97, 100],
    ]
    expected_result_end = [
        [122, 122, 119],
        [122, 122, 120],
        [122, 122, 121],
        [122, 122, 122],
    ]
    assert len(actual_result) == expected_length
    assert actual_result[:4] == expected_result_start
    assert actual_result[-4:] == expected_result_end


def test_decrypt_text():
    # arrange
    from src.p059_xor_decryption.p059_xor_decryption import decrypt_text

    encrypted_text = [65, 107]

    # act
    actual_result = decrypt_text(encrypted_text, [42])

    # assert
    expected_result = 'kA'
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_decrypted_text,expected_result', [
    ('This text consists of common english words.', 6),
    ('hrnskhqing82jdnak 39gsjd la39gnda49', 0)
])
def test_score_decrypted_text(test_input_decrypted_text, expected_result):
    # arrange
    from src.p059_xor_decryption.p059_xor_decryption import score_decrypted_text

    # act
    actual_result = score_decrypted_text(test_input_decrypted_text)

    # assert
    assert actual_result == expected_result
