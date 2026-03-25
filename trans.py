from deep_translator import GoogleTranslator

text1 = input("Enter the text to be translated: ")
text2 = input("Enter target language (e.g., ta, hi, fr): ")

res = GoogleTranslator(source='en', target=text2).translate(text1)

print("Original:", text1)
print("Translated:", res)