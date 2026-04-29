import random
lista =  []
def negativ(nums):
    if nums < 0: 
        return True
    else:
        return False



for num in range(100):
    num = random.randint(-50, 50)
    if negativ(num) is True:
        lista.append(num)

print(f" A generált számok között {len(lista)} negatív szerepelt")



