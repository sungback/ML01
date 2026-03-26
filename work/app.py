# pip install streamlit
# streamlit run app.py

# import streamlit as st
# st.title('내 첫 Streamlit 앱')
# st.write('Hello, Streamlit!')

import streamlit as st
import pandas as pd

st.title("간단 대시보드")
df = pd.DataFrame({"A": [1, 2, 3], "B": [10, 20, 30]})
st.write(df)
value = st.slider("값 선택", 0, 100)
st.line_chart(df)
