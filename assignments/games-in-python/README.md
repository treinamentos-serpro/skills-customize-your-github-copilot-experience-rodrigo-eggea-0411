
# 📘 Atividade: Jogo da Forca em Python

## 🎯 Objetivo

Pratique strings, listas, condicionais, loops e entrada de dados criando um jogo da Forca. O jogador deverá adivinhar uma palavra escolhida aleatoriamente antes de esgotar as tentativas incorretas.

## 📝 Tarefas

### 🛠️ Preparar a palavra e os palpites

#### Descrição
Use a lista de palavras do código inicial para escolher uma palavra secreta e implemente a leitura dos palpites do jogador. Mostre as letras já descobertas e use espaços reservados para as letras que ainda faltam.

#### Requisitos
O programa concluído deve:

- Selecionar uma palavra aleatoriamente da lista fornecida.
- Começar sem letras descobertas e exibir o progresso no formato `_ _ _`.
- Aceitar um palpite de letra por vez e revelar todas as ocorrências corretas dessa letra.
- Atualizar o progresso sem ocultar letras que já foram descobertas.

### 🛠️ Controlar o andamento da partida

#### Descrição
Complete o loop principal para contabilizar palpites incorretos e encerrar a partida quando o jogador vencer ou ficar sem tentativas.

#### Requisitos
O programa concluído deve:

- Limitar a quantidade de palpites incorretos a seis e informar quantas tentativas restam.
- Não descontar tentativas por letras repetidas ou entradas que não sejam uma única letra.
- Encerrar a partida quando todas as letras da palavra forem descobertas ou as tentativas acabarem.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra secreta.