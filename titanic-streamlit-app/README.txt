시작 > 모두 > Anaconda (anaconda3) > Anaconda Prompt

# 가상환경 만들기
conda create -n titanic-streamlit python=3.11 -y
conda activate titanic-streamlit

# github 에 업로드할 폴더(이미 존재한다고 가정)로 이동
cd ML01
pip install -r titanic-streamlit-app/requirements.txt
python titanic-streamlit-app/train_model.py
streamlit run titanic-streamlit-app/app.py

git add titanic-streamlit-app
git commit -m "Rebuild Titanic model with fixed package versions"
git push


share.streamlit.io
GitHub 계정으로 로그인합니다.

→ 새 앱 생성
→ Python 3.11 선택
→ Main file path: titanic-streamlit-app/app.py
→ Deploy

https://srkbuhsb52epss6rsfneii.streamlit.app/

