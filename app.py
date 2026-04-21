import streamlit as st
import os
from main import process_pdf, ask_question

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


st.title("📄 Chat with Retail Documents using RAG")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    file_path = os.path.join("data", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded!")

    vectorstore = process_pdf(file_path)

    query = st.chat_input("Ask your question")

    if query:
        answer, sources = ask_question(vectorstore, query, st.session_state.chat_history)



        # ✅ Store conversation
        st.session_state.chat_history.append(("You", query))
        st.session_state.chat_history.append(("Bot", answer))
    
    # ✅ Display full conversation
    for role, msg in st.session_state.chat_history:
        if role == "You":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)

   #st.write("📚 Sources:")
   #for src in sources:
   #    st.write("-", src[:150])


