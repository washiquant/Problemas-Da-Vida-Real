def faturamento_diario():

    """O objetivo deste final deste projeto, é fazer as comandas de pedidos, sejam guardadas pelos seus indices, e somada seus valores
    para resolver o problema de ir somando as comandas na calculadora e em um dado momento, aquela soma sumir e vc perder os valores somados
    """

    historico_entregas = {"Diária":40}
    while True :
        comanda = str(input("Qual o Numero da Comanda ? (Ou digite 'sair' para fechar)"))
        if comanda.lower() == 'sair' :
            break
        if comanda in historico_entregas :
            print("Essa comanda ja foi adicionada!Verifique os pedido")
            continue
        valores = int(input("Qual o valor do Pedido ?"))
        historico_entregas[comanda] = valores

        total = sum(historico_entregas.values())

        print(f"Estamos em {total}R$, Continua garoto!")
        with open("comandas.txt", 'a') as arquivo :
            linha_texto = (f"Comanda {comanda}: Valor {valores}\n")
            arquivo.write(linha_texto)


if __name__ == '__main__':
    faturamento_diario()
