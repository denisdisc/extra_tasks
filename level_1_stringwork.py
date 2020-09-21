# Вывести последнюю букву в слове
word = 'Архангельск'
last_word = list(word)
print(last_word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'е', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
n = 0
for letter in word.lower():
    if letter in vowels:
        n += 1
print(n)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for target in sentence.split():
    print(target[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
m = 0
for target in sentence.split():
    m += len(target)
print(m/len(sentence.split()))
