import streamlit as st

# 사용자가 버튼을 클릭하면 특정 동작을 실행
if st.button("클릭하세요"):
    st.write("버튼이 클릭되었습니다!")

# 체크박스를 추가하여 사용자가 선택
agree = st.checkbox("동의합니다")
if agree:
    st.write("동의하셨습니다!")

# 라디오 버튼 : 여러 옵션 중 하나를 선택
selected_option = st.radio("옵션을 선택하세요", ("옵션 1", "옵션 2", "옵션 3"))
st.write(f"선택된 옵션: {selected_option}")

# 드롭다운 리스트에서 하나의 옵션을 선택
fruit = st.selectbox("과일을 선택하세요", ["사과", "바나나", "오렌지"])
st.write(f"선택한 과일: {fruit}")

# 여러 개의 옵션을 동시에 선택
planets = st.multiselect("행성을 선택하세요", ["목성", "화성", "해왕성"])
st.write(f"선택한 행성: {planets}")

# 슬라이더를 사용하여 숫자 값을 조정
number = st.slider("숫자를 선택하세요", 0, 50)
st.write(f"선택된 숫자: {number}")


rating = st.select_slider("평가를 선택하세요", ["나쁨", "보통", "좋음", "최고"])
st.write(f"선택한 평가: {rating}")
