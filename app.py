#Password_Strength_Meter 👁 centered
#Password Strength Genrator 🔐
#Enter your password below to check its security level. 🔍
#❌ Password should be **at least 8 cherecter long**.
#❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.
#❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.
#❌ Password should include **at least one number (0-9)**.
#✅ **Strong Password** - Your password is secure
#⚠️ **Moderate Password** - Consider improveing by adding more feature
#❌ **Week Password** - Follow the suggestion below to strength it.
#🔍 **Improve Your Password**
#⚠️ Please enter a password first!
#
#


import streamlit as st
import re

st.set_page_config("Password_Strength_Meter",page_icon="👁",layout="centered")

st.title("Password Strength Genrator 🔐")
st.write("Enter your password below to check its security level.")

def check_password_strength(password):
    score = 0 
    feedbacks = []

    if len(password) >= 8:
        score += 1
    else:
        feedbacks.append("❌ Password should be **at least 8 cherecter long**.")   
           
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score += 1
    else:
        feedbacks.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")   

    if re.search(r"\d",password):
        score += 1
    else:
        feedbacks.append("❌ Password should include **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*]",password):
        score += 1
    else:
        feedbacks.append("❌ Include **at least one special cherecter (!@#$%^&*)**.")


    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure")    
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improveing by adding more feature")    
    else:
        st.error("❌ **Week Password** - Follow the suggestion below to strength it.")    

    if feedbacks:
        with st.expander("🔍 **Improve Your Password**"):
            for feedback in feedbacks:
                st.write(feedback)   

         
password = st.text_input(label="Enter your Password", type="password", placeholder="Enter Password", help="Ensure your password is strong 🔐" )

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.info("⚠️ Please enter a password first!")