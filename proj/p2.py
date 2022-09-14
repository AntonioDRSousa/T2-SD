"""
modulo de rotinas do p2 no pipeline

"""

import criptografia 
import script

def processo_p2(crypto, signature, us_in, us_out):
    # recebe para p1: signature, crypto, us_in, us_out
    if criptografia.verifica_assinatura_b(crypto,signature,key[0]) :
        # envia para cliente out: crypto
        t=script.clientes[us_in][us_out]
        script.clientes[us_in][us_out]=(t[0],(t[1]).append(crypto),t[2])
    else:
        # envia para cliente out: "mensagem com integridade comprometida"
        print("\n\n\n----------------------------")
        print("cliente "+str(pos_us))
        print("!!! Mensagem com Integridade Comprometida !!!")
        print("----------------------------\n\n\n")


