from collections import Counter

def is_valid_anagram(s, t):
    s_counter = Counter(s)
    t_counter = Counter(t)
    is_valid = True
    for alph, count in s_counter.items():
        if not t_counter.get(alph) or count != t_counter.get(alph):
            return False
    for alph, count in t_counter.items():
        if not s_counter.get(alph) or count != s_counter.get(alph):
            return False
    return is_valid

s = "a"
t = "ab"
print(is_valid_anagram(s, t))