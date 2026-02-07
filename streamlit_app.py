"""
Professional AI Banking Assistant - Streamlit Web App
Deploy to Streamlit Cloud for free hosting
"""

import streamlit as st
from banking_bot import BankingBot
import os

# Page configuration
st.set_page_config(
    page_title="Banking Assistant",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 0rem;
    }
    .stChatMessage {
        padding: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "bot" not in st.session_state:
    try:
        st.session_state.bot = BankingBot()
        st.session_state.bot_ready = True
    except Exception as e:
        st.session_state.bot_ready = False
        st.session_state.error_message = str(e)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("🏦 Banking Assistant")
    st.markdown("---")
    
    st.subheader("About")
    st.markdown("""
    Professional AI Banking Assistant powered by **Mistral Large**.
    
    I can help with:
    - 📋 Account types & products
    - 💳 Card information
    - 🏠 Loan guidance
    - 🔐 Security tips
    - 🆔 KYC process
    - 💻 Digital banking
    - ❓ General banking questions
    """)
    
    st.markdown("---")
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        if st.session_state.bot_ready:
            st.session_state.bot.clear_history()
        st.success("Conversation cleared!")
    
    st.markdown("---")
    
    st.subheader("⚠️ Security Notice")
    st.markdown("""
    - Never share account numbers, PINs, or passwords
    - This bot cannot access your account
    - For account-specific issues, contact official support
    - Information provided is general guidance only
    """)
    
    st.markdown("---")
    st.caption("🚀 Powered by [Mistral AI](https://mistral.ai)")

# Main content
col1, col2 = st.columns([3, 1])

with col1:
    st.title("🏦 Professional Banking Assistant")

with col2:
    if st.session_state.bot_ready:
        st.success("✓ Ready", icon="✅")
    else:
        st.error("✗ Error", icon="❌")

st.markdown("---")

# Bot status
if not st.session_state.bot_ready:
    st.error(f"""
    ⚠️ **Bot Initialization Failed**
    
    Error: {st.session_state.error_message}
    
    **Solution:** Make sure your `.streamlit/secrets.toml` file contains:
    ```
    MISTRAL_API_KEY = "your_api_key_here"
    ```
    """)
    st.stop()

# Chat interface
st.subheader("Chat")

# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me about banking products, security, KYC, digital banking..."):
    # Add user message to session
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            try:
                response = st.session_state.bot.chat(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_text = f"❌ Error: {str(e)}"
                st.error(error_text)
                st.session_state.messages.append({"role": "assistant", "content": error_text})

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <small>💡 Tips: Ask about account types, cards, loans, KYC, security, or digital banking</small><br>
    <small>🔒 Your privacy is protected. This bot cannot access your account or sensitive data.</small>
</div>
""", unsafe_allow_html=True)
