
#Даны два массива строк words1 и words2.

#Строка b является подмножеством строки a, если каждая буква в b встречается в строке a в том числе и в кратном количестве.

#Например, "wrr" является подмножеством "warrior", но не является подмножеством "world".
#Строка a из words1 является универсальной, если для каждой строки b из words2 b является подмножеством a.

#Возвращает массив всех универсальных строк в words1 Вы можете вернуть ответ в любом порядке.

#Пример 1:

#Вход: words1 = ["amazon", "apple", "facebook", "google", "leetcode"], words2 = ["e", "o"]Вывод: ["facebook", "google", "leetcode"].

words1 = ["amazon", "apple", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]

class Words():
    def __init__(self, words1, words2):
        self.words1=words1
        self.words2=words2

    
    def case(self):
        try:
            1 <= len(words1) and len(words2) <= 104
        except:
            print('Первое ограничение')
        try:
            for el in words1:
                1 <= len(el) 
            for el in words2:
                len(el) <= 10
        except:
            print('Второе ограничение')
        for el in words1:
            alphavit={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
            for letter in el: 
                if letter in alphavit:
                    pass
                else:
                    print('Третье ограничение')
                    break   
        if len(words1)==len(set(words1)):
            pass
        else:   
            return print('Четвертое ограничение')
        spisok=[]
        for el in words1:
            if all (letter in el for letter in words2):
                spisok.append(el)
        print(spisok)

raz=Words(words1, words2)
raz.case()


words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["l", "e"]

dva=Words(words1, words2)
dva.case()


#1 <= words1.length, words2.length <= 104
#1 <= words1[i].length, words2[i].length <= 10
#Слова1[i] и слова2[i] состоят только из строчных английских букв.
#Все строки words1 уникальны.
