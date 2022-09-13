"""

modulo responsavel por encriptar a mensagem
o metodo de encriptacao e' o rsa, que e' por chave assimetrica

"""

import rsa

# tamanho da chave
nbits = 1024

# gera chaves criptograficas para o algoritmo rsa
def gera_chaves():
    return rsa.newkeys(nbits)

# encripta a mensagem
def encripta(msg,key):
    return rsa.encrypt(msg.encode(),key)

# decripta a mensagem
def decripta(msg,key):
    return (rsa.decrypt(msg,key)).decode()

# cria uma assinatura digital para a mensagem
def assinatura(msg,priv_key):
    return rsa.sign(msg.encode(),priv_key,'SHA-1')

def assinatura_b(msg,priv_key):
    return rsa.sign(msg,priv_key,'SHA-1')

# verifica se a assinatura corresponde a' mensagem
def verifica_assinatura(msg,sign,pub_key):
    try:
        rsa.verify(msg.encode(), sign, pub_key)
        return True
    except:
        return False

def verifica_assinatura_b(msg,sign,pub_key):
    try:
        rsa.verify(msg, sign, pub_key)
        return True
    except:
        return False
