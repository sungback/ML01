import streamlit as st

# 애플리케이션의 제목을 설정하는 함수입니다. 가장 큰 글씨 크기로 표시됩니다.
st.title("Streamlit 웹 애플리케이션")

# 헤더(큰 제목) 를 설정하는 함수로, st.title()보다 크기가 작지만, 주요 섹션을 나누는 데 유용
st.header("이것은 헤더입니다")

# 서브헤더(소제목) 를 설정하는 함수로, st.header()보다 작은 크기의 제목입니다.
st.subheader("이것은 서브헤더입니다")

# Markdown 문법을 사용하여 텍스트를 포맷
st.markdown("# 큰 제목 (Markdown)")
st.markdown("**굵은 글씨**와 *이탤릭체* 사용 가능")

# 설명이나 주석을 다는 캡션을 추가하는 함수로, 작은 글씨로 표시됨
st.caption("이것은 캡션(설명)입니다.")

# Python 코드 또는 다른 프로그래밍 언어 코드를 하이라이팅된 코드 블록으로 출력
st.code("""
          def hello():
              print("Hello, Streamlit!")
        """, language="python")

# LaTeX 문법을 사용하여 수식을 렌더링
st.latex(r"E = mc^2")
