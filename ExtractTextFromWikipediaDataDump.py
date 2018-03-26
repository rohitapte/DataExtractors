import os
import re

INPUT_DIR='C:/Users/tihor/Documents/wiki_text'
OUTPUT_PATH='C:/Users/tihor/Documents'
OUTPUT_FILE='text_corpus_cased.txt'
ENCODING="utf-8"
LOWERCASE=False

remove_space_comma=re.compile(r' ,')
file_count=0

with open(os.path.join(os.path.normpath(OUTPUT_PATH),OUTPUT_FILE),"w",encoding=ENCODING) as f_out:
    for dirpath,dirnames,filenames in os.walk(os.path.normpath(INPUT_DIR)):
        for file in filenames:
            file_count+=1
            with open(os.path.join(dirpath,file),'r',encoding=ENCODING) as f_in:
                content=f_in.readlines()
                for item in content:
                    tag_check=item[0:5]
                    if tag_check!='<doc ' and tag_check!='</doc':
                        text=item.replace('<nowiki>*</nowiki>','')
                        text=remove_space_comma.sub(' ',text).strip()
                        if LOWERCASE:
                            text=text.lower()
                        if len(text)>0:
                            f_out.write(text+'\n')
            if file_count>1000:
                break

