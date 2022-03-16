def criptoC(frase):
    tradutor = " "
    for letra in frase:
        if letra in "Aa":
            tradutor = tradutor + "@"
        elif letra in "Bb":
            tradutor = tradutor + ";"
        elif letra in "Cc":
            tradutor = tradutor + "'"
        elif letra in "Dd":
            tradutor = tradutor + "$"
        elif letra in "Ee":
            tradutor = tradutor + "3"
        elif letra in "Ff":
            tradutor = tradutor + "_"
        elif letra in "Gg":
            tradutor = tradutor + "&"
        elif letra in "Hh":
            tradutor = tradutor + "-"
        elif letra in "Ii":
            tradutor = tradutor + "8"
        elif letra in "Jj":
            tradutor = tradutor + "+"
        elif letra in "Kk":
            tradutor = tradutor + "("
        elif letra in "Ll":
            tradutor = tradutor + ")"
        elif letra in "Mm":
            tradutor = tradutor + "?"
        elif letra in "Nn":
            tradutor = tradutor + "!"
        elif letra in "Oo":
            tradutor = tradutor + "9"
        elif letra in "Pp":
            tradutor = tradutor + "0"
        elif letra in "Qq":
            tradutor = tradutor + "1"
        elif letra in "Rr":
            tradutor = tradutor + "4"
        elif letra in "Ss":
            tradutor = tradutor + "#"
        elif letra in "Tt":
            tradutor = tradutor + "5"
        elif letra in "Uu":
            tradutor = tradutor + "7"
        elif letra in "Vv":
            tradutor = tradutor + ":"
        elif letra in "Ww":
            tradutor = tradutor + "2"
        elif letra in "Xx":
            tradutor = tradutor + '"'
        elif letra in "Yy":
            tradutor = tradutor + "6"
        elif letra in "Zz":
            tradutor = tradutor + "*"
        elif letra in "Çç":
            tradutor = tradutor + "/"
        else:
            tradutor = tradutor + letra
    return tradutor


print(criptoC(input("Digite sua Frase:")))
