"""
Este modulo e' exclusivamente de testes
Aqui sao testados aspectos criptograficos da aplicacao

"""

import criptografia
print(criptografia.nbits)

#msg = str(input("msg = "))
msg="banana"

key = criptografia.gera_chaves()
crypto = criptografia.encripta(msg, key[0])
signature = criptografia.assinatura(msg,key[1])
decrypt = criptografia.decripta(crypto, key[1])

print("\n----------------------------------")
print("Chaves")
print("----------------------------------\n")
print(key)
print("\n----------------------------------\n")
print("\n----------------------------------")
print("Mensagem Encriptada")
print("----------------------------------\n")
print(crypto)
print("\n----------------------------------\n")
print("\n----------------------------------")
print("Assinatura")
print("----------------------------------\n")
print(signature)
print("\n----------------------------------\n")
print("\n----------------------------------")
print("Verificacao de Assinatura")
print("----------------------------------\n")
print(criptografia.verifica_assinatura(msg,signature,key[0]))
print("\n----------------------------------\n")
print("\n----------------------------------\n")
print("Mensagem Decriptada")
print("----------------------------------\n")
print(decrypt)
print("\n----------------------------------\n")
#print(criptografia.verifica_assinatura(crypto,signature,key[0]))
print(type(crypto))
signature = criptografia.assinatura_b(crypto,key[1])
print(criptografia.verifica_assinatura_b(crypto,signature,key[0]))
