# app.py

import os
import streamlit as st
from langchain.llms import OpenAI as LangchainOpenAI

# Configuration d'OpenAI avec votre clé d'API
os.environ['OPENAI_API_KEY'] = st.secrets["auth"]

# Configuration de la page
st.set_page_config(page_title='Générateur de Messages', page_icon="🤖", layout="wide", initial_sidebar_state="expanded")

# Titre avec emoji
st.title('Générateur de Messages 🤖')

# Introduction
st.write("""
Ce générateur est conçu pour aider à rédiger des messages adaptés à diverses situations. 
Il suffit de fournir les détails nécessaires, et le générateur produira un message adapté à vos besoins.
""")

# Sélection de la version de GPT
gpt_version = st.selectbox('Sélectionnez une version de GPT:', ['gpt-3.5-turbo', 'gpt-4'])

# Saisie du rôle
role = st.text_input('Indiquez votre rôle:')

# Contexte
contexte = st.text_area('Décrivez le contexte ou la situation:')

# Résultat souhaité
resultat_souhaite = st.text_area('Quel est le résultat ou l'action souhaitée?')

# Générer le message
def generate_message(gpt_version, role, contexte, resultat_souhaite):
    llm = LangchainOpenAI(model_name=gpt_version, temperature=0.2)
    prompt = f"Rôle: {role}. Contexte: {contexte}. Résultat souhaité: {resultat_souhaite}. Générer un message adapté."
    response = llm.predict(prompt)
    return response

if st.button('Générer le message 🚀'):
    message = generate_message(gpt_version, role, contexte, resultat_souhaite)
    st.subheader('Message Généré 📄')
    st.text_area("", message, height=300)

# Section d'aide et de support
st.sidebar.header('Aide & Support 🆘')
st.sidebar.text("Besoin d'aide ?")
st.sidebar.text("Consultez notre FAQ ou contactez-nous directement.")
