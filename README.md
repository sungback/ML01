# ML이해/분석활용 [Level.3]

제조 AX를 위한 머신러닝 모델링·분석 과정 (6일, 총 48시간) 실습 저장소입니다.

- 실습 환경: **Miniforge 가상환경 `ml_l3` (Python 3.11, PyCaret 3.3.2)** + Jupyter Notebook
- 실습 노트북: `work/student/day1 ~ day6/`
- 과제 안내: `work/assignment/assignment.md` (Word 파일 `assignment.docx`)

---

## 🛠️ 개발 환경 구성하기

6일 동안 쓰는 환경입니다. **1일차 1교시에 함께 설치**하며, 미리 해 오시면 더 좋습니다.

### 1. Miniforge 설치 및 설정
1. **Miniforge 다운로드 및 설치**
   - [Miniforge 다운로드 링크](https://github.com/conda-forge/miniforge/releases/latest)
   - 운영체제별 설치 파일을 다운로드한 후 설치를 진행합니다.

   | OS | 방법 |
   |---|---|
   | Windows | `Miniforge3-Windows-x86_64.exe` 를 내려받아 Next와 Yes를 눌러 설치 (기본 옵션 그대로) |
   | Mac | `Miniforge3-MacOSX-arm64.sh`(M1 이후) 또는 `x86_64`(인텔)를 내려받은 뒤 터미널에서 `bash 파일이름.sh` |

2. **Miniforge 프롬프트 실행**
   - Windows: `시작` > `모두` > `Miniforge3` > `Miniforge Prompt`
   - Mac: 터미널

### 2. 저장소 내려받기
이 저장소를 클론하거나, GitHub의 `Code` > `Download ZIP`으로 내려받아 압축을 풉니다.

### 3. 가상환경 생성 및 필요 라이브러리 설치

> 💡 **초보자 추천**: 아래 **방법 1 (yml 파일 사용)** 로 한 번에 설치하세요!

**방법 1. yml 파일로 한 번에 설치 (권장, 처음 한 번 5~10분)**
1. Miniforge Prompt에서 `work` 폴더로 이동한 뒤, 아래 명령어 한 줄로 가상환경 생성과 라이브러리 설치를 끝냅니다.
   ```bash
   cd work
   conda env create -f environment.yml
   ```
   Python 3.11과 PyCaret 3.3.2를 포함해 필요한 패키지가 `environment.yml`에 정해진 버전으로 설치됩니다.
2. 가상환경을 활성화합니다.
   ```bash
   conda activate ml_l3
   ```

**방법 2. 직접 설치**
1. 가상환경을 만들고 활성화합니다 (Python 3.11).
   ```bash
   conda create -n ml_l3 python=3.11 -y
   conda activate ml_l3
   ```
2. 필수 라이브러리를 설치합니다. 버전은 PyCaret 3.3.2와 함께 검증한 조합이므로 바꾸지 마세요.
   ```bash
   pip install pycaret==3.3.2 scikit-learn==1.4.2 pandas==2.1.4 numpy==1.26.4 scipy==1.11.4 matplotlib==3.7.5 lightgbm==4.7.0 pmdarima==2.0.4 joblib==1.3.2 duckdb==1.5.6 pyarrow==25.0.1 seaborn==0.13.2 koreanize-matplotlib==0.1.1 xlrd==2.0.2 statsmodels==0.15.0 factor_analyzer==0.5.1 mlxtend==0.23.4 imbalanced-learn==0.14.2 streamlit==1.64.0 jupyterlab==4.6.4 ipykernel==7.4.0
   ```

> ⚠️ 이전 과정에서 쓰던 `ds`(Python 3.12), `pycaret_env`(Python 3.10) 환경은 **쓰지 않습니다.** 이 과정은 PyCaret까지 포함한 `ml_l3` 환경 하나로 진행합니다.

### 4. 매 수업 시작할 때
```bash
conda activate ml_l3
cd work
jupyter lab
```
브라우저에서 Jupyter가 열리면 `student/day1/D1_01_환경점검.ipynb`부터 엽니다.

> 📌 **실습 환경 안내**
> 본 강의는 **Jupyter Notebook(JupyterLab)** 을 기준으로 진행됩니다.
> 아래 환경은 `ml_l3` 가상환경을 커널로 선택하면 사용할 수 있지만, 수업은 JupyterLab 기준으로 안내합니다.
> | 환경 | 특징 |
> |---|---|
> | [VS Code](https://code.visualstudio.com/) | 가볍고 확장성 높은 범용 에디터 (Jupyter 확장 설치 후 커널을 `ml_l3`로 선택) |
> | [PyCharm](https://www.jetbrains.com/pycharm/) | 강력한 Python 전용 IDE (Community 버전 무료) |
> | [Google Colab](https://colab.research.google.com/) | 설치 없이 브라우저에서 실행. 다만 이 과정의 패키지 버전(Python 3.11, PyCaret 3.3.2 등)과 달라 일부 노트북이 다르게 동작할 수 있습니다 |

### 5. Visual Studio Code 설치 (선택)
- [VS Code 다운로드 링크](https://code.visualstudio.com/download)
- 운영체제별 설치 파일을 다운로드한 후, Next와 Yes를 클릭하여 설치를 진행합니다.

### 6. 폴더 구성
| 폴더 | 내용 |
|---|---|
| `work/data/` | 수업 데이터 (`raw/`는 원본, 수정하지 않음) |
| `work/student/day1 ~ day6/` | 교시별 실습 노트북 (직접 입력 칸이 비어 있음) |
| `work/assignment/` | 과제 안내 (`assignment.md`, `assignment.docx`) |
| `work/environment.yml` | 가상환경 설치 파일 |

### 7. 자주 생기는 문제
| 증상 | 해결 |
|---|---|
| `conda`를 찾을 수 없음 | Windows는 일반 명령 프롬프트가 아니라 **Miniforge Prompt**에서 실행 |
| 노트북에서 `ModuleNotFoundError` | 오른쪽 위 커널이 `ml_l3` 환경인지 확인, 아니면 `conda activate ml_l3` 후 `jupyter lab` 다시 실행 |
| 그래프 한글이 네모로 깨짐 | 노트북 첫 셀의 `import koreanize_matplotlib` 를 실행했는지 확인 |
| Streamlit 앱이 데이터를 못 찾음 | 터미널에서 **노트북이 있는 폴더로 이동한 뒤** `streamlit run 앱.py` 실행 |

---

## 🤖 AutoML (PyCaret) 사용법

PyCaret 3.3.2는 `ml_l3` 환경에 이미 들어 있으므로 **별도 가상환경이 필요 없습니다.** (6일차에서 사용)

**참고 소스 (PyCaret 사용 예제)**
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

**PyCaret 공부 사이트**
* [1위 PyCaret 소개 Low-code 머신러닝의 시작](https://wikidocs.net/306399)

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

### Streamlit 배포 주소
| 앱 | 짧은 주소 | 실제 주소 |
|---|---|---|
| KOSPI 추세 투자 분석 | https://tinyurl.com/kotuja | https://kdz8ro4tbw2pk2tjsvdgcf.streamlit.app/ |
| 업비트 코인 분석 | http://tinyurl.com/cointuja | https://paymqcbygcojz4gwfbogbu.streamlit.app/ |
| 미국 주식 상승 추세 분석 | https://tinyurl.com/mijusik | https://pxquwya8k9bfmyumuj9wcy.streamlit.app/ |

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
- [Github 저장소](https://github.com/sungback/ML01)의 etc 폴더에서 `kaggle-notebook-translation-helper-main.zip` 다운로드
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

## 📱 AI로 5분 만에 앱 개발 : onspace.ai

코딩 없이도 AI를 활용해 앱을 직접 만들고, 수익화·배포까지 한 번에 할 수 있는 OnSpace AI 관련 영상 모음입니다.

* [(코딩X) 앱 외주 맡기지 마세요. AI가 5분 만에 진짜 앱 만들어줍니다](https://www.youtube.com/watch?v=wKwvzXFP2Wg&t=24s)
* [간단한 앱도 돈내고 쓰고 계셨나요? 이제는 직접 만드는 시대 — OnSpace로 앱 제작, 수익화, 배포까지 한번에!](https://www.youtube.com/watch?v=43heYabCgMI)
* [요즘 잘나가는 유튜버들이 몰래 앱으로 갈아타고 있는 이유](https://www.youtube.com/watch?v=Uazp3vRusbQ)
* [가장 빠르게 앱을 제작하고 배포하는 법 — OnSpaceAI](https://www.youtube.com/watch?v=N2Z0BsIpcIc)
