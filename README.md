"# ML01"

## 개발 환경 구성하기

### miniconda 다운로드
==> https://repo.anaconda.com/miniconda/

### conda update
conda update -n base -c defaults conda

### 기본 레포지토리를 conda-forge로 변경하기
conda config --add channels conda-forge
conda config --set channel_priority strict

### 가상환경 생성 명령
conda create -n ds python=3.11 -y
conda activate ds

### 라이브러리 설치
conda install -c conda-forge numpy pandas scipy matplotlib seaborn plotly jupyter scikit-learn statsmodels openpyxl xlrd beautifulsoup4 lxml requests tqdm xgboost lightgbm optuna catboost



### Visual Studio Code 다운로드 주소
https://code.visualstudio.com/download



### 인공지능 제조 플랫폼 주소
https://www.kamp-ai.kr/main

