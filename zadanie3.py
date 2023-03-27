# Zadanie 3

def caesar_cipher(text, key, alphabet=None):
    if alphabet is None:
        alphabet = list("abcdefghijklmnopqrstuvwxyz".strip())

    text = list(text.lower().strip())
    res = ""
    for t in text:
        if t in alphabet:
            res += alphabet[(alphabet.index(t) + key) % len(alphabet)]
        else:
            res += t
    return res


data = "The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll"

# enc = caesar_cipher(data, 5)
# enc = caesar_cipher(data, 31)
enc = caesar_cipher(data, 3, ["a", "B"])
print(enc)
