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

def sort_dict_by_count(inp_dict):
    list_dict = []
    for key, value in inp_dict.items():
        list_dict.append({"char": key, "num": value})
    print(list_dict)
    list_dict.sort(reverse=True, key=sort_on)
    print(list_dict)
    return list_dict

def sort_on(items):
    return items["num"]