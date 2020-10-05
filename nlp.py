import os
import nltk
import nltk.corpus
from nltk import Tree
from nltk.draw import TreeView
from nltk import word_tokenize

myfile = open("D:\sample.txt")
print(myfile)
text=myfile.read()
print(text)
print(myfile.readlines())
print (len(text))


sentence = [("a", "DT"),("clever","JJ"),("fox","NN"),("was","VBP"),
   ("jumping","VBP"),("over","IN"),("the","DT"),("wall","NN")]
grammar = "NP:{<DT>?<JJ>*<NN>}"
parser_chunking = nltk.RegexpParser(grammar)
parser_chunking.parse(sentence)
output = parser_chunking.parse(sentence)
output.draw()



words = word_tokenize(text)
print (len(words))
print (words)


