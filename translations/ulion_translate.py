import translators as ts

tam = open('./data/tam_equalized.txt', 'r',encoding='utf8').read().split('\n\n')
trans = open('data/ulion_translate.txt', 'a')

for i in range(10):
    for j in range(len(tam[i].split('\n'))):
        try:
            t_line = tam[i].split('\n')[j]
            trans.write(ts.google(t_line, from_language='ta', to_language='en'))
            trans.write('\n')
        except UnicodeEncodeError:
            trans.write('error')
            trans.write('\n')

    trans.write('\n')
