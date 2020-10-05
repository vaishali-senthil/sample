from textblob import TextBlob
from textblob import Word

text_word = Word('tired')

antonyms = set()
for synset in text_word.synsets:
    for lemma in synset.lemmas():
        if lemma.antonyms():
            antonyms.add(lemma.antonyms()[0].name())

print(antonyms)