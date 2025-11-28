import re

def detectar_intent(message: str):
    msg = message.lower()

    # Cancelamento
    if any(k in msg for k in ["cancelar", "cancela", "cancelamento"]):
        return "cancelar_pedido"

    # Reembolso
    if any(k in msg for k in ["reembolso", "reembolsar", "estorno"]):
        return "reembolso"

    # Atraso
    if any(k in msg for k in ["atraso", "demorando", "demorado", "não chegou", "nao chegou"]):
        return "pedido_atrasado"

    # Status / rastrear
    if any(k in msg for k in ["status", "rastrear", "acompanhar", "andamento"]):
        return "status_pedido"

    # Se mencionou número rastreamento por padrão
    if re.search(r"\b[pP]?(\d{1,9})\b", msg):
        return "status_pedido"

    return "info_geral"
