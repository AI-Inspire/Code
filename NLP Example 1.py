from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag #importing necessary libraries which will be called in code to perform NLP tasks
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

#TASK 1
text = "Hi! How are you today? I am awesome! How about you?"
print(word_tokenize(text)) #tokenizing text by splitting it wherever space is present in the sentence
print() #new line

#TASK 2
print(sent_tokenize(text))#tokenizing text by splitting it wherever a punctuation mark is present
print() #new line


#TASK 3 : tokenizing words in a diff. language, tokenizing so that sentences are separated by punctuation marks
textSpanish = "¡Hola! Estoy feliz porque estoy aprendiendo a codificar. ¿Cómo estás?"
print(sent_tokenize(textSpanish,"spanish"))
print() #new line


#TASK 4
#example with Part Of Speech (POS) Tagging, homynoyms are present in text : words with same spelling but diff. meaning
text1 = "They refuse to permit us to obtain the refuse permit"
print(pos_tag(text1)) #determing POS of each word
print() #new line


#TASK 5 : Word stemming
WordStemmer = PorterStemmer()
print(WordStemmer.stem('coding'))
print(WordStemmer.stem('seesaw'))
print(WordStemmer.stem('purple'))
print() #new line

#TASK 6 : Removing stop words
sentence = "You don't need a pen to write this essay. No pens are allowed. Only pencils are allowed."
stopWords = set(stopwords.words('english')) #generating all stop words in English
words = word_tokenize(sentence) #tokenizing the sentence into individual words
wordsFiltered = [] #this is an array, where all words will be filtered, and stop words will be removed

for w in words: #traversing through
    if w not in stopWords:  #if word is not a stop word
        wordsFiltered.append(w) #add it to the wordsFiltered[]

print(wordsFiltered) #print all of the words filtered (not stop words)
