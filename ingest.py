from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings


loader = PyPDFLoader("data/notes.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=120
)

chunks = splitter.split_documents(docs)

db = Chroma.from_documents(
    chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text"),
    persist_directory="db"
)

db.persist()
print("Indexleme tamamlandı")
print(docs[0].page_content[:500])

