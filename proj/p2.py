"""
modulo de rotinas do p2 no pipeline

"""

import criptografia 
import script

def processo_p2(crypto, signature, pos_us):
    # recebe para p1: signature, crypto, pos_us
    if criptografia.verifica_assinatura_b(crypto,signature,key[0]) :
        print()# comando inutil
        # envia para cliente out: crypto
    else:
        print()# comando inutil
        # envia para cliente out: "mensagem com integridade corrompida"


