# Projeto

O projeto e' um sistema de envio de emails simples.
A ideia é dividir em 3 pipelines em um sistema distribuido:

1. **p0**: recebe mensagem do usuário, busca o usuário receptor da mensagem, gera as chaves criptograficas, fornece a chave privada para o usuário a receber a mensagem, cria uma assinatura para a mensagem, envia a mensagem com a chave pública para o próximo estágio
2. **p1**: encripta com a chave pública a mensagem
3. **p2**: armazena a mensagem criptografada do usuário, quando o usuário a receber estiver online, envia a mensagem realizando a autenticação da assinatura, após o envio a mensagem é deletada

Nesse sistema a decriptação é realizada no ambiente local do usuário receptor. Tal medida visa aumentar a segurança
