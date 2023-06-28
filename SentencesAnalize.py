def check_character_type(character):
    if character.isalpha():
        return "Alphabetic"
    elif character.isdigit():
        return "Numeric"
    elif not character.isalnum():
        return "Special Symbol"
    else:
        return "Unknown"

def analyze_text(text):
    result = []
    for char in text:
        char_type = check_character_type(char)
        result.append((char, char_type))
    return result

# We ask the user to enter the desired text:
input_text = input("Please, Enter your text: ")

# Analyze the text and get the result
analysis_result = analyze_text(input_text)

# Show result
for char, char_type in analysis_result:
    print(f"The letter '{char}' has an '{char_type}' type.")
import unicodedata

def get_character_type(character):
    category = unicodedata.category(character)
    if category.startswith("L"):
        return "Letter"
    elif category.startswith("N"):
        return "Number"
    elif category.startswith(("S", "P")):
        return "Symbol"
    else:
        return "Unknown"

def analyze_text(text):
    result = {"Letters": [], "Numbers": [], "Symbols": [], "Unknown": []}
    for char in text:
        char_type = get_character_type(char)
        result.setdefault(char_type, []).append(char)
    return result


def detect_language(text):
    language_data = {
        "en": "English",
        "fr": "French",
        "de": "German",
        "es": "Spanish",
        # Add other languages here
    }

    language_results = {}
    for lang_code, lang_name in language_data.items():
        lang_chars = []
        for char in text:
            if lang_code in unicodedata.name(char, "").lower():
                lang_chars.append(char)
        language_results[lang_name] = lang_chars
    return language_results

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

print("Language recognition: ")
for lang, chars in language_result.items():
    if chars:
        print(f"Language '{lang}':")
        print(", ".join(chars))
        print()
