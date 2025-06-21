def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    chars = {}
    text = text.lower()

    for c in text:
        if c not in chars:
            chars[c] = 0
        chars[c] += 1
    
    return chars