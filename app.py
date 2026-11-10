import streamlit as st

from feedback_store import add_suggestion, initialize_database, list_suggestions


DATABASE_PATH = "suggestions.db"

initialize_database(DATABASE_PATH)

st.title("한 줄 건의함")
st.caption("이름 없이 익명으로 한 줄 건의를 남겨 주세요.")

with st.form("suggestion_form"):
    suggestion = st.text_input("건의 내용", placeholder="건의 내용을 입력하세요")
    submitted = st.form_submit_button("제출")

if submitted:
    try:
        add_suggestion(suggestion, DATABASE_PATH)
    except ValueError:
        st.error("빈 건의는 제출할 수 없습니다.")
    else:
        st.success("건의가 제출되었습니다.")

st.subheader("최근 건의")
suggestions = list_suggestions(DATABASE_PATH)
if suggestions:
    for content in suggestions:
        st.write(content)
else:
    st.info("아직 등록된 건의가 없습니다.")
