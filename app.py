import re
import streamlit as st


# Page Styling
st.set_page_config(page_title="Password Strength Meter", page_icon="👁", layout="centered")

# Page title and description
st.title("Password Strength Genrator 🔐")
st.write("Enter your password below to check its security level. 🔍")

# Password Strength Checker Function
def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 cherecter long**.")
        
        
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")
        
        
    if re.search(r"\d", password):
        score += 1    
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")    
    
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1    
    else:
        feedback.append("❌ Include **at least one special cherecter (!@#$%^&*)**.")    
    
    
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improveing by adding more feature")      
    else:
        st.error("❌ **Week Password** - Follow the suggestion below to strength it.")    
    
    
    #feedback
    if feedback:
        with st.expander("🔍 **Improve Your Password** "):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")                

#Button Working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!") 
        
        
        