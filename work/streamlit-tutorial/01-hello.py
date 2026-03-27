import streamlit as st

st.title("✨Hello Streamlit! 🚀")
st.write("이것은 Streamlit으로 만든 간단한 웹 애플리케이션입니다.")

import streamlit as st

col1,col2 = st.columns([2,3])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.

with col1 :
  # column 1 에 담을 내용
  st.title('here is column1')
with col2 :
  # column 2 에 담을 내용
  st.title('here is column2')
  st.checkbox('this is checkbox1 in col2 ')

