import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rand = np.random.normal(1, 2, size=20)  # 정규분포 난수 생성
fig, ax = plt.subplots()
ax.hist(rand, bins=15)  # 히스토그램 그리기
st.pyplot(fig)


df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.bar_chart(df)

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)

# np.random.randn(500, 2): 500행 2열의 행렬 생성. 표준 정규 분포(평균 0, 표준편차 1)를 따르는 난수
# / [50, 50]: 생성된 난수들을 50으로 나눕니다. 원래 값들이 보통 -3에서 3 사이에 분포하므로, 50으로 나누면 약 -0.06에서 0.06 사이의 아주 작은 소수가 됩니다. 지도의 범위를 좁히기 위한 작업
# + [37.5663, 126.9918]: 여기에 특정 좌표를 더합니다. 이 숫자가 핵심인데, 바로 서울(Seoul)의 위도(Latitude)와 경도(Longitude)
df = pd.DataFrame(
      np.random.randn(500, 2) / [50, 50] + [37.5663, 126.9918],
      columns=['lat', 'lon']
  )
st.map(df)
