# 🛵 Controle de Faturamento para Entregadores

## 📝 O Problema
Ao longo do tempo trabalhando como motoboy, percebi que uma das dores de trabalhar com comandas e valores anotados em papéis era que, 
ao irmos somando esses valores na calculadora do celular, acontecia de sem querer fecharmos o aplicativo ou a bateria acabar, fazendo com que perdêssemos a nossa soma. 

O resultado disso era o pior cenário possível: **não tínhamos a mínima ideia de quanto havíamos faturado no dia**.

## 🚀 A Solução
Este script em Python veio para sanar esse problema. Ele funciona como uma calculadora inteligente que:
1. Pede o número da comanda (garantindo que você não insira a mesma taxa duas vezes por engano).
2. Calcula o faturamento acumulado em tempo real, mostrando o total atualizado a cada nova entrega.
3. Faz a **persistência dos dados**, salvando automaticamente cada corrida em um arquivo de texto (`comandas.txt`). Assim, mesmo que o programa feche ou o celular desligue, o seu histórico e o seu dinheiro estão salvos no disco rígido.

## 🛠️ Conceitos de Programação Aplicados
* **Estrutura de Repetição:** `while True` para manter o programa rodando durante todo o turno.
* **Controle de Fluxo:** `break` para fechar o caixa e `continue` para tratar erros e comandas duplicadas.
* **Estrutura de Dados:** Dicionários (`dict`) para vincular cada número de comanda ao seu respectivo valor.
* **Manipulação de Arquivos (I/O):** Uso do `with open` no modo `append ('a')` para gravar os dados de forma segura sem apagar o histórico anterior.
