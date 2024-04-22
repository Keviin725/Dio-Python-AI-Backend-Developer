saldo = 0
depositos = []
saques = []

def deposito(valor):
    global saldo
    if valor > 0:
        saldo += valor
        depositos.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor de depósito inválido.")

def saque(valor):
    global saldo
    if valor <= 0:
        print("Valor de saque inválido.")
        return
    if len(saques) >= 3:
        print("Limite diário de saques atingido.")
        return
    if valor > 500:
        print("Limite máximo por saque é de R$ 500.00.")
        return
    if saldo < valor:
        print("Saldo insuficiente para saque.")
        return

    saldo -= valor
    saques.append(valor)
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def extrato():
    global saldo
    if not depositos and not saques:
        print("Não foram realizadas movimentações.")
        return

    print("Extrato:")
    for deposito in depositos:
        print(f"Depósito: R$ {deposito:.2f}")
    for saque in saques:
        print(f"Saque: R$ {saque:.2f}")

    print(f"Saldo atual: R$ {saldo:.2f}")

# Exemplo de uso do sistema:
deposito(1000)
saque(300)
saque(200)
saque(600)  # Tentando sacar mais do que o limite permitido
extrato()
