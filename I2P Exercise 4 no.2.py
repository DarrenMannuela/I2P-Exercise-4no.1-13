
def translate(text):
    translated = ""
    for letter in range(len(text)):
        if text[letter] == "a":
            translated += text[letter]
        elif text[letter] == "i":
            translated += text[letter]
        elif text[letter] == "u":
            translated += text[letter]
        elif text[letter] == "e":
            translated += text[letter]
        elif text[letter] == "o":
            translated += text[letter]
        elif text[letter] == " ":
            translated += text[letter]
        else:
            translated = translated+text[letter]+"o"+text[letter]
    return translated


translate_this = input("What would you like to translate:")
print(translate(translate_this))
