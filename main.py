import http.client
import json
from playsound import playsound

text = input("Enter text: ")

# Must end with English
languages = {
    "Amharic": 'am',
    'Arabic': 'ar',
    'Basque': 'eu',
    "Bengali": "bn",
    "Portuguese (Brazil)": "pt-BR",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Cherokee": "chr",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "Estonian": "et",
    "Filipino": "fil",
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

connTranslate = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")
headersTranslate = {
    'content-type': "application/x-www-form-urlencoded",
    'Accept-Encoding': "application/gzip",
    'X-RapidAPI-Host': "google-translate1.p.rapidapi.com",
    'X-RapidAPI-Key': "85632300dbmsha01f5765f1a7303p18df83jsn83e04aa1780a"
}


def slugify(sentence):
    return sentence.replace(' ', '%20')


def urlify(text, target):
    slug = slugify(text)
    return f"q={slug}&target={target}"


def getTranslation(abv):
    payloadEng = urlify(text, abv)
    try:
        connTranslate.request("POST", "/language/translate/v2",
                              payloadEng.encode('utf-8'), headersTranslate)
        resEng = connTranslate.getresponse()
        dataEng = resEng.read()
    except http.client.HTTPException:
        return "🤖🦇 Error translating. Try again"
    else:
        return json.loads(dataEng.decode("utf-8"))["data"]["translations"][0]['translatedText']


if __name__ == "__main__":
    for (key, value) in languages.items():
        text = getTranslation(value)
        playsound('note.wav')
        print(f"\n{key}: " + text)
