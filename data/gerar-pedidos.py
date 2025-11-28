import json, random

users = ["Paulo", "Mariana", "João", "Ana", "Carlos", "Beatriz", "Rafael", "Juliana", "Felipe", "Camila"]
pratos = ["X-Burguer", "Pizza", "Salada", "Sushi", "Pastel", "Coxinha", "Lasanha", "Churrasco", "Taco", "Hambúrguer Vegano"]

pedidos = []

for i in range(1, 31):
    pedidos.append({
        "pedido_id": f"P{i:03}",
        "user": random.choice(users),
        "status": random.choice(["em_preparo", "saiu_para_entrega", "entregue", "pronto_para_entrega", "em_transporte" "cancelado", "reembolsado", "aguardando_pagamento"]),
        "itens": [
            {
                "nome": random.choice(pratos),
                "qtd": random.randint(1, 3)
            }
        ],
        "total": round(random.uniform(20, 80), 2)
    })

with open("pedidos_mock.json", "w") as f:
    json.dump(pedidos, f, indent=2)

print("Mock gerado!")
