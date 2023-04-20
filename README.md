# Fundamentos de Computação - Atividade Prática II

Este programa se trata de uma aplicação simples em Python que permite receber um ou mais URLs como argumento e retorna o status de cada website. Na figura abaixo temos a tela inicial do programa:

<img align="center" alt="Home" width="500" height="500" src="imagens\Print - 1.png">

# Funcionamento

## 1. Abrir arquivo ou adicionar texto

O programa permite que o usuário, clicando no botão "Abrir arquivo de texto", importe um arquivo .txt do seu computador, no qual cada linha deve ser a URL de um site. Ao pressionar o botão "Abrir arquivo de texto", irá abrir uma tela para seleção do arquivo .txt, assim como mostra a figura abaixo

<img align="center" alt="Home" width="1000" height="500" src="imagens\Print - 6.png">

Também existe a opção de digitar cada URL manualmente e clicar no botão "Adicionar na lista de sites", como ilustram as duas figuras abaixo:

Digitando a url do site:

<img align="center" alt="Home" width="500" height="500" src="imagens\Print - 2.png">

Adicionando o texto na lista:

<img align="center" alt="Home" width="500" height="500" src="imagens\Print - 3.png">

 É possível adicionar vários arquivos .txt e vários sites manualmente e cada adição vai sendo posicionada embaixo dentro da caixa de texto.

## 2. Testar a conexão 

Logo abaixo da caixa de texto localiza-se o botão "Testar conexão" que irá testar a conexão do site que estiver selecionado dentro da caixa de texto (basta clicar no site com o mouse). A figura abaixo ilustra a seleção de uma url para testar:

<img align="center" alt="Home" width="500" height="500" src="imagens\Print - 4.png">

Após pressionar o botão "Testar conexão", irá exibir a mensagem logo abaixo deste botão (se o site está online ou não), a caixa de mensagem vai ficar verde para o site online e vermelha caso contrário, facilitando a visualização. Isso pode ser observado na figura abaixo:

<img align="center" alt="Home" width="500" height="500" src="imagens\Print - 5.png">

Após testar a conexão ele irá remover o site da caixa de texto principal e armazenar o resultado em um arquivo final.txt. Em caso de ocorrer erros de digitação é possível selecionar o texto com erros dentro da caixa de texto e apertar o botão "Apagar texto"

## 3. Testar tudo, apagar e fechar

Por fim, o botão "Testar tudo, salvar e fechar" irá testar todos os sites que ainda estiverem na caixa de texto e acrescentar os resultados diretamente no arquivo final.txt (sem exibir na tela), o qual irá conter as informações de todos os sites que foram testados, tanto individualmente com o botão "testar conexão" quanto aos que sobraram na caixa de texto para teste posterior.

Após pressionar o botão "Testar tudo, salvar e fechar", irá aparecer na tela a mensagem, conforme figura abaixo:

<img align="center" alt="Home" width="500" height="500" src="imagens\Print - 8.png">

O resultado final armazenado no arquivo .txt ficará conforme a figura abaixo (repare que valores repetidos são salvos apenas uma vez):

<img align="center" alt="Home" width="700" height="500" src="imagens\Print - 9.png">

