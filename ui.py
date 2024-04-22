import streamlit as st
from utils import write_to_json
import os
from rchain import rag_chain

st.set_page_config(
    page_title="Lallan Lucknow AI",
    page_icon="🙏",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Function to handle exceptions and store them in a JSON file
def handle_exception(exception):
    error_message = str(exception)
    st.error("Hme Lgta aap kuch aant shant dal diye hai")
    error_data = {"error_message": error_message}
    write_to_json(error_data, "errors.json")


# try:
# Load chat engine
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = rag_chain

# Load previous messages and email
if "messages" not in st.session_state:
    st.session_state.messages = []
if "email" not in st.session_state:
    st.session_state.email = ""
if "inpu" not in st.session_state:
    st.session_state.inpu = False

    # Form for email input
with st.form("my_form"):
    st.header("Enter your email")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Submit")
    if submitted and email != "":
        st.write("Email entered successfully. You can now proceed further.")
        write_to_json({"email": email}, "emails.json")
        st.session_state.email = email
        st.session_state.inpu = True

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input and assistant response
if prompt := st.chat_input(
    "Farmaiye Janaab", disabled=False if st.session_state.inpu else True
):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.spinner("Processing..."):

        a = st.session_state.rag_chain.invoke(prompt)
    with st.chat_message("assistant"):
        st.markdown(a)
    email_filename = os.path.join(
        "queries", f"{st.session_state.email.split('@')[0]}.json"
    )
    queries_folder = "queries"
    if not os.path.exists(queries_folder):
        os.makedirs(queries_folder)
    write_to_json(
        {"prompt": prompt, "answer": a},
        email_filename,
    )
    st.session_state.messages.append({"role": "assistant", "content": a})


# except Exception as e:
#     handle_exception(e)
