from playsound import playsound
from googletrans import Translator

text = input("Enter text: ")
translator = Translator()

# Must end with English
languages = {
    "Amharic": 'am',
    'Arabic': 'ar',
    'Basque': 'eu',
    "Bengali": "bn",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "Estonian": "et",
    "Finnish": "fi",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Hebrew": "iw",
    "Hindi": "hi",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Indonesian": "id",
    "Italian": "it",
    "Japanese": "ja",
    "Kannada": "kn",
    "Korean": "ko",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Malay": "ms",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Norwegian": "no",
    "Polish": "pl",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian": "sr",
    "Chinese (PRC)": "zh-CN",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Spanish": "es",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tamil": "ta",
    "Telugu": "te",
    "Thai": "th",
    "Chinese (Taiwan)": "zh-TW",
    "Turkish": "tr",
    "Urdu": "ur",
    "Ukrainian": "uk",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "English": 'en',
}

def getTranslation(abv):
    try:
        response = translator.translate(text, dest=abv).text
    except Exception:
        print(f"\n🤖🦇: Error translating in {abv}")
        return
    else:
        return response


if __name__ == "__main__":
    for (key, value) in languages.items():
        text = getTranslation(value)
        playsound('note.wav')
        print(f"\n{key}: " + text)
