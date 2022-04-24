import math


def input_int(prompt):
    inp = ""
    while type(inp) is not int:
        inp = input(prompt)

        try:
            inp = int(inp)
        except:
            continue

    return inp


def encrypt(msg):
    pass


def decrypt(msg):
    pass


while True:
    cmd = input("Möchten sie eine Nachricht verschlüsseln[v] oder entschlüssen[e]: [v/e]   ")
    if cmd.lower() == "v":
        print("Geben sie jetzt das Public-Key-Paar der Form (n, e) nacheinander ein")
        public_key = (input_int("n:    "), input_int("e:    "))
        plain = input_int("Geben sie ihre Nachricht ein (eine ganze Zahl):   ")
        cypher = (plain ** public_key[1]) % public_key[0]
        print("Ihre Nachricht wurde verschlüsselt:   " + str(cypher))
        print("Die Nachricht kann nur wieder entschlüsselt werden, wenn sie das richtige Private-Key-Paar angeben.")
        print("----------------------------->")

    elif cmd.lower() == "e":
        print("Sie können nur Nachrichten entschlüsseln, die mit ihrem Public-Key verschlüsselt wurden")
        print("Geben sie jetzt das passende Private-Key-Paar der Form (n, d) nacheinander ein")
        public_key = (input_int("n:    "), input_int("d:    "))
        cypher = input_int("Geben sie die verschlüsselte Nachricht ein (eine ganze Zahl):   ")
        plain = cypher ** public_key[1] % public_key[0]
        print("Ihre Nachricht wurde entschlüsselt:   " + str(plain))
        print("----------------------------->")


