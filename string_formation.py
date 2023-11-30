#Форматирование строк

sentence = input('Enter your sentence of 2 words: ')
sentence_split=sentence.split()
first_word=sentence_split[0]  
second_word=sentence_split[1]
first_word,second_word=second_word,first_word
if len(sentence_split) !=2:
    print('You entered a lot of words')
else:
    if second_word.isalpha() and first_word.isalpha() == False:
        print('You entered more than just')
    else:
        print('Final sentence: !{} ! {}!'.format(first_word, second_word))
        print('Final sentence: !%s ! %s!'%(first_word,second_word))
        print('Final sentence: !{0} ! {1}!'.format(first_word,second_word))
        print(f'Final sentence: !{first_word} ! {second_word}!')


