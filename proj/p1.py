"""
modulo de rotinas do p1 no pipeline

"""

import criptografia   

def processo_p1(msg,pub_key, priv_key, us_in, us_out):
    # recebe de p0: pub_key, priv_key, msg, us_in, us_out
    crypto = criptografia.encripta(msg, pub_key)
    signature = criptografia.assinatura_b(crypto,priv_key)
    # envia para p2: signature, crypto, us_in, us_out
    return crypto, signature, us_in, us_out



