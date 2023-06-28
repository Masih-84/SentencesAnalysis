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
