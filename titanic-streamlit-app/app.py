# app.py
# 역할: 저장된 titanic_pipeline.joblib 모델을 불러와 Streamlit 웹 앱으로 예측하기

from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


# ============================================================
# 1. 기본 설정
# ============================================================
BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "titanic_pipeline.joblib"

st.set_page_config(
    page_title="타이타닉 생존 예측 앱",
    page_icon="🚢",
    layout="centered",
)


# ============================================================
# 2. 모델 불러오기
# ============================================================
@st.cache_resource
def load_model():
    model = joblib.load(MODEL_PATH)
    return model


if not MODEL_PATH.exists():
    st.error("모델 파일이 없습니다.")
    st.write("먼저 아래 명령어로 모델을 학습하고 저장하세요.")
    st.code("python titanic-streamlit-app/train_model.py")
    st.stop()

pipeline = load_model()


# ============================================================
# 3. 화면 제목
# ============================================================
st.title("타이타닉 생존 예측 앱")
st.write(
    """
    승객 정보를 입력하면 머신러닝 모델이 생존 여부를 예측합니다.

    이 앱은 `titanic.csv` 데이터로 학습한  
    `DecisionTreeClassifier` 모델을 사용합니다.
    """
)


# ============================================================
# 4. 사이드바 설명
# ============================================================
st.sidebar.header("앱 설명")
st.sidebar.write(
    """
    이 예제는 타이타닉 데이터를 사용한  
    머신러닝 배포 실습용 앱입니다.

    사용 흐름:

    1. 승객 정보 입력
    2. 입력값 확인
    3. 생존 여부 예측
    4. 생존 확률 확인
    """
)

st.sidebar.markdown("---")
st.sidebar.write("사용 모델: Decision Tree")
st.sidebar.write("저장 파일: titanic_pipeline.joblib")


# ============================================================
# 5. 사용자 입력 영역
# ============================================================
st.subheader("1. 승객 정보 입력")

pclass = st.selectbox(
    "객실 등급",
    options=[1, 2, 3],
    index=2,
    help="1등석, 2등석, 3등석 중 선택합니다.",
)

sex = st.selectbox(
    "성별",
    options=["male", "female"],
    format_func=lambda x: "남성" if x == "male" else "여성",
)

age = st.slider(
    "나이",
    min_value=0,
    max_value=80,
    value=30,
)

sibsp = st.number_input(
    "함께 탑승한 형제/배우자 수",
    min_value=0,
    max_value=10,
    value=0,
)

parch = st.number_input(
    "함께 탑승한 부모/자녀 수",
    min_value=0,
    max_value=10,
    value=0,
)

fare = st.number_input(
    "운임 요금",
    min_value=0.0,
    max_value=600.0,
    value=30.0,
    step=1.0,
)

embarked = st.selectbox(
    "탑승 항구",
    options=["S", "C", "Q"],
    format_func=lambda x: {
        "S": "S - Southampton",
        "C": "C - Cherbourg",
        "Q": "Q - Queenstown",
    }[x],
)


# ============================================================
# 6. 입력값을 DataFrame으로 변환
# ============================================================
input_data = pd.DataFrame(
    {
        "pclass": [pclass],
        "sex": [sex],
        "age": [age],
        "sibsp": [sibsp],
        "parch": [parch],
        "fare": [fare],
        "embarked": [embarked],
    }
)

st.subheader("2. 입력 데이터 확인")
st.dataframe(input_data, use_container_width=True)


# ============================================================
# 7. 예측 실행
# ============================================================
st.subheader("3. 예측 결과")

if st.button("생존 여부 예측하기"):

    prediction = pipeline.predict(input_data)[0]
    probability = pipeline.predict_proba(input_data)[0]

    death_probability = probability[0]
    survival_probability = probability[1]

    if prediction == 1:
        st.success("예측 결과: 생존 가능성이 높습니다.")
    else:
        st.error("예측 결과: 생존 가능성이 낮습니다.")

    st.write(f"생존 확률: **{survival_probability:.2%}**")
    st.write(f"사망 확률: **{death_probability:.2%}**")

    result_df = pd.DataFrame(
        {
            "구분": ["사망 확률", "생존 확률"],
            "확률": [death_probability, survival_probability],
        }
    )

    st.bar_chart(
        data=result_df,
        x="구분",
        y="확률",
    )


# ============================================================
# 8. 하단 안내
# ============================================================
st.markdown("---")

st.caption(
    """
    주의: 이 앱은 수업용 예제입니다.  
    실제 의사결정용 모델이 아니라, 머신러닝 배포 흐름을 이해하기 위한 데모입니다.
    """
)
