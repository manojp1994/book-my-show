import nltk
from nltk.corpus import stopwords
from nltk.tokenize import  word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

# example
traintext=state_union.raw("2003-GWBush.txt")
sampletext=state_union.raw("2004-GWBush.txt")

sometext=PunktSentenceTokenizer(traintext)
tokenizedsometext=sometext.tokenize(sampletext)


def process_content():
    try:
        for i in tokenizedsometext:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<.*>+}
            }<VB.?|IN|DT|TO>+{"""
            # print(chunkGram)
            chunkParser=nltk.RegexpParser(chunkGram)
            chunked=chunkParser.parse(tagged)
            # print(chunked)
            chunked.draw()

    except Exception as e:
        print(str(e))

process_content()
