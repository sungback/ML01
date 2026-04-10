# pip install streamlit scikit-learn joblib pandas
# streamlit run app.py

import streamlit as st  # 웹 앱 구성을 위한 메인 라이브러리
import joblib           # 저장된 AI 모델을 불러오기 위함
import numpy as np      # 입력 데이터를 행렬로 변환하기 위함
import pandas as pd     # 데이터를 표(Table)와 차트로 시각화하기 위함

# [함수] 모델 로딩 (캐싱 기능을 사용하여 웹사이트 속도 저하 방지)
@st.cache_resource
def load_trained_model():
    try:
        # 학습시킨 모델 파일을 불러옵니다.
        return joblib.load('svm_model.pkl')
    except FileNotFoundError:
        # 파일이 없을 경우 화면에 에러 메시지를 표시합니다.
        st.error("⚠️ 'svm_model.pkl' 파일을 찾을 수 없습니다. 학습 코드를 먼저 실행하세요!")
        return None

# 모델 로드 및 품종 이름 정의
model = load_trained_model()
target_names = ['Setosa', 'Versicolor', 'Virginica']

# --- 화면 UI 시작 ---
st.title("🌸 붓꽃(Iris) 품종 예측 서비스")
st.write("왼쪽 사이드바에서 꽃의 수치를 조절하고 예측 버튼을 눌러보세요.")

# [사이드바] 사용자가 수치를 입력할 수 있는 슬라이더 생성
st.sidebar.header("📏 특징(Feature) 입력")

def user_input_features():
    # slider(이름, 최소, 최대, 기본값)
    s_len = st.sidebar.slider('꽃받침 길이 (Sepal Length)', 4.0, 8.0, 5.8)
    s_wid = st.sidebar.slider('꽃받침 너비 (Sepal Width)', 2.0, 4.5, 3.0)
    p_len = st.sidebar.slider('꽃잎 길이 (Petal Length)', 1.0, 7.0, 4.3)
    p_wid = st.sidebar.slider('꽃잎 너비 (Petal Width)', 0.1, 2.5, 1.3)

    # 모델 입력 형식인 2차원 배열(1행 4열)로 변환
    data = np.array([[s_len, s_wid, p_len, p_wid]])
    return data

# 사용자 입력값 저장
input_data = user_input_features()

# [메인 화면] 입력값 확인
st.subheader("1. 입력된 수치 데이터")
df = pd.DataFrame(input_data, columns=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
st.table(df) # 표 형태로 출력

# [메인 화면] 예측 실행 버튼
if st.button('🚀 어떤 품종일까요?'):
    if model is not None:
        # 1. AI 예측 결과 (0, 1, 2 중 하나)
        prediction = model.predict(input_data)[0]
        # 2. AI가 각 품종이라고 생각하는 확률값
        probabilities = model.predict_proba(input_data)[0]

        st.divider() # 구분선 추가
        st.balloons() # 축하 풍선 효과

        # 결과 메시지 (성공을 뜻하는 초록색 박스)
        st.success(f"### 분석 결과: 이 꽃은 {target_names[prediction]}입니다!")

        # 최대 확률 정보 표시
        max_prob = np.max(probabilities) * 100
        st.write(f"예측 신뢰도: **{max_prob:.2f}%**")

        # [시각화] 막대 차트로 확률 보여주기
        st.subheader("📊 품종별 확률 분포")
        prob_df = pd.DataFrame({
            '품종': target_names,
            '확률 (%)': probabilities * 100
        })
        # 품종 이름을 인덱스로 설정하여 차트 생성
        st.bar_chart(prob_df.set_index('품종'))
    else:
        st.warning("모델이 로드되지 않아 예측을 수행할 수 없습니다.")
