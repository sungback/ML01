# pip install streamlit
# streamlit run app2.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI4I 2020 EDA", layout="wide")

st.title("AI4I 2020 제조 데이터 EDA")
st.write("예지보전용 제조 데이터를 간단하게 탐색하는 Streamlit 앱")

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("ai4i2020.csv")
    return df

df = load_data()

# -----------------------------
# 전처리
# -----------------------------
df["Temp_diff"] = df["Process temperature [K]"] - df["Air temperature [K]"]

df["wear_bin"] = pd.cut(
    df["Tool wear [min]"],
    bins=[0, 50, 100, 150, 200, 250],
    include_lowest=True
)

numeric_cols = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
    "Temp_diff"
]

# -----------------------------
# 사이드바
# -----------------------------
st.sidebar.header("분석 옵션")

selected_col = st.sidebar.selectbox(
    "분포를 볼 변수 선택",
    numeric_cols
)

box_col = st.sidebar.selectbox(
    "고장/정상 비교 변수 선택",
    numeric_cols,
    index=4
)

show_raw = st.sidebar.checkbox("원본 데이터 보기", False)

# -----------------------------
# 기본 정보
# -----------------------------
st.subheader("1. 데이터 기본 정보")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("행 수", f"{df.shape[0]:,}")
with col2:
    st.metric("열 수", f"{df.shape[1]:,}")
with col3:
    failure_rate = df["Machine failure"].mean() * 100
    st.metric("전체 고장률", f"{failure_rate:.2f}%")

st.write("### 결측치 개수")
st.dataframe(df.isnull().sum().to_frame("missing_count"))

if show_raw:
    st.write("### 원본 데이터")
    st.dataframe(df.head(20))

# -----------------------------
# 타입별 고장률
# -----------------------------
st.subheader("2. 타입별 고장률")

type_summary = (
    df.groupby("Type")["Machine failure"]
    .agg(["count", "mean"])
    .reset_index()
)

type_summary["failure_rate(%)"] = type_summary["mean"] * 100
st.dataframe(type_summary[["Type", "count", "failure_rate(%)"]])

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(type_summary["Type"], type_summary["failure_rate(%)"])
ax.set_title("Failure Rate by Type")
ax.set_xlabel("Type")
ax.set_ylabel("Failure Rate (%)")
st.pyplot(fig)

# -----------------------------
# 변수 분포
# -----------------------------
st.subheader("3. 수치형 변수 분포")

fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(df[selected_col], bins=30)
ax.set_title(f"Distribution of {selected_col}")
ax.set_xlabel(selected_col)
ax.set_ylabel("Count")
st.pyplot(fig)

# -----------------------------
# 고장/정상 비교
# -----------------------------
st.subheader("4. 고장/정상 비교")

fig, ax = plt.subplots(figsize=(7, 4))
df.boxplot(column=box_col, by="Machine failure", ax=ax)
ax.set_title(f"{box_col} by Machine failure")
ax.set_xlabel("Machine failure (0=Normal, 1=Failure)")
ax.set_ylabel(box_col)
plt.suptitle("")
st.pyplot(fig)

group_mean = df.groupby("Machine failure")[box_col].mean().reset_index()
st.write("### 그룹 평균")
st.dataframe(group_mean)

# -----------------------------
# 공구 마모 구간별 고장률
# -----------------------------
st.subheader("5. 공구 마모 구간별 고장률")

wear_summary = (
    df.groupby("wear_bin", observed=False)["Machine failure"]
    .agg(["count", "mean"])
    .reset_index()
)

wear_summary["failure_rate(%)"] = wear_summary["mean"] * 100
st.dataframe(wear_summary[["wear_bin", "count", "failure_rate(%)"]])

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(wear_summary["wear_bin"].astype(str), wear_summary["failure_rate(%)"])
ax.set_title("Failure Rate by Tool Wear Bin")
ax.set_xlabel("Tool wear bin")
ax.set_ylabel("Failure Rate (%)")
plt.xticks(rotation=30)
st.pyplot(fig)

# -----------------------------
# 상관관계
# -----------------------------
st.subheader("6. 상관관계 히트맵")

corr_cols = numeric_cols + ["Machine failure"]
corr = df[corr_cols].corr()

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(corr, aspect="auto")
ax.set_xticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha="right")
ax.set_yticks(range(len(corr.columns)))
ax.set_yticklabels(corr.columns)
ax.set_title("Correlation Heatmap")
fig.colorbar(im, ax=ax)
st.pyplot(fig)

# -----------------------------
# 간단 해석
# -----------------------------
st.subheader("7. 해석 포인트")

st.markdown(
    """
- **전체 고장률**이 높지 않다면 제조 데이터의 불균형 특성을 확인할 수 있습니다.
- **타입별 고장률** 차이가 있으면 제품 타입에 따라 위험도가 다를 수 있습니다.
- **고장/정상 비교 박스플롯**으로 특정 변수의 차이를 빠르게 볼 수 있습니다.
- **공구 마모 구간별 고장률**이 올라가면 공구 마모가 중요한 신호일 수 있습니다.
- **Temp_diff**는 열 방출 상태를 간단히 볼 수 있는 파생변수입니다.
"""
)
