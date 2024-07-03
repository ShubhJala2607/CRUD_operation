import streamlit as st
import subprocess
import time
import webbrowser

# Function to start the Flask app
def start_flask():
    subprocess.Popen(["python", "flask_app.py"])
    time.sleep(5)
    # redirect to a web browser to the Flask app URL
    webbrowser.open_new_tab("http://127.0.0.1:5000")

# Display a message to start the Flask app
st.title("Flask App on Streamlit Cloud")
st.write("Click the button below to start the Flask app.")

if st.button("Start Flask App"):
    start_flask()
    st.write("Flask app started!")

st.write("The Flask app is running. You can now make requests to it.")
