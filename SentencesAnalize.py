import langid
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

def detect_language(text):
    language_data = {
        "en": "English",
        "fr": "French",
        "de": "German",
        "es": "Spanish",
        "fa": "Farsi",
        # Add other languages here
    }

# We ask the user to enter the desired text:
input_text = input("Please, Enter your text: ")

# Analyze the text and get the result
analysis_result = analyze_text(input_text)
language_result = detect_language(input_text)

# Show result
print("Analyze the text and get the result: ")
for char_type, chars in analysis_result.items():
    if chars:
        print(f"Type '{char_type}':")
        print(", ".join(chars))
        print()

print("anguage recognition: ")
for lang, words in language_result.items():
    if words:
        print(f"language '{lang}':")
        for word in words:
            print(f"word '{word}'")
        print()
