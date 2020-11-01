#  Copyright (c) 2020.
#  This code was designed and created by TH3R4VEN, its use is encouraged for academic and professional purposes.
#  I am not responsible for improper or illegal uses
#  Follow me on GitHub: https://github.com/th3r4ven

import random
import hashlib

g = random.randint(1, 10000)  # Qualquer numero inteiro (PUBLICO)
p = 13  # Pode ser qualquer numero, mas numeros primos fornecem mais segurança

a = random.randint(1, 10000)  # Numero secreto pra gerar a chave privada (NAO COMPARTILHAR) (PRIVATE KEY)
b = random.randint(1, 10000)  # Numero secreto pra gerar a chave privada (NAO COMPARTILHAR) (PRIVATE KEY)

A = (g**a) % p  # Gera a chave publica do usuario A, usuario B terá acesso a esse valor A
B = (g**b) % p  # Gera a chave publica do usuario B, usuario A terá acesso a esse valor B

print("Numeros compartilhados: g: " + str(g) + " p: " + str(p))

# Calculo das hashes com as chaves privadas com chaves publicas

keyA = (B**a) % p
keyB = (A**b) % p

print("Chaves privadas usuario 1: " + str(a))
print("Chaves publicas usuario 1: " + str(A))
print("Hashes de criptografia do usuario 1: " + str(hashlib.sha256(str(keyA).encode()).hexdigest()))
print("\n==================================================================================================================\n")
print("Chaves privadas usuario 2: " + str(b))
print("Chaves publicas usuario 2: " + str(B))
print("Hashes de criptografia do usuario 2: " + str(hashlib.sha256(str(keyB).encode()).hexdigest()))
