import xml.etree.ElementTree as etree
import os
import re

PATH_WIKI_XML='C:\\Users\\tihor\\Documents\\'
FILENAME_WIKI='enwiki-latest-pages-articles-multistream.xml'
ENCODING="utf-8"

pathWikiXML=os.path.join(PATH_WIKI_XML, FILENAME_WIKI)

regex_expressions=[]
regex_expressions.append((re.compile('\s\s+'),' '))
regex_expressions.append((re.compile('<ref.*?<\/ref>'),''))
regex_expressions.append((re.compile('\{\{.*?\}\}'),''))
regex_expressions.append((re.compile('\[\[(?:[^|\]]*\|)'),''))
regex_expressions.append((re.compile('\[\['),''))
regex_expressions.append((re.compile('\]\]'),''))
regex_expressions.append((re.compile("'''"),"'"))
regex_expressions.append((re.compile("''"),"'"))
regex_expressions.append((re.compile(" ,"),","))
regex_expressions.append((re.compile('\=\=(?:[^|\]]*\=\=)'),''))


totalCount=0


for event, elem in etree.iterparse(pathWikiXML, events=('start', 'end')):
    if elem.tag=='{http://www.mediawiki.org/xml/export-0.10/}text' and elem.text is not None and event=='end':
        article_text=elem.text
        if article_text[:10]!='#REDIRECT ':
            for item,replace_item in regex_expressions:
                article_text=item.sub(replace_item,article_text).strip()
            x=-5

