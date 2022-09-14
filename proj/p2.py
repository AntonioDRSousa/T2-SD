"""
modulo de rotinas do p2 no pipeline

"""

import criptografia 
from clientes import clientes

def processo_p2(crypto, signature, pub_key, us_in, us_out):
    # recebe de p1: crypto, signature, pub_key, us_in, us_out
    if criptografia.verifica_assinatura_b(crypto, signature, pub_key) :
        # envia para cliente out: crypto
        t = clientes[us_in][us_out]
        clientes[us_in][us_out] = (t[0], t[1].append(crypto), t[2])
        return clientes[us_in][us_out]
    else:
        # envia para cliente out: "mensagem com integridade comprometida"
        print("\n\n\n----------------------------")
        print("cliente "+str(pos_us))
        print("!!! Mensagem com Integridade Comprometida !!!")
        print("----------------------------\n\n\n")


