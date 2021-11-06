from cipher_ky2458 import cipher_ky2458
def test_cipher():
    text = 'K'
    expected = 'L'
    actual = cipher(text, 1)
    assert actual == expected, "Cipher failed."