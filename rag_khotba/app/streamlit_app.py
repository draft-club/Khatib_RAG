import streamlit as st
from configs.settings import MODEL_PATH, INDEX_PATH, AUDIO_TOGGLE
from retrieval.retriever import Retriever
from generation.generator import Generator
from audio.tts_google import TextToSpeech

# Initialize components
retriever = Retriever(INDEX_PATH)
generator = Generator(MODEL_PATH)
tts = TextToSpeech()

# Streamlit app title
st.title("Khotba Retrieval and Generation")

# User input for query
user_query = st.text_input("Enter your query:")

if st.button("Search"):
    if user_query:
        # Retrieve relevant chunks
        results = retriever.retrieve(user_query)
        st.write("### Retrieved Results:")
        for result in results:
            st.write(result)

        # Generate response
        response = generator.generate(user_query)
        st.write("### Generated Response:")
        st.write(response)

        # Text-to-Speech option
        if AUDIO_TOGGLE:
            if st.button("Generate Audio"):
                tts.speak(response)
                st.success("Audio generated successfully!")
    else:
        st.warning("Please enter a query to search.")