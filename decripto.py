def criptoD(frase):
    tradutor = " "
    for letra in frase:
        if letra in "@":
            tradutor = tradutor + "a"
        elif letra in ";":
            tradutor = tradutor + "b"
        elif letra in "'":
            tradutor = tradutor + "c"
        elif letra in "$":
            tradutor = tradutor + "d"
        elif letra in "3":
            tradutor = tradutor + "e"
        elif letra in "_":
            tradutor = tradutor + "f"
        elif letra in "&":
            tradutor = tradutor + "g"
        elif letra in "-":
            tradutor = tradutor + "h"
        elif letra in "8":
            tradutor = tradutor + "i"
        elif letra in "+":
            tradutor = tradutor + "j"
        elif letra in "(":
            tradutor = tradutor + "k"
        elif letra in ")":
            tradutor = tradutor + "l"
        elif letra in "?":
            tradutor = tradutor + "m"
        elif letra in "!":
            tradutor = tradutor + "n"
        elif letra in "9":
            tradutor = tradutor + "o"
        elif letra in "0":
            tradutor = tradutor + "p"
        elif letra in "1":
            tradutor = tradutor + "q"
        elif letra in "4":
            tradutor = tradutor + "r"
        elif letra in "#":
            tradutor = tradutor + "s"
        elif letra in "5":
            tradutor = tradutor + "t"
        elif letra in "7":
            tradutor = tradutor + "u"
        elif letra in ":":
            tradutor = tradutor + "v"
        elif letra in "2":
            tradutor = tradutor + "w"
        elif letra in '"':
            tradutor = tradutor + 'x'
        elif letra in "6":
            tradutor = tradutor + "y"
        elif letra in "*":
            tradutor = tradutor + "z"
        elif letra in "/":
            tradutor = tradutor + "ç"
        else:
            tradutor = tradutor + letra
    return tradutor


print(criptoD(input("Digite sua Frase:")))
