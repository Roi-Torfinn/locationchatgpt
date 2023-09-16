import os
import streamlit as st
from langchain.llms import OpenAI as LangchainOpenAI

# Configuration d'OpenAI avec votre clé d'API
os.environ['OPENAI_API_KEY'] = st.secrets["auth"]

# Configuration de la page
st.set_page_config(page_title='Gestion de Location de Chats et Chiens pour Promenades', page_icon="🐾", layout="wide", initial_sidebar_state="expanded")

# Titre avec emoji
st.title('Gestion de Location de Chats et Chiens pour Promenades 🐾')

# Paragraphe introductif
st.write("""
Bienvenue sur notre plateforme de gestion de location d'animaux pour des promenades. 
Vous pouvez choisir entre différents types de chats et de chiens, sélectionner la durée de la promenade, et même ajouter des services supplémentaires.
""")

# Catégories et sous-catégories de location
categories = {
    "Chats": ["Chaton", "Chat adulte", "Chat âgé"],
    "Chiens": ["Chiot", "Chien adulte", "Chien âgé"]
}

# Sélection de la catégorie et de la sous-catégorie
categorie = st.selectbox('Sélectionnez une catégorie:', list(categories.keys()))
sous_categorie = st.selectbox('Sélectionnez une sous-catégorie:', categories[categorie])

# Durée de la promenade
duree = st.slider("Durée de la promenade (en minutes):", 15, 120, 30)

# Services supplémentaires
services = st.multiselect("Services supplémentaires:", ["Nourriture", "Jouets", "Soins médicaux"])

# Informations de contact
st.header('Informations de Contact 📞')
nom = st.text_input('Votre nom complet')
telephone = st.text_input("Votre numéro de téléphone")
email = st.text_input("Votre adresse e-mail")

# Générer la réservation
def generate_booking(categorie, sous_categorie, duree, services, nom, telephone, email):
    llm = LangchainOpenAI(model_name='gpt-3.5-turbo-16k', temperature=0.2)
    prompt = f"Générer une réservation pour une promenade avec un {sous_categorie} de la catégorie {categorie} pour une durée de {duree} minutes. Services supplémentaires : {', '.join(services)}. Contact : {nom}, {telephone}, {email}."
    response = llm.predict(prompt)
    return response

if st.button('Confirmer la réservation 🚀'):
    booking = generate_booking(categorie, sous_categorie, duree, services, nom, telephone, email)
    st.subheader('Réservation Confirmée 📄')
    st.text_area("", booking, height=300)

# Section d'aide et de support
st.sidebar.header('Aide & Support 🆘')
st.sidebar.text("Besoin d'aide ?")
st.sidebar.text("Consultez notre FAQ ou contactez-nous directement.")
