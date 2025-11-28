from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from vector import retriever
model = OllamaLLM(model="llama3.2")

# Step 1: Define the system and human message templates
system_template = """
You are a helpful assistant. 
You are an expert in answering questions about a pizza restaurant
Here are some reviews: {reviews}
"""
human_template = "Here is the question to answer: {question}"

# Step 2: Create message prompt templates
system_message = SystemMessagePromptTemplate.from_template(system_template)
human_message = HumanMessagePromptTemplate.from_template(human_template)

# Step 3: Combine into a ChatPromptTemplate
chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])


while True:
   # Step 4: Format the prompt with variables
   print("-------------------------------------------------------------")
   question = input("Ask your question (enter q to quit): ")
   print("---------------------------Response--------------------------")
   if question == 'q':
      print("quitting..\n")
      break

   # retriever embeds the question and 
   # will look up the vector store for relevant reviews, using similarity search algorithm,
   # and returns the top results (return result count specified in the retriever implementation)
   reviews = retriever.invoke(question) 
   formatted_prompt = chat_prompt.format(reviews=reviews, question=question)

   # Step 5: Invoke the model
   result = model.invoke(formatted_prompt)
   print(result)
   