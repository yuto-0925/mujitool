import streamlit as st
import mujichicken

st.title('Instagram-Auto By mujichicken:)')

#設定ファイルからの読み込み
setting_list = []

username=st.text_input('Username:')
password=st.text_input('Password:')
tagName=st.text_input('ハッシュタグ:')
likedMax=st.number_input('自動いいね数:')

answer = st.button('スタート')

if answer == True:
     mujichicken.py.insta_auto_like(username, password, tagName)
     st.write('自動いいねスタート')
else:
     st.write('')