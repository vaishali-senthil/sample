import os
import nltk
from nltk import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.stem import 	WordNetLemmatizer

myfile = open("D:\sample1.txt")
print(myfile)
text=myfile.read()
print(text)

sentences = word_tokenize(text)
print(len(sentences))
sentences

wordcloud = WordCloud().generate(text)
plt.figure(figsize = (12, 12))
plt.imshow(wordcloud)

plt.axis("off")
plt.show()



wordnet_lemmatizer = WordNetLemmatizer()
text = "studies studying cries cry"
tokenization = nltk.word_tokenize(text)
for w in tokenization:
	print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w)))