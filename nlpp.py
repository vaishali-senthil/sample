import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

sentence = "At eight o'clock on Thursday morning, Arthur didn't feel very good."
print (nltk.word_tokenize(sentence))

