"""
modulo de rotinas do p2 no pipeline

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

status_usuarios=[]  

def processo_p2(crypto, signature, pos_us):
    # verificar se usuario out esta' online, pode ser um evento recebido por este
    if len(status_usuarios)>pos:
        if status_usuarios[pos_us]:
            if criptografia.verifica_assinatura(msg,signature,key[0]) :
                print()# comando inutil
                # envia para cliente out: crypto
                # deletar crypto, signature e pos_us, por questao de seguranca
            else:
                print()# comando inutil
                # envia para cliente out: "mensagem com integridade corrompida"
                # deletar crypto, signature e pos_us, por questao de seguranca
        else:
            print()# comando inutil
            # faz nada
    else:
        print()# comando inutil
        # faz nada

# definir uma funcao que recebe o status de usuarios
def recebe_status(s_us):
    status_usuarios = s_us


