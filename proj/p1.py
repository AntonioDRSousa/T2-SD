"""
modulo de rotinas do p1 no pipeline

"""

# pseudocodigo de "sistemas distribuidos"

"""

Evento Consumir(mensagem,nos_que_enviaram):
	// interpreta_mensagem pega a mensagem e transforma nos argumentos correspondente da funcao
	saida = procedimento(interpreta_mensagem(mensagem));
	envia(nos_que_enviaram,mensagem);

// permite a memoria compartilhada dentro do nó de processamento central	
procedimento(procedimento_correspondente, *entrada, *saida):
	enquanto True:
		adquirir_lock_entrada();
		Se *entrada != nulo:
			adquirir_lock_saida();
			*saida = procedimento_correspondente(entrada);
			*entrada = nulo;
			libera_lock_saida();
		libera_lock_entrada();


main:
	enquanto True:
		Se get_evento == Consumir:
			// o computador central produz threads para cada evento que receber de cada nó
			Thread(Consumir(mensagem,mps_que_envia));

"""

import criptografia
    

def processo_p1(msg,pub_key, signature, pos_us):
    crypto = criptografia.encripta(msg, pub_key)
    # envia para p2: signature, crypto, pos_us
    # deletar pub_key, por ser desnecessaria a partir de agora
    # deletar msg, por questao de seguranca

# definido na aplicacao principal os parametros
def processo_status_p1(status_usuarios):
    print()# comando inutil
    # envia para p1: status_usuarios com (status, pos)


