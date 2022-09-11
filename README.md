# T2-SD
Segundo Trabalho da disciplina de Sistemas Distribuídos do curso de Graduação em Ciência da Computação da UERJ

Ideia = serviço de emails simples pelo prompt de comando

PIPELINE

p0           ->                  p1                ->         p2
criptografia -> checksum(autenticação da mensagem) -> decriptografia

Seja um cliente A e um cliente B
Cada cliente insere loga com o seu nome
Cada cliente possui 3 opções:
  1 - sair da aplicação
  2 - listar emails recebidos
  3 - enviar um email
  
 (1) é trivial
 (2) listamos todos os emails
 (3) é inserido o nome do cliente para o qual será enviado o email, o assunto do email e o conteudo da mensagem
 
Vamos analisar um envio de um email de um cliente A para um cliente B.
1 - o cliente A envia um email que passa pelo nó da criptografia, tendo a mensagem criptografada
2 - após a criptografia, a mensagem passa por um checksum, onde é autenticada
3 - a mensagem aguarda um evento de leitura por parte do cliente B, em caso o cliente B decida ler o email especifico, a mensagem é decriptada

A mensagem chega em p0 e é colocada numa fila, quando é processada é armezenada criptografada
A mensagem é armazenada em p2 de modo criptografado, só sendo decriptada com a solicitação do cliente B

Tais medidas visam a segurança
