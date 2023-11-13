from preloaded import MORSE_CODE

def decode_morse(morse_code: str) -> str:
    decoded_words = [];
    for word in morse_code.strip().split('   '):
        decoded_word = ''
        for unit in word.split(' '):
            decoded_word += MORSE_CODE[unit]
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)