"""
modulo de rotinas do p0 no pipeline

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

# busca usuario a receber mensagem por nome num vetor com os usuarios
# retorna a posicao do elemento
def busca_usuario(us,usuarios):
    for i in range(0,len(usuarios)):
        if usuarios[i]==us:
            return i
    return -1
    

def processo_envio_p0(msg,us_in,us_out):
    pos = busca_usuario(us_out,usuarios)
    if pos==(-1):
        print()# comando inutil
        # envia informacao de ausencia de usuario para o us_in
    else:
        key = criptografia.gera_chaves()
        priv_key = key[1]
        pub_key = key[0]
        signature = criptografia.assinatura(msg,priv_key)
        # envia para p1: pub_key, signature, msg, pos(precisa para saber usuario a receber)
        # envia para cliente in e cliente out: priv_key
        # deletar priv_key, por questao de seguranca

# definido na aplicacao principal os parametros
def processo_status_p0(status_usuarios):
    print()# comando inutil
    # envia para p1: status_usuarios com (status, pos)



