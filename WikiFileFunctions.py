import os
from nltk.tokenize import sent_tokenize
import re

class GlobalVariables(object):
    def __init__(self):
        #reads the files spit out by wikiextractor in this directory
        self.WIKIPEDIA_INPUT_DIR='C:/Users/tihor/Documents/wiki_text'
        #no need to write output since we can save model and continue training
        self.ENCODING='utf-8'
        self.character_vocab=[' ', 'e', 'a', 't', 'i', 'n', 'o', 'r', 's', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'p', 'g', 'w', 'y', 'b', ',', '.', 'v', 'START_TOKEN', 'END_TOKEN', 'k', '"', '1', '0', '9', '2', '-', 'x', 'j', "'", ')', '(',
                               '8', '5', '3', '4', '6', 'z', '7', 'q', '%', ':', ';', '–', '/', '\xa0', '$', 'é', '—', '’', '&', '_', ']', '[', 'á', '²', '”', '“','UNKNOWN_TOKEN']


class WikiFileSentences(object):
    def __init__(self):
        self.vars=GlobalVariables()
        print(self.vars.ENCODING)
        print(self.vars.WIKIPEDIA_INPUT_DIR)
        self.remove_space_comma=re.compile(r' ,')

    def __iter__(self):
        for dirpath, dirnames, filenames in os.walk(os.path.normpath(self.vars.WIKIPEDIA_INPUT_DIR)):
            for file in filenames:
                for line in open(os.path.join(dirpath,file),'r',encoding=self.vars.ENCODING):
                    tag_check=line[0:5]
                    if tag_check != '<doc ' and tag_check != '</doc':
                        text=line.replace('<nowiki>*</nowiki>', '')
                        text=self.remove_space_comma.sub(' ', text).strip()
                        text=text.lower()
                        if len(text)>0:
                            for sentence in sent_tokenize(text):
                                char_sentence=['START_TOKEN']
                                for s in list(sentence):
                                    if s in self.vars.character_vocab:
                                        char_sentence.append(s)
                                    else:
                                        char_sentence.append('UNKNOWN_TOKEN')
                                char_sentence.append('END_TOKEN')
                                yield char_sentence

zz=WikiFileSentences()
for item in zz:
    print(item)