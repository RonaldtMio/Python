letters = { 1:"AEIOULNSTRАВЕИНОРСТ",
            2:"DGДКЛМПУ",
            3:"BCMPБГЁЬЯ",
            4:"FHVWYЙЫ",
            5:"KЖЗХЦЧ",
            8:"JXШЭЮ",
            10:"QZФЩЪ"}

user_word = input("Введите слово: ").upper()
sum = 0
for i in user_word:
    for k, v in letters.items():
        if i in v:
            sum += k
print(f"Количество баллов за слово: {sum}")