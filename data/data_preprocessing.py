import os
# from indicnlp.tokenize import sentence_tokenize
# import nltk
import re

# nltk.download('punkt')
# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
#
# def split_sentences(paragraph, language):
#     if language == "en":
#         return nltk.tokenize.sent_tokenize(paragraph)
#     else:
#         return sentence_tokenize.sentence_split(paragraph, lang='ta')

files = os.listdir("./resources")//folder containing raw data with 10 english and 10 tamil text files
eng_data = open('./data/english.txt', 'a', encoding='utf8')//text file in which english data to be written
tam_data = open('./data/tamil.txt', 'a', encoding='utf8')//text file in which tamil data to be written
for i in files:
    a = i.rsplit('.txt')
    b = a[0].split('-')
    loc = "./resources/" + i
    file = open(loc, 'r', encoding='utf8')
    info = file.read()
    info = info.splitlines()

    if b[-1] == 'ta':
        data = ''
        for j in info:
            s = ''
            x = j.split(' ')
            for k in x:
                s = s + k + ' '
            s = re.sub("\{.*?\}", "", s)
            s = re.sub("\(.*?\)", "", s)
            data += s
        # s = split_sentences(data, language='ta')
        s = data.split('.')
        for q in s:
            if len(q) < 9:
                continue
            else:
                tam_data.write(q)
                tam_data.write('\n')
        tam_data.write('\n')

    else:
        data = ''
        if info[0].split(' ')[0]=='SECTION':
            info = info[2:]
        for j in info:
            s = ''
            x = j.split(' ')
            for k in x:
                if k[:2] == 'p.' or k[0] == '6' or k[0] == '7' :
                    continue
                else:
                    s = s + k + ' '
            s = re.sub("\(.*?\)", "", s)
            data += s
        # s = split_sentences(data, language='en')
        s = data.split('.')
        s = s[:-2]

        for q in s:
            if len(q) < 10:
                continue
            else:
                eng_data.write(q)
                eng_data.write('\n')
                # print(q)
        eng_data.write('\n')

