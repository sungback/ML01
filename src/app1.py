# pip install streamlit
# streamlit run app1.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("AI4I 2020 간단 EDA")

df = pd.read_csv("ai4i2020.csv")

st.write("## 1. 데이터 보기")
st.dataframe(df.head())

st.write("## 2. 전체 고장률")
failure_rate = df["Machine failure"].mean() * 100
st.write(f"고장률: {failure_rate:.2f}%")

st.write("## 3. 타입별 고장률")
type_rate = df.groupby("Type")["Machine failure"].mean() * 100
st.dataframe(type_rate.reset_index())

fig, ax = plt.subplots()
ax.bar(type_rate.index, type_rate.values)
ax.set_title("Failure Rate by Type")
ax.set_xlabel("Type")
ax.set_ylabel("Failure Rate (%)")
st.pyplot(fig)

st.write("## 4. 변수 분포 보기")
col = st.selectbox(
    "변수 선택",
    ["Air temperature [K]", "Process temperature [K]", "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]"]
)

fig, ax = plt.subplots()
ax.hist(df[col], bins=30)
ax.set_title(f"{col} Distribution")
ax.set_xlabel(col)
ax.set_ylabel("Count")
st.pyplot(fig)

st.write("## 5. 고장/정상 비교")
fig, ax = plt.subplots()
df.boxplot(column="Tool wear [min]", by="Machine failure", ax=ax)
ax.set_title("Tool wear by Machine failure")
ax.set_xlabel("Machine failure")
ax.set_ylabel("Tool wear [min]")
plt.suptitle("")
st.pyplot(fig)
