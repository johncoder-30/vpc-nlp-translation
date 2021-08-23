from nltk.translate.bleu_score import corpus_bleu

test = open('./data/eng_equalized.txt', 'r').read().split('\n\n')
pred = open('./data/ulison_translate.txt', 'r').read().split('\n\n')

for i in range(10):
    test_line = []
    pred_line = []
    for j in range(len(test[i].split('\n'))):
        t_line = test[i].split('\n')[j].split()
        test_line.append(t_line)
        p_line = pred[i].split('\n')[j].split()
        pred_line.append(p_line)
    bleu = corpus_bleu(test_line, pred_line, weights=(1.0, 0, 0, 0))
    print(f'BLEU score of para {i + 1} is {bleu}')
