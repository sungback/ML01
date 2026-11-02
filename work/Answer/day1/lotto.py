import streamlit as st
import random
st.title("로또 번호 생성기")
st.markdown("### 합계가 170~200 사이인 것만 사용!")
def gen_lotto():
    while True:
        lotto = sorted( random.sample( range(1, 46), 6 ) )
        if 170 <= sum(lotto) <= 200:
            return lotto
btn = st.button("버튼을 클릭하여 로또를 생성해 주세요.")
if btn:
    for i in range(1, 6):
        lotto = gen_lotto()
        st.markdown(f"#### {i}. 행운의 번호: :green[{lotto}], {sum(lotto)}")
