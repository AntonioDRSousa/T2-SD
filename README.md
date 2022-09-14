Explicação da Ideia

O sistema foi feito com uma topologia de pipeline em 3 estágios:

p0: recebe mensagem do usuário, gera as chaves criptográficas, fornece a chave privada para os usuários a, enviar a mensagem com a chave pública e privada para o próximo estágio
p1: encripta com a chave pública a mensagem e cria uma assinatura para a mensagem
p2: armazena a mensagem criptografada do usuário, envia a mensagem realizando a autenticação da assinatura

O código script simula a ação de um cliente.
Nesse sistema usou-se como criptografia a criptografia RSA, devido a ser uma criptografia forte, na assinatura usou-se SHA-1.

