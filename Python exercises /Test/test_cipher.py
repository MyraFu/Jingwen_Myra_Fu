import pytest
import pandas as pd

def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    assert type(shift) == int, "Shift parameter needs to be an integer"
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

def test_cipher_single():
    example = 'QMSS'
    expected = 'RNTT'
    actual = cipher('QMSS', 1)
    assert actual == expected

def test_cipher_negative():
    example = 'QMSS'
    expected = 'PLRR'
    actual = cipher('QMSS', shift = -1)
    assert actual == expected

def test_cipher_others():
    example = 'CU2022', 1
    expected = 'DV2022'
    actual = cipher('CU2022', shift = 1)
    assert actual == expected

def test_cipher_string():
    example = 'QMSS'
    shift = 'two'
    expected = 'SOUU'
    with pytest.raises(AssertionError):
        assert cipher(example, shift) == expected
        
@pytest.mark.parametrize(('example, expected'), [
    ('QMSS', 'RNTT'), 
    ('cu', 'dv'), 
    ('Fu', 'Gv'), 
    ('TikTok is additive', 'UjlUpl jt beejujwf')
])
def test_cipher_exs(example, expected):
    output = cipher(example, 1)
    assert output == expected
    
@pytest.mark.parametrize(('example, shift, expected'), [('fu', 1, 'gv'), ('fu', 2, 'hw'), ('fu', 3, 'ix'), 
        ('fu',4, 'jy'), ('fu',5, 'kz'), ('fu',6, 'lA'), ('fu',7, 'mB'), 
        ('fu',8, 'nC'), ('fu',9, 'oD'), ('fu',10, 'pE')
])
def test_cipher_dec(example, shift, expected):
    encrypted = cipher(example, shift)
    decrypted = cipher(encrypted, shift, encrypt = False)
    assert example == decrypted



