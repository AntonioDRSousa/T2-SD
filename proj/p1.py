"""
modulo de rotinas do p1 no pipeline

"""

import criptografia   

def processo_p1(msg,pub_key, signature, pos_us):
    crypto = criptografia.encripta(msg, pub_key)
    signature = criptografia.assinatura_b(crypto,priv_key)
    # recebe de p0: pub_key, msg, pos
    # envia para p2: signature, crypto, pos_us



