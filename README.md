# RAG-PDF-READER
PDF RAG (Retrieval-Augmented Generation) Projesi
================================================

Bu proje, büyük ve karmaşık PDF dokümanları (kitaplar, teknik dokümantasyonlar, akademik metinler vb.) üzerinde
anlamsal arama ve soru–cevap yapabilen bir RAG (Retrieval-Augmented Generation) sistemidir.

Klasik PDF aramasının (Ctrl+F) ötesine geçerek:
- kelime değil anlam arar
- farklı bölümlere dağılmış bilgileri birleştirir
- kullanıcıya tek ve tutarlı bir cevap üretir

Proje tamamen **lokal** çalışır ve **API key gerektirmez**.

------------------------------------------------
PROJECT STRUCTURE / PROJE YAPISI
------------------------------------------------

yeni_rag_projesi/
│
├── ingest.py        -> PDF’i okuyup embedding ve vector database oluşturan script
├── query.py         -> Soru–cevap arayüzü (terminalden çalışır)
├── data/            -> PDF dosyalarının bulunduğu klasör
├── chroma_db/       -> Oluşturulan vektör veritabanı (otomatik oluşur)
├── rag-env/         -> Python sanal ortamı
└── README.txt

------------------------------------------------
SİSTEM GEREKSİNİMLERİ
------------------------------------------------

- macOS / Linux / Windows
- Python 3.11.x (önerilen)
- En az 8 GB RAM
- Ollama (lokal LLM için)

------------------------------------------------
KURULUM ADIMLARI
------------------------------------------------

1) Python 3.11 Kurulumu

Python sürümünü kontrol edin:

python3.11 --version

Eğer Python 3.11 kurulu değilse:
macOS için Homebrew ile:

brew install python@3.11

------------------------------------------------

2) Projeyi Klonlayın veya İndirin

git clone <repo_url>
cd yeni_rag_projesi

------------------------------------------------

3) Sanal Ortam Oluşturma

python3.11 -m venv rag-env
source rag-env/bin/activate

Aktif olduğunda terminal başında (rag-env) görünür.

------------------------------------------------

4) Gerekli Paketlerin Kurulumu

pip install --upgrade pip
pip install langchain langchain-community chromadb pypdf ollama

------------------------------------------------

5) Ollama Kurulumu ve Model İndirme

https://ollama.com adresinden Ollama’yı kurun.

Model indirin:

ollama pull llama3.1:8b

Test edin:

ollama run llama3.1:8b

------------------------------------------------
PDF HAZIRLAMA
------------------------------------------------

- PDF dosyanızı data/ klasörü içine koyun
- Sadece metin içeren PDF’ler önerilir
- Scan PDF’ler için OCR gerekebilir

------------------------------------------------
INGEST (PDF’İ İŞLEME)
------------------------------------------------

Bu adım PDF’i okuyup vektör veritabanını oluşturur.

python ingest.py

Bu işlem:
- PDF’i parçalara böler
- Embedding üretir
- ChromaDB’ye kaydeder

⚠️ PDF değiştiğinde BU ADIM TEKRAR ÇALIŞTIRILMALIDIR.

------------------------------------------------
QUERY (SORU–CEVAP)
------------------------------------------------

PDF işlendiğinde soru sormaya başlayabilirsiniz:

python query.py

Terminalde:

Soru:
> Evrenin yaşı nedir?

Sistem, PDF içeriğine dayanarak tek bir cevap üretir.

------------------------------------------------
PDF ARAMADAN FARKI
------------------------------------------------

PDF Arama:
- Kelime bazlı
- Aynı ifade yoksa sonuç yok
- Manuel okuma gerekir

Bu Proje:
- Anlam bazlı
- Farklı bölümlerden bilgi toplar
- Tek cevap üretir

------------------------------------------------
BİLİNEN SINIRLAMALAR
------------------------------------------------

- Scan PDF’ler OCR gerektirir
- Çok büyük modeller yüksek RAM ister
- Yanıtlar sadece PDF içeriğine dayanır

Eğer bilgi PDF’te yoksa sistem açıkça belirtir.

------------------------------------------------
AMAÇ
------------------------------------------------

Bu proje, dokümanlarla konuşabilen yapay zekâ sistemlerinin temelini göstermek için geliştirilmiştir.
Kitaplar, teknik dokümanlar ve bilgi tabanları için uygundur.

------------------------------------------------

PDF RAG (Retrieval-Augmented Generation) Project
================================================

This project is a Retrieval-Augmented Generation (RAG) system that enables semantic search and
question–answering over large PDF documents.

It runs fully locally and does not require any API keys.

------------------------------------------------
HOW TO RUN
------------------------------------------------

1) Install Python 3.11
2) Create virtual environment
3) Install dependencies
4) Install and run Ollama
5) Place PDF into data/
6) Run ingest.py
7) Run query.py
8) Ask questions in terminal

------------------------------------------------
