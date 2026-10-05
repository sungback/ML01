# pip install yfinance
import streamlit as st
import yfinance as yf
from datetime import datetime
import pandas as pd

st.title('📈 간단 주식 차트 (Yahoo Finance)')

# 1. 입력부
col1, col2 = st.columns(2)
with col1:
    ticker = st.text_input('종목코드', value='005930.KS', help="삼성전자는 005930.KS, 애플은 AAPL")
with col2:
    start_date = st.date_input('시작일', value=datetime(2023, 1, 1))

# 2. 데이터 가져오기 및 출력
if ticker:
    # auto_adjust=True: 배당/분할이 반영된 수정종가 사용
    # df = yf.download(ticker, start=start_date) # <== 멀티 인덱스가 기본값
    # 데이터를 가져올 때 처음부터 1층으로 가져오도록 설정하는 옵션 사용
    df = yf.download(ticker, start=start_date, multi_level_index=False)
    # print(df)
    if not df.empty:
        # 데이터가 MultiIndex인 경우를 대비해 'Close' 컬럼만 안전하게 추출
        if isinstance(df.columns, pd.MultiIndex):
            # 아래의 멀티 인덱스 중에 아래 부분인 'Ticker' 레벨(1번 인덱스)을 삭제
            # Price        Close        High        Low        Open        Volume
            # Ticker       005930.KS    005930.KS   005930.KS  005930.KS   005930.KS
            df.columns = df.columns.droplevel(1)
            data = df['Close']
        else:
            data = df['Close']
        print(data)
        st.line_chart(data)
    else:
        st.error("데이터를 찾을 수 없습니다. 종목코드 뒤에 .KS(코스피) 또는 .KQ(코스닥)를 확인하세요.")
