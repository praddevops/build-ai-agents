from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

# Load the csv file
df = pd.read_csv("realistic_restaurant_reviews.csv")

# Load/Define the embedding model
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# specify the location to store the vector DB (you can choose to name it as you like)
db_location = "./.local/chroma_langchain_db"


# if db_location doesn't exist, vectorize the data otherwise skip it to avoid repeatedly vectorizing the data
add_documents = not os.path.exists(db_location)


# Prepare data
if add_documents:
    documents = []
    ids = []
    
    # create individual documents and add them to documents list
    for index, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"], # used for querying
            metadata = { "rating": row["Rating"], "date": row["Date"] }, # metadata is additional info included with Document, but isn't used for querying
            id = str(index)
        )
        ids.append(str(index))  # we need two seperate lists to store in the vector database - 1. documents 2. associated ids
        documents.append(document)

# Create and Initialize the vector store (Chroma DB)
vector_store = Chroma(
    collection_name = "restaurant_reviews",
    persist_directory = db_location,
    embedding_function = embeddings 
)

# Add data to the vector store
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

# Look up documents (specified count) and then we can pass them in the prompt for the LLM
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)
        