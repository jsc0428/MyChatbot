import streamlit as st

st.title("간단한 챗봇")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("메시지를 입력하세요:")

if st.button("전송") and user_input:
    # 간단한 챗봇 응답 (에코)
    response = f"챗봇: {user_input}"
    st.session_state['chat_history'].append(("나", user_input))
    st.session_state['chat_history'].append(("챗봇", response))

st.write("---")
for speaker, message in st.session_state['chat_history']:
    st.write(f"**{speaker}:** {message}")
