import streamlit as st

# 사용자가 텍스트를 입력할 수 있는 입력 상자를 제공
name = st.text_input("이름을 입력하세요")
st.write(f"입력된 이름: {name}")

# 사용자가 숫자를 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=100, step=1)
st.write(f"입력된 나이: {age}")

# 사용자가 날짜를 선택
selected_date = st.date_input("날짜 선택")
st.write(f"선택한 날짜: {selected_date}")

# 사용자가 시간을 선택
selected_time = st.time_input("시간 선택")
st.write(f"선택한 시간: {selected_time}")

# 여러 줄의 텍스트를 입력할 수 있는 입력 필드
message = st.text_area("메시지를 입력하세요")
st.write(f"입력된 메시지:\n{message}")

# 사용자가 파일을 업로드
uploaded_file = st.file_uploader("파일을 업로드하세요")
if uploaded_file is not None:
    st.write("업로드된 파일:", uploaded_file.name)

# 색상을 선택
color = st.color_picker("색상을 선택하세요", "#00f900")
st.write(f"선택한 색상: {color}")
