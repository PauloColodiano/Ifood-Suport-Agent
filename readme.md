# 🍔 iFood Support Agent

Um agente inteligente de suporte ao cliente, construído do zero utilizando **LLMs**, **Function Calling**, **RAG (Retrieval-Augmented Generation)** e **FastAPI**, simulando operações reais de atendimento do iFood.

Este projeto foi desenvolvido para demonstrar habilidades práticas em:

* Engenharia com LLMs
* Construção de agentes inteligentes
* Integração entre IA + backend
* Uso de ferramentas (tools) via function calling
* RAG para recuperação de políticas internas
* Deploy e organização profissional de projeto
* Estrutura limpa e escalável

---

## 🚀 Features

### 🧠 **Agente com Function Calling**

O agente identifica a intenção do usuário e decide automaticamente quando:

* 🔍 Buscar pedido
* ❌ Cancelar pedido
* 📦 Consultar status
* ⏱️ Tratar atrasos
* 💸 Reembolsos
* 📚 Usar RAG ao invés de tools
* 💬 Gerar resposta natural ao cliente

### 🔧 **Ferramentas (tools)**

Implementadas manualmente, simulando operações reais do iFood:

| Tool              | Descrição                                  |
| ----------------- | ------------------------------------------ |
| `buscar_pedido`   | Recupera dados do pedido em `pedidos.json` |
| `cancelar_pedido` | Aplica regras reais de cancelamento        |
| `utils.load_json` | Carrega bancos mockados                    |
| `utils.save_json` | Persiste alterações                        |

### 📚 **RAG (ChromaDB + Embeddings)**

Usado para:

* Políticas de reembolso
* Políticas de atraso
* Políticas de cancelamento
* Normas internas

O agente combina **tools + RAG + LLM** para gerar respostas humanas e precisas.

### ⚙️ **API com FastAPI**

Endpoint principal:

```
POST /chat
{
  "message": "Quero saber o status do pedido P003"
}
```

## 📁 Estrutura do Projeto

```
ifood-support-agent/
├─ app/
│  ├─ api.py          # FastAPI + endpoint /chat
│  ├─ agent.py        # Orquestração principal do agente (RAG + tools + intents)
│  ├─ tools.py        # Implementações das ferramentas
│  ├─ intent.py       # Classificador de intenção
│  ├─ rag.py          # Indexação e busca dos documentos
│  ├─ utils.py        # load_json / save_json
│  └─ system_prompt.py (opcional)
│
├─ data/
│  ├─ pedidos.json
│  ├─ restaurantes.json (opcional)
│  └─ docs/
│      ├─ cancelamento.txt
│      ├─ reembolso.txt
│      └─ atrasos.txt
│
├─ ui/
│  └─ app.py          # Streamlit UI
│
├─ infra/
│  └─ Dockerfile
│
├─ requirements.txt
└─ README.md
```

---

## ▶️ Como Rodar

### 1. Criar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate    # Mac/Linux
.venv\Scripts\activate       # Windows
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Exportar chave OpenAI

```bash
export OPENAI_API_KEY="sua-chave"
```

### 4. Iniciar a API

```bash
uvicorn app.api:app --reload
```

### 5. Enviar uma requisição

```json
POST http://localhost:8000/chat
{
  "message": "Quero rastrear o pedido P003"
}
```

---

## 🧩 Exemplos

### 🔍 Buscar status

Entrada:

```
"meu pedido P003 está demorando"
```

Saída:

```
"O pedido P003 está pronto para entrega."
```

---

### ❌ Cancelar pedido

Entrada:

```
"cancela o pedido 7"
```

Saída:

```
"Não é possível cancelar pedidos já entregues."
```

---

### 📚 RAG (política de reembolso)

Entrada:

```
"como funciona o reembolso?"
```

Saída (baseado em políticas reais):

```
"Reembolsos são processados em até 7 dias úteis..."
```

---

## 🧠 Como o Agente Decide o Que Fazer?

O pipeline é:

```
Intent → Extrair ID → Tools ou RAG → LLM → Resposta final
```

Exemplo:

| Mensagem do usuário        | Intenção        | Ação do agente               |
| -------------------------- | --------------- | ---------------------------- |
| "cancelar pedido 5"        | cancelar_pedido | executa tool cancelar_pedido |
| "status do pedido 8"       | status_pedido   | busca tool buscar_pedido     |
| "como funciona reembolso"  | reembolso       | usa RAG                      |
| "meu pedido está atrasado" | pedido_atrasado | usa RAG                      |

---

## 🎯 Objetivo do Projeto


* habilidade em **construir agentes completos**
* uso de **OpenAI + Python + FastAPI**
* manipulação real de **function calling**
* implementação de **RAG** sem frameworks pesados
* pensamento de **produto + engenharia de IA**
* entrega rápida e limpa

---



## 👨‍💻 Autor

Projeto criado por **Paulo Colodiano** como parte de um portfólio técnico focado em IA aplicada ao iFood.

---

## ⭐ Contribuições

Pull requests são bem-vindos — especialmente melhorias no agente, novos tools e novos fluxos.

---

