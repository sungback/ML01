## Streamlit 정보
- Streamlit은 Python으로 데이터 앱을 빠르게 만드는 오픈소스 라이브러리입니다. 주로 데이터 과학자와 개발자들이 웹 대시보드나 시각화 앱을 몇 줄 코드로 쉽게 구축할 수 있게 해줍니다.

### 주요 특징
- 간편한 사용: Python 스크립트를 간단한 방법으로 웹 애플리케이션으로 변환할 수 있습니다. 복잡한 웹 개발 지식이 없어도 사용할 수 있습니다.
- 데이터 과학 친화적: 데이터 시각화, 데이터 분석, 머신러닝 모델의 결과를 쉽게 웹에서 시연할 수 있습니다.
- 커스터마이징과 확장성: 다양한 위젯과 API를 통해 사용자 입력, 차트, 맵 등을 웹 애플리케이션에 쉽게 통합할 수 있습니다.
- 빠른 프로토타이핑: 머신러닝 프로토타입 및 데이터 과학 프로젝트를 빠르게 웹 애플리케이션으로 전환할 수 있어, 데모나 프레젠테이션을 손쉽게 준비할 수 있습니다.
- Python 스크립트만 작성하면 자동으로 웹 인터페이스를 생성합니다.
- st.write(), st.slider(), st.button() 같은 간단한 API로 텍스트, 차트, 이미지 등을 렌더링합니다.
- 실시간 상호작용(위젯)이 가능하며, pandas DataFrame이나 Plotly 그래프를 바로 표시할 수 있습니다.

### 설치 및 실행

- pip install streamlit
- streamlit hello  # 데모 확인
- streamlit run app.py  # 앱 실행

- app.py 파일에 import streamlit as st 후 코드를 작성하면 브라우저에서 바로 열립니다.

### app.py 소스

import streamlit as st
import pandas as pd

st.title("간단 대시보드")
df = pd.DataFrame({"A": [1, 2, 3], "B": [10, 20, 30]})
st.write(df)
value = st.slider("값 선택", 0, 100)
st.line_chart(df)

- 위 코드를 저장하고 실행하면 슬라이더와 차트가 포함된 웹 앱이 뜹니다.

- 시작 > 모두 > Anaconda(miniconda 3) > Anaconda Prompt

- pip install streamlit

- streamlit run app.py

- streamlit run app1.py

- streamlit run app2.py
