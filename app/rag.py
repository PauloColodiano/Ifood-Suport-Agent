import chromadb
from chromadb.config import Settings
from openai import OpenAI
   

client = OpenAI()

chroma_client = chromadb.PersistentClient(path="data/chroma")

collection = chroma_client.get_or_create_collection(
    name="ifood_docs",
    metadata={"hnsw:space": "cosine"},
)

def embed(text: str):
    res = client.embeddings.create(model="text-embedding-3-small", input=text)
    return res.data[0].embedding

def index_document(doc_id: str, text: str):
    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embed(text)]
    )

def search(query: str, top_k: int = 3):
    results = collection.query(
        query_embeddings=[embed(query)],
        n_results=top_k
    )
    return results
