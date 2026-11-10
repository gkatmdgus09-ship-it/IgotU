# 한 줄 건의함

익명으로 한 줄 건의를 제출하고 최신순으로 확인하는 Streamlit 앱입니다. 건의 내용은 앱 폴더의 `suggestions.db` SQLite 데이터베이스에 저장됩니다. 이름이나 연락처 등 개인정보는 입력받지 않습니다.

## 실행

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## 테스트

```bash
python -m unittest discover -s tests
```
