import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory


template = """Você é um Assistente de Viagem que ajuda o usuário a planejar viagens,
dando sugestões de destinos, roteiros e dicas práticas.
A primeira coisa que deve fazer é perguntar para onde o usuário vai, com quantas pessoas e por quanto tempo

Histórico de conversa:
{history}
    
Entrada do usuário:
{input}
"""
 

# Criar template de prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Configurar o modelo
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Criar chain
chain = prompt | llm

# Armazenar histórico de sessões
store = {}

def get_session_history(session_id: str) -> ChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# Criar chain com histórico
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

def iniciar_assistente_viagem():
    print("Bem-vindo ao Assistente de Viagem! Digite 'sair' para encerrar.\n")
    while True:
        pergunta_usuario = input("Você: ")
        
        if pergunta_usuario.lower() in ["sair", "exit"]:
            print("Assistente de viagem: Até mais! Aproveite sua viagem!")
            break;
        
        resposta = chain_with_history.invoke(
            {"input": pergunta_usuario},
            config={'configurable': {'session_id': 'user123'}}
        )
        
        print('Assistente de Viagem:', resposta.content)
        
if __name__ == '__main__':
    iniciar_assistente_viagem()