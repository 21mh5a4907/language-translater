from googletrans import Translator, LANGUAGES

def get_user_input():
    return input("Enter the text you want to translate: ")

def select_target_language():
    print("\nSelect the target language:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")

    target_code = input("Enter the language code: ")
    return target_code.lower()

def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

if __name__ == "__main__":
    user_input = get_user_input()
    target_language = select_target_language()

    translated_text = translate_text(user_input, target_language)

    print(f"\nOriginal text ({translator.detect(user_input).lang}): {user_input}")
    print(f"Translated text ({target_language}): {translated_text}")
