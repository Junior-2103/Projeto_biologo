import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI as genai
from langchain_core.prompts import ChatPromptTemplate

api = st.sidebar.text_input('Coloque a api')
if api == '19996865107':
    st.success('Senha correta!')
    load_dotenv()
    llm = genai(
        model='models/gemini-1.5-flash',
        temperature=0.1,
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system',
                '''
                # História
                    Você é um biologo que vai ajudar um iniciante em biologia falando  todas as curiosidade
                    principais caracteristicas: filo,ambiente que vive,altura em media,peso,tamanho.
                # Saída
                    Titulo - Nome do animal: Principal caracteristica/curiosidade,
                    Corpo do texto - Caracteristicas e curiosidade,
                    2º parte sobre uma parte das analise sobre uma das caracteristicas do animal
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
                        Você é um biologo que vai ajudar um iniciante em biologia falando  todas as curiosidade
                        principais caracteristicas: filo,ambiente que vive,altura em media,peso,tamanho.
                    # Saída
                        Titulo - Nome do animal: Principal caracteristica/curiosidade,
                        Corpo do texto - Caracteristicas e curiosidade,
                        2º parte sobre uma parte das analise sobre uma das caracteristicas do animal
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
