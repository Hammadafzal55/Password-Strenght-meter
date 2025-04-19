import re
import streamlit as st

st.set_page_config(page_title="Password Strenght Manager", page_icon="🔑", layout="centered")
# custom CSS for the app
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px; }
    .stButton button:hover {background-color: #45a049}
</style>
""", unsafe_allow_html=True)

# page title and description

st.title("🔐 Password Strength Generator")
st.write("Enter your password to check its strength.🔎")

# function to check password strength
def check_password_strenght(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", password ) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one digit (0-9)**.")

    # special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one special character(!@#$%^&*(),.?\":{}|<>)**.")

    #display password strength results
    if score == 4:
        st.success("✅**Strong Password** - Your Password is strong!")
        st.balloons()
    elif score == 3:
        st.info("⚠️**Moderate Password** - Consider improving security by adding more features.")
    else:
        st.warning("❗❌**Weak Password** - Follow the suggestions to improve your password strength.")

    if feedback:
        with st.expander("**🔎 Improve Your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure  your password is strong. 🔐")

# button woking
if st.button("Check Password Strength"):
    if password:
        check_password_strenght(password)
    else:
        st.warning("❗ Please enter a password first.") # show warning if password is empty

