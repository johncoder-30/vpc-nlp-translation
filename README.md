# Aug 2021 - Venmurasu Programming Contest 


Stage-1: Building Parallel Dataset

 - We looped through the folder containing 20 paragraphs of text file in both english and tamil.
 - read the individual text file separated it by full stop, then used regex to remove items in brackets.
 - the edited line was written line by line seperated by newline.
 - next paragraph is separated by an empty line
 - english paragraphs were written in english text file and tamil in tamil text file
 - the code we used for this is under data folder named data_preprocessing.py
 - then we manually corrected one to many and many to one statements
 - the tamil text is in file tam_equalized.txt with its equal english line in elg_equalized.txt under data folder

Stage-2: Running a Neural Machine Translation Model

- We fed the tamil data(tam_equalized.txt) to AI4Bharat in colab(https://github.com/AI4Bharat/indicTrans#using-the-model-for-translating-any-input) and got the respective translated english sentences
- the code we used for this is under translations folder named AI4Bharat colab code.py
- the translated sentences are in translated.txt file under translations floder  

Stage-3: Computing the scores of translation

- Then for BLEU score we used the NLTK library and passed the english translated sentences(translated.txt)and the english sentences(eng_equalized.txt)
-  the code we used for this is under evaluation folder named bleu_score.py

Stage-4: (Bonus points) Compare the model with other services

- Then using this library (https://github.com/UlionTse/translators) we translated the tamil sentences(tam_equalized.txt)
- the translated sentences are under translation folder named ulison translate.txt
- then calculated the BLEU scores using the same NLTK library by passing the translated sentence(ulison translate.txt) and it's english sentence(eng_equalized.txt)
- the code we used for this is under evaluation folder named bleu_score.py


### BLEU score computation for translated sentence using AI4BHARAT Model
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

### BLEU score computation for translated sentence using UlionTse library
- BLEU score of para 1 is 0.011363636363636359
- BLEU score of para 2 is 0.005181347150259067
- BLEU score of para 3 is 0.021739130434782608
- BLEU score of para 4 is 0.002881844380403458
- BLEU score of para 5 is 0.048701298701298704
- BLEU score of para 6 is 0.017751479289940832
- BLEU score of para 7 is 0.02727272727272727
- BLEU score of para 8 is 0.021857923497267763
- BLEU score of para 9 is 0.015217391304347823
- BLEU score of para 10 is 0.012882447665056364

### BLEU score comparision
![score_comparision](https://user-images.githubusercontent.com/71711641/132689364-369a9f7a-8369-408a-9fd7-336fc1ff18e8.jpeg)
