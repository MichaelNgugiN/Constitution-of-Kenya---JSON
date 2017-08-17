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

def parseArrangement(html_text):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_text, 'html.parser')
    constitution = []
    count = 0
    flag = False
    Pre_amble = False
    mycnt = 1;
    chapters = []
    for tag in soup.find_all():
        if tag.name == 'h6' or re.search('CHAPTER ', str(tag.text)) and tag.name == 'p':
            # print(tag.text)
            chapters.append([])
            chapters[count].append(tag)
            sections = []
            for sib in tag.next_siblings:
                if re.search('Part ', str(sib)):
                    # print(sib.text)
                    continue
                    # sib.decompose()
                    # for section in sib.next_siblings:
                    #     if re.search('Part ', str(section)):
                    #         # print(section.text)
                    #         continue
                    #     if re.search('CHAPTER ', str(section)):
                    #         break
                    #     # print(section)
                    # break
                if sib.text == 'PREAMBLE':
                    # if mycnt == 1:
                    #     for content in sib.next_siblings:
                    #         if str(content.contents[0].name) == "img":
                    #             content.decompose()
                    #         # if re.search('The Constitution of Kenya', str(content)):
                    #         #     print("Yada")
                    #         #     break
                    #         # if re.search('CHAPTER ', str(content)):
                    #         #     print("Yada Yada Yada")
                    #         #     break
                    #         print(content)
                    # mycnt = mycnt + 1
                    break
                if re.search('CHAPTER ', str(sib)):
                    break
                sections.append(sib.text)
            chapters[count].append(sections)
            count = count + 1
                # print(sib.text)
    constitution.append(chapters)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(constitution)
    return
def ParseConstitution(html_text_constitution):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_text_constitution, 'html.parser')
    constitution = []
    chapters = []
    count = 0
    flag = False
    Pre_amble = False
    mycnt = 0;
    for tag in soup.find_all():
        if re.search('The Constitution of Kenya', str(tag.text)) and tag.name == 'p':
            if tag.previous_sibling.text == 'GOD BLESS KENYA':
                for headings in tag.next_siblings:
                    if headings.name == 'h4':
                        chapters.append([])
                        chapters[count].append(headings.text)
                        sections = []
                        sections.append([])

                        # print(headings.text)
                        for sib in headings.next_siblings:
                            if str(sib.contents[0].name) == "img":
                                sib.decompose()
                            if re.search('Part ', str(sib)):
                                continue
                                # print(sib.text)
                                # for section in sib.next_siblings:
                                #     if re.search('Part ', str(section)):
                                #         print(section.text)
                                #         continue
                                #     if re.search('CHAPTER ', str(section)):
                                #         break
                                    # print("--------------------"+section.text)
                                break
                            if re.search('CHAPTER ', str(sib)):
                                break
                            if sib.find('strong'):
                                if sib.find('strong').text == 'SCHEDULES':
                                    break
                                # print()
                                sec_count = 0
                                sections[sec_count].append(sib.previous_sibling.text)
                                sectionBody = []
                                sectionBody.append(sib.text)
                                for section in sib.next_siblings:
                                    if section.find('strong'):
                                        break
                                    sectionBody.append(section.text)
                                    # print(section.text)
                                sections[sec_count].append(sectionBody)
                                # sections.append(sib.text)
                        chapters[count].append(sections)
                        count = count + 1
    constitution.append(chapters)
    # d = {t[0]:t[1:] for t in constitution}
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(constitution)
    with open('output.txt','w') as output:
            output.write(json.dumps(constitution,indent=4))
            print("DONE!")
    return



with open(def_docxfile,"rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value
    messages = result.messages
    # parseArrangement(html)
    ParseConstitution(html)






#Okay now the Foundation check, Now the real work begins
#Now User the multidimensional array to go through the document
