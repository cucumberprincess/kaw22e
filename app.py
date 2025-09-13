import streamlit as st
import os

def load_html(file_path):
    """
    지정된 경로의 HTML 파일을 읽어와서 반환합니다.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"파일을 찾을 수 없습니다: {file_path}")
        return None

def main():
    st.set_page_config(layout="wide")
    
    # htmls 폴더와 index.html 파일 경로 설정
    html_folder = "htmls"
    html_file = "index.html"
    file_path = os.path.join(html_folder, html_file)
    
    # HTML 파일 로드
    html_content = load_html(file_path)
    
    if html_content:
        # Streamlit 앱에 HTML 콘텐츠 표시
        st.components.v1.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
