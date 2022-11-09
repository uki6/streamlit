import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    layout='wide',
    initial_sidebar_state='collapsed',
    page_title='유기 동물의 쉼터',
    page_icon='🐹'
)


st.image('https://mir-s3-cdn-cf.behance.net/project_modules/disp/1f8b1e82249331.5d17ab0738dbe.jpg', caption=None, width=1200, use_column_width=100, clamp=False, channels="RGB", output_format="auto")
st.title('🐹 유기 동물의 쉼터')
st.subheader('유기 동물들을 돌보고 새로운 가족을 찾아주고 있습니다')
txt = st.text_area('문의 사항', '분양, 파양 관련 문의를 입력해주세요')
st.download_button('문의하기', txt)





data = [
    {
        'category': '강아지',
        'url': 'https://image.ajunews.com/content/image/2019/12/25/20191225170826943516.jpg',
        'name': '인절미',
        'content': '골든 리트리버',
        'price': '분양 가능'
    },
    {
        'category': '강아지',
        'url': 'https://image-notepet.akamaized.net/resize/620x-/seimage/20190325%2Fb6c456f4f6bf5d2560c26a780b7c36b9.jpg',
        'name': '심바',
        'content': '비숑 프리제',
        'price': '분양 완료'
    },
    {
        'category': '강아지',
        'url': 'https://mblogthumb-phinf.pstatic.net/MjAyMDEyMTZfMTUg/MDAxNjA4MDk2MzE0MzQx.Z8FcJNCtZLBHqhNWRY13ioeuuLx6lkLXVPpKMgNTWnEg.Xf9678xxIVWUCdIBYGlYH1duvuIpcWtfhh2XhEDoK9Ug.JPEG.alwayshappiness211/1608096313753.jpg?type=w800',
        'name': '행크',
        'content': '하이브리드 견',
        'price': '분양 가능'
    },
    {
        'category': '고양이',
        'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLIuchTusbpvxURK8q7U9Vaa4qxPoFVaBpJQ&usqp=CAU',
        'name': '먼지',
        'content': '러시안 블루',
        'price': '분양 가능'
    },
    {
        'category': '고양이',
        'url': 'https://img.danawa.com/images/descFiles/4/482/3481655_1509576344099.jpeg',
        'name': '뭉치',
        'content': '노르웨이 숲 고양이',
        'price': '분양 가능'
    },
    {
        'category': '햄스터',
        'url': 'http://image.dongascience.com/Photo/2019/12/fb4f7da04758d289a466f81478f5f488.jpg',
        'name': '토리',
        'content': '사파이어',
        'price': '분양 완료'
    },
    {
        'category': '햄스터',
        'url': 'https://imgscience.ytn.co.kr/sciencetv/jpg/vod1459/2021//202112071802272615_h.jpg',
        'name': '봄이',
        'content': '골든 햄스터',
        'price': '분양 가능'
    },
    {
        'category': '햄스터',
        'url': 'https://contents.creators.mypetlife.co.kr/content/uploads/2021/06/10101455/3628_8037_3014-384x384.jpg',
        'name': '겨울이',
        'content': '블랙아이 화이트',
        'price': '분양 가능'
    }
]


def card_list(menu):
    result = ''
    for value in data:
        if value['category'] == menu:
            result = result + f"""
      <div class="col">
      <div class="card" style="width: 18rem;">
          <img src="{value['url']}" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">{value['name']}</h5>
            <p class="card-text">{value['content']}</p>
          </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item">{value['price']}</li>
      </ul>
      </div>
      </div>
    """
    return result

st.sidebar.subheader('분양 정보')
menu = st.sidebar.selectbox('선택', ('강아지', '고양이', '햄스터'))



components.html(
    f"""
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>

        <div class="container">
      <div class="row">
        {card_list(menu=menu)}
          </ul>
            </div>
         </div>
     </div>
    """, height=2200
)




    # text_contents = """누구든지 동물을 사육·관리 또는 보호할 때에는 다음 각 호의 원칙이 준수되도록 노력하여야[1] 한다(제3조).
    #     동물이 본래의 습성과 신체의 원형을 유지하면서 정상적으로 살 수 있도록 할 것
    #     동물이 갈증 및 굶주림을 겪거나 영양이 결핍되지 아니하도록 할 것
    #     동물이 정상적인 행동을 표현할 수 있고 불편함을 겪지 아니하도록 할 것
    #     동물이 고통·상해 및 질병으로부터 자유롭도록 할 것
    #     동물이 공포와 스트레스를 받지 아니하도록 할 것
    #
    #     국가와 지방자치단체는 대통령령으로 정하는 민간단체에 동물보호운동이나 그 밖에 이와 관련된 활동을 권장하거나 필요한 지원을 할 수 있다(제4조 제3항).
    #
    #     모든 국민은 동물을 보호하기 위한 국가와 지방자치단체의 시책에 적극 협조하는 등 동물의 보호를 위하여 노력하여야 한다(같은 조 제4항)."""
    # st.download_button('download', text_contents)

