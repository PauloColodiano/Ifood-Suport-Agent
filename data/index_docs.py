from app.rag import index_document

docs = {
    "cancelamento": open("data/docs/politicas.txt").read(),
    "reembolso": open("data/docs/reembolso.txt").read(),
    "atrasos": open("data/docs/atrasos.txt").read()
}

for doc_id, text in docs.items():
    index_document(doc_id, text)

print("Documentos indexados!")
