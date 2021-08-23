# Aug 2021 - Venmurasu Programming Contest 


Stage-1: Building Parallel Dataset

 - We looped through the data separated it by full stop, used regex to remove items in brackets.
 - then we manually corrected one to many and many to one statements

Stage-2: Running a Neural Machine Translation Model

- We fed the tamil data to AI4Bharat in colab and got the respective translated english sentences

Stage-3: Computing the scores of translation

- Then for BLEU score we used the NLTK library and passed the english translated and english sentences

Stage-4: (Bonus points) Compare the model with other services

- Then using this library (https://github.com/UlionTse/translators) we translated the tamil sentences
- then calculated the BLEU scores using the same NLTK library

###BLEU score computation for translated sentence using AI4BHARAT Model
- BLEU score of para 1 is 0.003816793893129772
- BLEU score of para 2 is 0.019354838709677424
- BLEU score of para 3 is 0.006864988558352401
- BLEU score of para 4 is 0.023758099352051837
- BLEU score of para 5 is 0.006993006993006996
- BLEU score of para 6 is 0.027848101265822784
- BLEU score of para 7 is 0.03237410071942446
- BLEU score of para 8 is 0.023992322456813823
- BLEU score of para 9 is 0.01955555555555556
- BLEU score of para 10 is 0.023578363384188623

###BLEU score computation for translated sentence using UlionTse library
- BLEU score of para 1 is 0.011363636363636359
- BLEU score of para 2 is 0.005181347150259067
- BLEU score of para 3 is 0.021739130434782608
- BLEU score of para 4 is 0.002881844380403458
- BLEU score of para 5 is 0
- BLEU score of para 6 is 0.017751479289940832
- BLEU score of para 7 is 0.02727272727272727
- BLEU score of para 8 is 0.021857923497267763
- BLEU score of para 9 is 0.015217391304347823
- BLEU score of para 10 is 0.012882447665056364
