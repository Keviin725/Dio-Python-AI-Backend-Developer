usuario = {"nome": "João", "cpf": "123.456.789-00"}
conta = {"usuario": usuario, "saldo": 0, "depositos": [], "saques": []}

def deposito(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        conta["depositos"].append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor de depósito inválido.")

def saque(conta, valor):
    if valor <= 0:
        print("Valor de saque inválido.")
        return
    if len(conta["saques"]) >= 3:
        print("Limite diário de saques atingido.")
        return
    if valor > 500:
        print("Limite máximo por saque é de R$ 500.00.")
        return
    if conta["saldo"] < valor:
        print("Saldo insuficiente para saque.")
        return

    conta["saldo"] -= valor
    conta["saques"].append(valor)
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def extrato(conta):
    if not conta["depositos"] and not conta["saques"]:
        print("Não foram realizadas movimentações.")
        return

    print("Extrato:")
    for deposito in conta["depositos"]:
        print(f"Depósito: R$ {deposito:.2f}")
    for saque in conta["saques"]:
        print(f"Saque: R$ {saque:.2f}")

    print(f"Saldo atual: R$ {conta['saldo']:.2f}")


# Exemplo de uso do sistema:
deposito(conta, 1000)
saque(conta, 300)
saque(conta, 200)
saque(conta, 600)  # Tentando sacar mais do que o limite permitido
extrato(conta)
