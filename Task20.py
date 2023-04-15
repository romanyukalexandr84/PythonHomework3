dictionary = {1:"AEIOULNSTRАВЕИНОРСТ", 2:"DGДКЛМПУ", 3:"BCMPБГЁЬЯ", 
     4:"FHVWYЙЫ", 5:"KЖЗХЦЧ", 8:"JXШЭЮ", 10:"QZФЩЪ"}

word = input ("Введите слово: ")
word = word.upper()

price = 0

for (k,v) in dictionary.items():
    for i in range(len(word)):
        if word[i] in v:
            price+=k

print(f"Стоимость введенного слова = {price} очков")