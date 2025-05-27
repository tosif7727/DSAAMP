import streamlit as st
from transformers import pipeline

st.title("Text Generation with GPT-2")

# Load the model only once
@st.cache_resource
def get_generator():
    return pipeline(task="text-generation", model="gpt2")
generator = get_generator()

user_input = st.text_area("Enter your prompt/question:", "Once I was a little")

if st.button("Generate"):
    with st.spinner("Generating..."):
        result = generator(user_input, max_length=50, num_return_sequences=1)
        st.markdown(f"**Generated Text:**\n\n{result[0]['generated_text']}")