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
        result[char_type].append(char)
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
        lang_words = []
        for word in text.split():
            word_chars = []
            for char in word:
                if lang_code in unicodedata.name(char, "").lower():
                    word_chars.append(char)
            lang_word = "".join(word_chars)
            if lang_word:
                lang_words.append(lang_word)
        language_results[lang_name] = lang_words
    return language_results

def check_word(word):
    invalid_chars = ["|"]
    for char in word:
        if char in invalid_chars:
            return f"Invalid character '{char}' found in word '{word}'"
    return None

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
        print(f"Language '{lang}':")
        for word in words:
            error = check_word(word)
            if error:
                print(f"Word '{word}': error - {error}")
            else:
                print(f"Word '{word}': valid")
        print()
