import streamlit as st  # 웹 앱 구성을 위한 메인 라이브러리
import joblib           # 저장된 AI 모델을 불러오기 위함
import numpy as np      # 입력 데이터를 행렬로 변환하기 위함
import pandas as pd     # 데이터를 표(Table)와 차트로 시각화하기 위함

# [설정] 웹 페이지의 제목과 아이콘, 레이아웃 설정
st.set_page_config(
    page_title="Iris 품종 예측기 v2026", 
    page_icon="🌸", 
    layout="centered"
)

# [함수] 모델 로딩 (캐싱 기능을 사용하여 웹사이트 속도 저하 방지)
@st.cache_resource
def load_trained_model():
    try:
        return joblib.load('svm_model.pkl')
    except FileNotFoundError:
        st.error("⚠️ 'svm_model.pkl' 파일을 찾을 수 없습니다. 학습 코드를 먼저 실행하세요!")
        return None

# 모델 로드 및 데이터 정의
model = load_trained_model()
target_names = ['Setosa', 'Versicolor', 'Virginica']

# 각 품종별 이미지 URL (위키피디아 공용 이미지)
iris_images = {
    'Setosa': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg',
    'Versicolor': 'https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg',
    'Virginica': 'https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg'
}

# --- 화면 UI 시작 ---
st.title("🌸 붓꽃(Iris) 품종 예측 서비스")
st.write("최신 Streamlit API가 적용된 예측 앱입니다.")

# [사이드바] 특징 입력
st.sidebar.header("📏 특징(Feature) 입력")

def user_input_features():
    s_len = st.sidebar.slider('꽃받침 길이', 4.0, 8.0, 5.8)
    s_wid = st.sidebar.slider('꽃받침 너비', 2.0, 4.5, 3.0)
    p_len = st.sidebar.slider('꽃잎 길이', 1.0, 7.0, 4.3)
    p_wid = st.sidebar.slider('꽃잎 너비', 0.1, 2.5, 1.3)
    return np.array([[s_len, s_wid, p_len, p_wid]])

input_data = user_input_features()

# [메인 화면] 입력값 확인
st.subheader("1. 입력된 수치 데이터")
df = pd.DataFrame(input_data, columns=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
st.table(df)

# [메인 화면] 예측 실행 버튼
if st.button('🚀 어떤 품종일까요?'):
    if model is not None:
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
        predicted_name = target_names[prediction]

        st.divider()
        st.balloons()
        st.success(f"### 분석 결과: 이 꽃은 **{predicted_name}**입니다!")

        # [업그레이드 레이아웃]
        col1, col2 = st.columns([1, 1]) 

        with col1:
            st.subheader("📸 꽃 사진")
            # *** 2026년 최신 방식: width='stretch' 사용 ***
            st.image(
                iris_images[predicted_name], 
                caption=predicted_name, 
                width='stretch'  # 컨테이너 너비에 맞춰 확장
            )

        with col2:
            max_prob = np.max(probabilities) * 100
            st.metric(label="예측 신뢰도", value=f"{max_prob:.2f}%")

            st.subheader("📊 품종별 확률 분포")
            prob_df = pd.DataFrame({
                '품종': target_names,
                '확률 (%)': probabilities * 100
            })
            st.bar_chart(prob_df.set_index('품종'))

    else:
        st.warning("모델 파일이 없어 예측을 수행할 수 없습니다.")
