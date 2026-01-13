from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

# Vector DB yükle
db = Chroma(
    persist_directory="db",
    embedding_function=OllamaEmbeddings(model="nomic-embed-text")
)

retriever = db.as_retriever(
    search_kwargs={"k": 10}
)


llm = Ollama(model="llama3.1")

prompt = PromptTemplate.from_template("""
Aşağıdaki metinlere dayanarak
sorunun cevabını çıkarım yaparak açıkla.

tek, net ve özet bir cevap üret.

- Listeleme yapma
- Gereksiz tekrar yapma

Eğer bilgi dolaylı anlatılmışsa,
bunu açıkça belirt.

{context}

Soru: {question}

Cevap:

""")



while True:
    question = input("Soru: ")

    docs = retriever.invoke(question)

    if not docs:
        print("Bu bilgi dokümanda yer almıyor.")
        continue

    context = "\n\n".join(d.page_content for d in docs)

    response = llm.invoke(
        prompt.format(context=context, question=question)
    )

    print("\n", response.strip())


