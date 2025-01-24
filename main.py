import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI as genai
from langchain_core.prompts import ChatPromptTemplate

st.title('Chat com BiologIA')
api = st.sidebar.text_input('Coloque a api')
if api == '19996865107':
    st.success('Senha correta!')
    api_key = st.secrets["google_api_key"]
    llm = genai(
        model='models/gemini-1.5-flash',
        temperature=0.1,
        api_key=api_key,
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system',
                '''
                # História
                    Você é um biologo que vai ajudar um iniciante em biologia respondendo todas as perguntas
                    e contando curiosidades e caracteristicas da pergunta
                # Saída
                    Titulo,
                    Corpo do texto,
                    E uma analise sobre o assunto da pergunta.
                    Em Markdown
                '''),
                ('human','{animal}')
        ]
    )
    chain = prompt | llm
    animal = st.text_input('Escreva um animal')
    if animal:
        st.write_stream(chain.stream({'animal':animal}))
else:
    try:
        llm = genai(
            model='models/gemini-1.5-flash',
            temperature=0.1,
            api_key=api
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                ('system',
                    '''
                # História
                    Você é um biologo que vai ajudar um iniciante em biologia respondendo todas as perguntas
                    e contando curiosidades e caracteristicas da pergunta
                # Saída
                    Titulo,
                    Corpo do texto,
                    E uma analise sobre o assunto da pergunta.
                    Em Markdown
                    '''),
                    ('human','{animal}')
            ]
        )


        chain = prompt | llm
        animal = st.text_input('Escreva um animal')
        if animal:
            st.write_stream(chain.stream({'animal':animal}))
    except:
        st.error('API Inválida')
