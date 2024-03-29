import langid
from langdetect import detect_langs
import unicodedata

def get_character_type(character):
    category = unicodedata.category(character)
    if category.startswith("L"):
        return "Letters"
    elif category.startswith("N"):
        return "Numbers"
    elif category.startswith(("S", "P")):
        return "Symbols"
    else:
        return "Unknown"

def analyze_text(text):
    result = {"Letters": [], "Numbers": [], "Symbols": [], "Unknown": []}
    for char in text:
        char_type = get_character_type(char)
        result[char_type].append(char)
    return result

# Checking the type of languages in the input text
def detect_languages(text):
    langs = detect_langs(text)
    return [(lang.lang, lang.prob) for lang in langs]

def get_language_name(lang_code):
    return langid.langs.get(lang_code, "Unknown")

# We ask the user to enter the desired text:
input_text = input("Please, Enter your text: ")

# Analyze the text and get the result
analysis_result = analyze_text(input_text)
language_probs = detect_languages(input_text)

# Show result
print("Analyze the text and get the result: ")
for char_type, chars in analysis_result.items():
    if chars:
        print(f"Type '{char_type}':")
        print(", ".join(chars))
        print()

print("language recognition: ")
for lang, prob in language_probs:
    lang_name = get_language_name(lang)
    print(f" language : {lang_name} (possibility: {prob})")
