# jogo_nim
AUTOR: Gabriel Costa Ferreira.

Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam alternadamente, retirando pelo menos 1 e no máximo m peças cada um. 
Quem tirar as últimas peças possíveis ganha o jogo.

Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.
O computador seguirá a estratégia vencedora descrita acima.

Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:
- Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa!"
- Caso contrário, o computador toma a inciativa de começar o jogo, declarando "Computador começa!"

Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. 
Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

função computador_escolhe_jogada: devolve um inteiro correspondente à próxima jogada do computador;

função usuario_escolhe_jogada: solicita que o jogador informe sua jogada e verifica se o valor informado é válido. 
Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.

função partida: solicita ao usuário que informe os valores de n e m e inicia o jogo, alternando entre jogadas do computador e do usuário 
(ou seja, chamadas às duas funções anteriores). 
A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam na mesa. 

função campeonato:  deve realizar três partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas e indicar o vencedor do campeonato. 
