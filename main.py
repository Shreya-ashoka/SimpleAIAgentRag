from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriver

# Initialize the Ollama LLM with the model name
model = OllamaLLM(model="llama3.2")

template ="""
you are an expert in answering questions about a pizza restaurant.

here are some relevant reviews: {reviews}

here is a question: {question}

"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n----------------------------------")
    question = input("Ask your question (or 'q' to quit): ")
    print("\n\n")
    if question.lower() == 'q':
        break

    reviews = retriver.invoke(question)
    result = chain.invoke({"reviews": reviews,"question": question})
    print(result)