"# ML01 

## 🛠️ 개발 환경 구성하기

### 1. Miniconda 설치 및 설정
1. **Miniconda 다운로드 및 설치**
   - [Miniconda 다운로드 링크](https://repo.anaconda.com/miniconda/)
   - 운영체제별 설치 파일을 다운로드한 후, Next와 Yes를 클릭하여 설치를 진행합니다.
2. **Miniconda 프롬프트 실행**
   - `시작` > `모두` > `Anaconda (miniconda3)` > `Anaconda Prompt`
3. **Conda 업데이트**
   ```bash
   conda update -n base -c defaults conda
   ```
4. **기본 레포지토리를 conda-forge로 변경**
   ```bash
   conda config --add channels conda-forge
   conda config --set channel_priority strict
   ```

### 2. 가상환경 생성 및 필요 라이브러리 설치
1. **가상환경 생성 및 활성화 (Python 3.11)**
   ```bash
   conda create -n ds python=3.11 -y
   conda activate ds
   ```
2. **필수 라이브러리 설치**
   ```bash
   conda install -c conda-forge numpy pandas scipy matplotlib seaborn plotly jupyter scikit-learn statsmodels openpyxl beautifulsoup4 lxml requests tqdm xgboost lightgbm optuna catboost
   ```

### 3. Visual Studio Code 설치
- [VS Code 다운로드 링크](https://code.visualstudio.com/download)
- 운영체제별 설치 파일을 다운로드한 후, Next와 Yes를 클릭하여 설치를 진행합니다.

---

## 📚 추천 학습 자료 및 링크

### 데이터 관련 주요 사이트
* [공공 데이터 포털](https://www.data.go.kr/)
* [국가 통계 포털 (KOSIS)](https://kosis.kr/index/index.do)
* [서울 열린 데이터 광장](https://data.seoul.go.kr/)
* [AI hub](https://aihub.or.kr/)
* [Google Dataset Search](https://datasetsearch.research.google.com/)
* [한국은행 경제통계 시스템 (ECOS)](https://ecos.bok.or.kr)
* [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/)
* [OpenML](https://www.openml.org/)
* [EU Open Research Repository (Zenodo)](https://zenodo.org/)
* [Huggingface Datasets](https://huggingface.co/datasets)
* [Registry of Open Data on AWS](https://registry.opendata.aws/)

### 활용 플랫폼
* [인공지능 제조 플랫폼 (KAMP)](https://www.kamp-ai.kr/main)
* [Kaggle (캐글)](https://www.kaggle.com/)

### Streamlit 학습 자료
* [Streamlit 공식 홈페이지](https://streamlit.io/)
* [Wikidocs - 데이터 과학자의 쉬운 웹 제작 도구](https://wikidocs.net/226653)
* [블로그 추천 - Streamlit 상세 설명](https://blog.zarathu.com/posts/2023-02-01-streamlit/)
* [GitHub 튜토리얼](https://github.com/teddylee777/streamlit-tutorial)
* [YouTube 영상 추천](https://www.youtube.com/watch?v=F8a-0JFHfOo)

### 추천 영상 강의
* **통계 기초**: [딥하지 않은 확률통계 (YouTube)](https://www.youtube.com/watch?v=1rppbn9M35c&list=PL44zjiJMJWSohV9vl-YU35sDS7nNBLbJQ)
* **AI 마스터하기**: [YouTube 재생목록](https://www.youtube.com/playlist?list=PLVE1cahS5WEShoNLpkRwwsmHcO9xaHorz)

---

## 📊 Kaggle 추천 데이터셋 및 팁

### Kaggle 제조 데이터 추천 데이터셋
1. [Predictive Maintenance Dataset (AI4I 2020)](https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020)
2. [Predictive Maintenance for Industrial Machines](https://www.kaggle.com/code/sayidmufaqih/predictive-maintenance-for-industrial-machines)
3. [SECOM (Semiconductor Manufacturing) Dataset](https://www.kaggle.com/datasets/paresh2047/uci-semcom)
4. [Faulty Steel Plates](https://www.kaggle.com/datasets/uciml/faulty-steel-plates)
5. [Predicting Manufacturing Defects Dataset](https://www.kaggle.com/datasets/rabieelkharoua/predicting-manufacturing-defects-dataset)

### Kaggle 노트북 번역 크롬 확장 프로그램 사용법
**1. 설치 방법**
- [Github 저장소](https://github.com/sungback/DS01)에서 `kaggle-notebook-translation-helper-main.zip` 다운로드
- 다운로드 된 파일을 안전한 폴더(예: `문서\kaggle-notebook-translation-helper-main`)에 압축 해제
- 크롬 브라우저 실행 > 우측 상단 `⋮` 클릭 > `확장 프로그램` > `확장 프로그램 관리`
- 우측 상단 `개발자 모드` 활성화(On)
- `[압축 해제된 확장 프로그램 로드]` 클릭 후 압축 해제한 폴더 아래의 `src` 폴더 선택
- `Kaggle Notebook Translation Helper 1.4.0` 설치 완료 확인

**2. 캐글에서 번역 기능 사용하기**
- Kaggle 데이터셋/대회 진입 (예: Competitions > Getting Started > Titanic)
- `Code` 탭에서 특정 노트북 클릭 (예: "Titanic competition w/ TensorFlow Decision Forests")
- 좌측 상단의 `[Display iframe]` 버튼 클릭 
- 화면 우클릭 후 `한국어로 번역` 선택

---

## 🤖 AutoML (PyCaret) 가상환경 설정 및 사용법

**1. Anaconda Prompt 실행**
- `시작` > `모두` > `Anaconda (miniconda3)` > `Anaconda Prompt`

**2. 가상환경 생성 및 활성화**
> 💡 *참고: Python 3.10 버전이 PyCaret과 가장 호환성이 좋습니다.*
```bash
# 가상환경 생성
conda create -n pycaret_env python=3.10 -y

# 가상환경 활성화
conda activate pycaret_env
```

**3. 필수 라이브러리 설치**
> 설치 시 `matplotlib`, `seaborn`, `scikit-learn` 등 주요 데이터 분석 라이브러리가 함께 설치됩니다.
```bash
pip install "pycaret[full]" jupyter ipykernel
```

**4. 참고 소스 (PyCaret 사용 예제)**
```python
from pycaret.datasets import get_data
from pycaret.classification import *

# 1. 데이터 불러오기 (붓꽃 데이터)
data = get_data('iris')

# 2. PyCaret 환경 초기화
# html=False 옵션은 특정 환경에서 UI 충돌을 방지합니다. (기본값 True)
s = setup(data, target='species', session_id=123)

# 3. 모델 성능 비교 (자동 ML 시작)
best_model = compare_models()

# 4. 결과 출력 확인
print(best_model)
```
