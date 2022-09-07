import streamlit as st

btn = st.button('버튼')

if btn:
    st.subheader('버튼 클릭')
else:
    st.subheader('안녕하세요')




text_contents = 'fileasdf'
st.download_button('다운로드', text_contents)




st.subheader('선택 과목')
a = st.checkbox('물리학')
b = st.checkbox('지구과학')
c = st.checkbox('생명과학')

text = ''

if a:
    text = text+'물리학, '

if b:
    text = text+'지구과학, '

if c:
    text = text+'생명과학'

st.write(f'{text}을 선택하셨습니다')




st.subheader('선택할 과목을 고르세요')
sub = st.radio('선택할 과목을 고르세요', ('미적분', '확률과 통계', '기하'))

if sub == '미적분':
    st.write('미적분')
elif sub == '확률과 통계':
    st.write('확률과 통계')
elif sub == '기하':
    st.write('기하')



option = st.selectbox('수학 선택과목은?', ('미분과 적분', '기하와 백터', '확률과 통계'))
st.write('당신의 선택은?', option)

options = st.multiselect(
    '과학 4과목 중 선택하세요',
    ['물리1', '화학1', '생명1', '지학1'],
    ['물리1', '화학1']
)

st.write('당신의 선택은?', options)


age = st.slider('당신의 나이는?', 0, 100, 25)
st.write('나이는', age)


color = st.select_slider(
    '당신이 좋아하는 색상을 선택하세요', options=['red', 'blue', 'green', 'black']
)
st.write('당신이 좋아하는 색상은', color)


number = st.number_input('숫자를 입력하세요', step=1)
st.write('현재 숫자는', number)
st.slider('당신이 선택한 숫자는',
          0, 100, number)


txt = st.text_area('글자를 입력하세요', '안녕하세요')
st.download_button('다운로드', txt)


import datetime
day= st.date_input('당신의 생일은', datetime.date(2006, 1, 1))
st.write('당신의 생일은', day)













































