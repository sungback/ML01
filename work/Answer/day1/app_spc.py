import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.set_page_config(page_title="공정 모니터링", layout="wide")
st.title("공정 모니터링")


@st.cache_data      # 화면을 바꿀 때마다 파일을 다시 읽지 않게 한다
def load():
    return pd.read_parquet("../../data/factory_table.parquet")


df = load()
# 힌트: st.sidebar.selectbox("이름", 목록), col.metric("이름", 값)
equip = st.sidebar.selectbox("설비 선택", sorted(df['equip_id'].unique()))
data = df[ df['equip_id'] == equip ]

col1, col2, col3 = st.columns(3)
col1.metric("생산 건수", f"{len(data)}건")
col2.metric("고장 건수", f"{data['failure'].sum()}건")
col3.metric("고장률", f"{data['failure'].mean():.1%}")

st.subheader("일별 고장 건수")
st.line_chart(data.resample("D", on="timestamp")["failure"].sum())

daily = data.resample("D", on="timestamp")["vibration"].mean()
base = daily.iloc[:60]
cl = base.mean()
mr_bar = base.diff().abs().mean()
ucl = cl + 2.66 * mr_bar
lcl = cl - 2.66 * mr_bar

st.subheader(f"{equip} 진동 I 관리도")
fig, ax = plt.subplots(figsize=(10, 3.5))
ax.plot(daily, marker="o")
ax.axhline(cl, color="green")
ax.axhline(ucl, color="red", linestyle="--")
ax.axhline(lcl, color="red", linestyle="--")
st.pyplot(fig)

st.subheader("관리한계를 벗어난 날")
out = daily[(daily > ucl) | (daily < lcl)]
st.dataframe(out.round(2))
