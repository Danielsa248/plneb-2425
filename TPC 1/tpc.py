# Exercício 1
def reverse_string(string):
    string = string[::-1]

    #string = ''.join(reversed(string))

    return string


# Exercício 2
def count_a_A(string):
    count_a = 0
    count_A = 0

    for char in string:
        if char == 'a':
            count_a += 1
        elif char == 'A':
            count_A += 1

    print(f'Número de a = {count_a}, Número de A = {count_A}')


# Exercício 3
def count_vowels(string):
    vowels = ['a', 'á', 'à', 'â', 'ã',
              'e', 'é', 'è', 'ê',
              'i', 'í', 'ì', 'î',
              'o', 'ó', 'ò', 'ô', 'õ',
              'u', 'ú', 'ù', 'û']
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1

    return count


# Exercício 4
def convert_lower(string):
    string = string.lower()
    return string


# Exercício 5
def convert_upper(string):
    string = string.upper()
    return string


# Exercício 6
def check_capicua(string):
    string2 = string[::-1]

    print("String 1 ---> ", string)
    print("String 2 ---> ", string2)

    if string == string2:
        return True
    else:
        return False


# Exercício 7
def check_balance(s1, s2):
    balance = True

    for char in s1:
        if char not in s2:
            balance = False

    return balance


# Exercício 8
def count_s1(s1, s2):
    count = 0
    i = 0
    while i <= (len(s2) - len(s1)):
        if s1 == s2[i:i + len(s1)]:
            count += 1

        i += 1

    return count


# Exercício 9
def check_anagrama(s1, s2):
    anagrama = True

    if sorted(s1) != sorted(s2):
        anagrama = False

    return anagrama


# Exercício 10
def tabela_anagrama(lista):
    tabela = {}

    for palavra in lista:
        key = ''.join(sorted(palavra))

        if key in tabela:
            tabela[key].append(palavra)

        else:
            tabela[key] = [palavra]

    return tabela



if __name__ == "__main__":
    lista = ["puer", "amor", "roma", "ova", "lago", "peru", "galo", "avo", "arroz"]

    print("Exercício 1")
    print(reverse_string(input("Digite uma palavra: ")))
    
    print("\nExercício 2")
    count_a_A(input("Digite uma palavra: "))
    
    print("\nExercício 3")
    print(count_vowels(input("Digite uma palavra: ")))
    
    print("\nExercício 4")
    print(convert_lower(input("Digite uma palavra: ")))
    
    print("\nExercício 5")
    print(convert_upper(input("Digite uma palavra: ")))
    
    print("\nExercício 6")
    print(check_capicua(input("Digite uma palavra: ")))
    
    print("\nExercício 7")
    print(check_balance(input("Digite uma palavra: "), input("Digite outra palavra: ")))
    
    print("\nExercício 8")
    print(count_s1(input("Digite uma palavra: "), input("Digite outra palavra: ")))

    print("\nExercício 9")
    print(check_anagrama(input("Digite uma palavra: "), input("Digite outra palavra: ")))

    print("\nExercício 10")
    print(tabela_anagrama(lista))

