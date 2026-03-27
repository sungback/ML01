import streamlit as st
from PIL import Image
import pandas as pd



image = Image.open("example.jpg")
st.image(image, caption="예제 이미지", width=400)

st.audio("exam_mp3.mp3")

st.video("exam_mp4.mp4")

df = pd.read_csv('titanic.csv')
# st.write(df) # 기본적인 형태로 출력
st.dataframe(df) # 스크롤 및 정렬 기능이 포함된 인터랙티브한 데이터프레임을 출력
# st.table(df) # 정적인 테이블 형태로 데이터를 출력

st.json({
      '이름': '홍길동',
      '나이': 25,
      '거주지': '을지로'
  })

st.metric(label="삼성전자", value="180,900원", delta="-4.29%")
st.metric(label="SK하이닉스", value="940,000원", delta="-5.53%")
