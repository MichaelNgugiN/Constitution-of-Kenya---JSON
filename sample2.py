'+-------------------------------------------------------------------+'
'| = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = |'
'|{>/-------------------------------------------------------------\<}|'
'|: | Author:  Michael Ngugi                                      | :|'
'| :| Email:   micqualngugi96@gmail.com                           | :|'
'|: | Purpose: Parse Law Documents Using BeautifulSoup            | :|'
'|: | Date: 16-August-2017                                        | :|'
'| :| Version: 1.0                                                | :|'
'| :| Language: Python                                            | :|'
'| :| Script: (parser.py) functional text Extraction.             | :|'
'|{>\-------------------------------------------------------------/<}|'
'| = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = |'
'+-------------------------------------------------------------------+'

import mammoth
import json
import re
import pprint

def_docxfile = "mm.docx"
with open(def_docxfile,"rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value
    messages = result.messages

def parse(html_text):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_text, 'html.parser')
    sections = [[]]
    count = 1
    flag = False
    for tag in soup.find_all("):
        closenow = False
        sections.append([])
        sections[count].append(tag);
        if str(tag.name) == "img":
            tag.decompose()
            continue
        inner_sec = []
        for sibling in tag.next_siblings:
            if sibling.name == 'h6' or re.search('CHAPTER ', str(sibling.text)) and sibling.name == 'p':
                print(sibling.text)


            if sibling.text == 'PREAMBLE':
                break
            if re.search('Part ', str(sibling)):
                flag = True
                # print(sibling.text)
                for sib in sibling.next_siblings:
                    if re.search('Part ', str(sib)):
                        break
                    if re.search('CHAPTER ', str(sib)):

                        # print(sib.text)
                        closenow = True
                        flag = False
                        break
                    # print(sib)
                continue
            if flag:
                continue
            if closenow:
                continue
            # print(sibling.text)


            inner_sec.append(str(sibling.text))
        sections[count].append(inner_sec)
        count = count + 1




    pp = pprint.PrettyPrinter(indent=4)
        # contains the name of a section
    # pp.pprint(sections)


    # sections = [[]]
    # count = -1
    # for tag in soup.select('tr'):
    #     if tag.select('td p strong'):
    #         if re.search('Division', str(tag.text)):
    #             sections[count].append(sanitize_text(str(tag.text)))
    #             continue
    #         count = count + 1
    #         sections.append([])
    #         sections[count].append(sanitize_text(str(tag.text)))
    #     else:
    #         if tag.select('td[colspan=4] p') != []:
    #             sections[count].append(sanitize_text(str(tag.select('td[colspan=4] p'))))
    # # d = {t: for t in sections[2]}
    with open('outputConst.txt','w') as output:

        print("DONE!")
    return

with open(def_docxfile,"rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value
    messages = result.messages
    parse(html)






#Okay now the Foundation check, Now the real work begins
#Now User the multidimensional array to go through the document
