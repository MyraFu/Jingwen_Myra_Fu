from cipher_jf3483 import cipher_jf3483
import pytest

def test_cipher_single():
    example = 'QMSS'
    expected = 'RNTT'
    actual = cipher_jf3483.cipher('QMSS', shift = 1)
    assert actual == expected