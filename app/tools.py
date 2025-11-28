import json
from pathlib import Path
from app.utils import load_json, save_json

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "pedidos.json"

def load_pedidos():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def buscar_pedido(pedido_id: str):
    pedidos = load_pedidos()
    for p in pedidos:
        if p["pedido_id"] == pedido_id:
            return p
    return None

def cancelar_pedido(pedido_id: str) -> dict:
    pedidos = load_json("data/pedidos.json")
    
    for p in pedidos:
        if p["pedido_id"] == pedido_id:

            # regras simples de cancelamento
            if p["status"] in ["entregue", "cancelado"]:
                return {
                    "ok": False,
                    "motivo": f"Não é possível cancelar pedidos com status '{p['status']}'."
                }

            # atualizar o pedido
            p["status"] = "cancelado"

            # salvar no arquivo
            save_json("data/pedidos.json", pedidos)

            return {
                "ok": True,
                "mensagem": f"Pedido {pedido_id} cancelado com sucesso!",
                "pedido": p
            }

    return {"ok": False, "motivo": "Pedido não encontrado."}
