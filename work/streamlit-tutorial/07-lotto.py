import streamlit as st
import random
from datetime import datetime

st.title('로또 생성기 🚀')
st.write("합계가 **100~170** 사이인 번호만 추출합니다.")

def generate_lotto():
    while True:
        # 1부터 45까지 6개의 숫자를 중복 없이 추출 후 정렬
        lotto = sorted(random.sample(range(1, 46), 6))

        # 합계가 100 이상 170 이하인지 확인
        if 100 <= sum(lotto) <= 170:
            return lotto

# st.subheader(f'행운의 번호: :green[{generate_lotto()}]')
# st.write(f"생성된 시각: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

button = st.button('버튼을 클릭해서 로또를 생성해 주세요!')

if button:
    for i in range(1, 6):
        st.subheader(f'{i}. 행운의 번호: :green[{generate_lotto()}]')
    st.write(f"📅 생성 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
