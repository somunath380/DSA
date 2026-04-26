def is_pangram(sentence):
    found_chars = {}
    for ch in sentence:
        if not found_chars.get(ch):
            found_chars[ch] = 1
    return sum(found_chars.values()) == 26

sent = "thequickbrownfoxjumpsoverthelazydog"
print(is_pangram(sent))