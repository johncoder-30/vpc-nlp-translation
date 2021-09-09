a = open('/data/tam_equalized.txt','r',encoding='utf8')//file uploaded to colab
translate = open('/content/translated.txt','a',encoding='utf8')
a = a.read().split('\n')
for i in a:
  e = indic2en_model.batch_translate([i], 'ta', 'en')
  translate.write(e[0])
  translate.write('\n')
