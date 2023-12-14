alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п",
             "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
#гронсфельд шифр

a = input("Введите слово: ").lower()
b = input("Введите ключ: ")
#а = АБВГДЕЁ = 7 символов
#b = 12      = 2 символа
newA = ""
if len(a) >= len(b):
    c = len(a) - len(b)
    for i in range(c):
        ii = i
        if(ii>len(b)):
            ii = 0
        b += b[ii]

    for i in range(len(b)):
        #0 1 2 3 4 5...
        newAindex = alphabet.index(a[i])
        if newAindex + int(b[i]) > 32:
            newAindex = 33 - alphabet.index(a[i])
            newAindex = int(b[i]) - newAindex
        else:
            newAindex += int(b[i])
        newA += alphabet[newAindex]
    print("Зашифрованный текст: " + newA)
    newA = ""
    for i in range(len(b)):
        #0 1 2 3 4 5...
        newAindex = alphabet.index(a[i])
        if newAindex - int(b[i]) < 0:
            newAindex = 33
            newAindex = newAindex - int(b[i])
        else:
            newAindex -= int(b[i])
        newA += alphabet[newAindex]
    print("Расшифрованный текст: " + newA)

elif len(a) < len(b):
    print("Введите ключ короче чем текст!")