import streamlit as st
import csv
import os
from datetime import datetime

DATA_FILE = "suggestions.csv"

st.set_page_config(page_title="한 줄 건의함", page_icon="💡")
st.title("💡 한 줄 건의함")

# 저장용 CSV 파일이 없으면 헤더와 함께 생성
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["content", "time"])

# 건의 작성 폼
with st.form(key="suggestion_form", clear_on_submit=True):
    content = st.text_input("건의 내용", placeholder="의견을 자유롭게 입력하세요.")
    submitted = st.form_submit_button("제출")

    if submitted:
        if not content.strip():
            st.warning("내용을 입력해 주세요.")
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(DATA_FILE, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([content.strip(), timestamp])
            st.success("건의가 제출되었습니다.")

st.divider()
st.subheader("📋 접수된 건의 목록 (최신순)")

# 건의 목록 불러오기 및 최신순 출력
if os.path.exists(DATA_FILE):
    suggestions = []
    with open(DATA_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # 헤더(첫 줄) 건너뛰기
        for row in reader:
            if row:
                suggestions.append(row)

    if not suggestions:
        st.info("아직 접수된 건의가 없습니다.")
    else:
        # 역순(최신순)으로 출력
        for item in reversed(suggestions):
            st.write(f"• **{item[0]}** *({item[1]})*")