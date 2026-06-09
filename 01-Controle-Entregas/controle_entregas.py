import sqlite3

def faturamento_diario():

    """O objetivo deste final deste projeto, é fazer as comandas de pedidos, sejam guardadas pelos seus indices, e somada seus valores
    para resolver o problema de ir somando as comandas na calculadora e em um dado momento, aquela soma sumir e você perder os valores somados
    """
    conexao = sqlite3.connect("entregas.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT SUM(valor_pedido) FROM comandas WHERE data_registro = CURRENT_DATE")
    resultado = cursor.fetchone()[0]
    total_acumulado_do_dia = resultado if resultado is not None else 0
    faturamento_atual = 40 + total_acumulado_do_dia
    historico_entregas = {}
    # Criamos um dicionário vazio apenas para travar comandas repetidas na mesma sessão
    historico_entregas = {}
    cursor.execute("""
CREATE TABLE IF NOT EXISTS comandas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_registro TEXT  DEFAULT CURRENT_DATE,
    numero_comanda TEXT,
    valor_pedido REAL
)
""")
    while True :
        comanda = str(input("Qual o Numero da Comanda ? (Ou digite 'sair' para fechar)"))
        if comanda.lower() == 'sair' :
            break
        if comanda in historico_entregas :
            print("Essa comanda ja foi adicionada!Verifique os pedido")
            continue
        valores = int(input("Qual o valor do Pedido ?"))
        historico_entregas[comanda] = valores
        faturamento_atual += valores
        print(f"Estamos em {faturamento_atual}R$, Continua garoto!")
        # 1. Preparar a ordem de inserção de dados
        cursor.execute("INSERT INTO comandas (numero_comanda, valor_pedido) VALUES (?, ?)", (comanda, valores))

        conexao.commit()

if __name__ == '__main__':
    faturamento_diario()
