#Если задан массив целых чисел nums и целое число target, то верните индексы двух чисел так, чтобы их сумма равнялась target.

#Вы можете предположить, что каждый вход будет иметь ровно одно решение, и не можете использовать один и тот же элемент дважды.

#Ответы можно возвращать в любом порядке.

 
#Пример 1:

#Вход: nums = [2,7,11,15], target = 9
#Выход: [0,1]
#Пояснение: Поскольку nums[0] + nums[1] == 9, мы возвращаем [0, 1].

nums = [2,7,11,15]
target = 9

class Case: 

    def __init__(self, nums,target): 
        self.nums=nums
        self.target=target  

    def summa(self):
        nums_prosmotr = {} 
        for i, num in enumerate(nums): 
            vtor_num = target - num 
            if vtor_num in nums_prosmotr: 
                return print([nums_prosmotr[vtor_num], i])
            nums_prosmotr[num] = i 
        return None 
    
raz = Case(nums,target)
raz.summa()

nums = [3,2,4]
target = 6
dva = Case(nums, target)
dva.summa()

nums = [3,3]
target = 6
tri = Case(nums, target)
tri.summa()

