import streamlit as st
import random

# 크리스마스 테마 꾸미기
st.markdown("<h1 style='text-align: center; color: red;'>🎄 Merry Christmas 🎅</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>함께 크리스마스를 즐겨요! 🎁</p>", unsafe_allow_html=True)

# 크리스마스 메시지 작성 섹션
st.header("📜 크리스마스 메시지 작성")
with st.form("message_form"):
    name = st.text_input("당신의 이름:")
    message = st.text_area("다른 사람들에게 보내고 싶은 크리스마스 메시지:")
    submitted = st.form_submit_button("메시지 보내기")
    if submitted:
        if name and message:
            st.success(f"메시지가 성공적으로 전송되었습니다! 🎉")
            st.write(f"**{name}**: {message}")
        else:
            st.error("이름과 메시지를 모두 입력해주세요!")

# 크리스마스 퀴즈 섹션
st.header("❓ 크리스마스 퀴즈")
quiz_question = "산타클로스의 썰매를 끄는 사슴은 총 몇 마리일까요?"
quiz_options = ["6마리", "8마리", "9마리", "12마리"]
answer = st.radio(quiz_question, quiz_options)

if st.button("정답 확인"):
    if answer == "9마리":
        st.success("정답입니다! 🎉")
        st.balloons()
    else:
        st.error("틀렸습니다. 정답은 9마리입니다. 🎅")

# 랜덤 선물 받기
st.header("🎁 랜덤 크리스마스 선물 받기")
gifts = [
    "초콜릿 바 🎂",
    "크리스마스 장식품 🎄",
    "따뜻한 스웨터 🧥",
    "책 📚",
    "커피 한 잔 ☕",
    "귀여운 곰인형 🧸",
    "미니 산타 모자 🎅",
]
if st.button("선물 받기!"):
    gift = random.choice(gifts)
    st.success(f"당신이 받은 선물은... {gift}! 🎁")

# 실시간 채팅 (간단한 버전)
st.header("💬 실시간 크리스마스 채팅")
if "messages" not in st.session_state:
    st.session_state["messages"] = []

with st.form("chat_form"):
    chat_message = st.text_input("메시지를 입력하세요:")
    chat_submitted = st.form_submit_button("전송")
    if chat_submitted and chat_message:
        st.session_state["messages"].append(chat_message)

st.write("### 채팅 기록")
for msg in st.session_state["messages"]:
    st.write(f"🎄 {msg}")
