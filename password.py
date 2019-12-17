import random

def generatePassword():
    letters = "abcdefghijklmnopqrstvuxyzåäö"
    lettersCaps = "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
    numbers = "0123456789"
    spec = "!#%&=+-_*@$?"

    choices = list("32211000")

    for i in range(1, 100):
        password = ""

        random.shuffle(choices)
        randomChoices = ''.join(choices)

        for choice in randomChoices:
            if choice == "0":
                password += letters[random.randint(0, len(letters) - 1)]
            elif choice == "1":
                password += lettersCaps[random.randint(0, len(lettersCaps) - 1)]
            elif choice == "2":
                password += numbers[random.randint(0, len(numbers) - 1)]
            elif choice == "3":
                password += spec[random.randint(0, len(spec) - 1)]

    return password

passwd = generatePassword()

print(passwd)