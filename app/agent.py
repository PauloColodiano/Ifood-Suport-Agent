import re
from openai import AsyncOpenAI

from app.tools import buscar_pedido, cancelar_pedido
from app.rag import search
from app.intent import detectar_intent
from app.system_prompt import SYSTEM_PROMPT

# Cliente OpenAI
client = AsyncOpenAI()

async def run_agent(message: str):

    intent = detectar_intent(message)

    # Extrair ID do pedido
    
    match = re.search(r"[pP]?\s?(\d{1,9})", message)
    pedido_id = match.group(1) if match else None

    if pedido_id:
        pedido_id = pedido_id.strip()
        pedido_id = pedido_id.zfill(3)      
        pedido_id = f"P{pedido_id}"         



    tool_result = None

    # CANCELAR PEDIDO
   
    if intent == "cancelar_pedido":
        if not pedido_id:
            return "Para cancelar o pedido, preciso do número. Pode me informar?"

        tool_result = cancelar_pedido(pedido_id)
        return str(tool_result)

    # STATUS / RASTREIO DE PEDIDO
  
    if intent == "status_pedido":
        if not pedido_id:
            return "Para rastrear ou verificar o status, preciso do número do pedido."

        tool_result = buscar_pedido(pedido_id)

        if tool_result is None:
            return f"Não encontrei nenhum pedido com o ID {pedido_id}."

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message},
            {
                "role": "assistant",
                "content": f"[RESULTADO DA TOOL buscar_pedido]: {tool_result}"
            }
        ]

        completion = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        return completion.choices[0].message.content


    # REEMBOLSO / ATRASO RAG

    if intent in ["reembolso", "pedido_atrasado"]:
        rag = search(message)
        docs = rag.get("documents", [[]])[0]
        context = "\n\n".join(docs) if docs else ""

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message},
            {"role": "assistant", "content": f"[CONHECIMENTO RAG]:\n{context}"}
        ]

        completion = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        return completion.choices[0].message.content

==
    # OUTROS ASSUNTOS RAG

    rag = search(message)
    docs = rag.get("documents", [[]])[0]
    context = "\n\n".join(docs) if docs else ""

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": message},
        {"role": "assistant", "content": f"[CONHECIMENTO RAG]:\n{context}"}
    ]

    completion = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return completion.choices[0].message.content
