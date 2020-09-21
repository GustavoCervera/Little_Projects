def rotate_word(word,rot):
    nova = ""
    for letter in word:
        num = ord(letter)
        new = num + rot
        tes = chr(new)
        nova = nova + tes
    return nova

word = input("Digite uma string: ")
rot  = int(input("Digite o numero de rotacao: "))

ans = rotate_word(word,rot)

print(ans)
