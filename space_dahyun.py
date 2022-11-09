import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    layout='wide',
    initial_sidebar_state='collapsed',
    page_title='(주)항공우주산업다현정보',
    page_icon='🚀'

)
st.sidebar.subheader('항공우주산업에 대한 정보들입니다.')
st.subheader('🚀항공우주산업🚀')

data = [
    {
        'category' : '경제 성장 기여 효과_항우(연)',
        'url': 'https://www.kari.re.kr/images/kor/sub01/achievement-effect.jpg',
        'name': '경제 성장 기여 효과',
        'content': '항우(연) 30년 연구개발 투자에 대한 경제성장 기여효과는 약 18조 7,761억원 (경제성장분 대비 1.48%)으로 산출',
    },
    {
        'category': '과학 기술적 성과_항우(연)',
        'url': 'https://cdn-icons-png.flaticon.com/512/888/888042.png',
        'name': '논문 및 학술 발표',
        'content': '총 19,761건 국내 항공우주 전체의 9% 차지',
    },
    {
        'category': '과학 기술적 성과_항우(연)',
        'url': 'https://png.pngtree.com/element_our/png/20181226/capabilityheadhumanknowledgeskill-line-icon--vector-isol-png_283474.jpg',
        'name': '특허 및 지식재산권',
        'content': '총 5,802건 국내 항공우주 전체의 약 54% 차지',
    },
    {
        'category': '과학 기술적 성과_항우(연)',
        'url': 'https://previews.123rf.com/images/indomercy/indomercy1611/indomercy161100159/66966999-%EB%8B%B9%EC%8B%A0%EC%9D%98-%EA%B8%B0%EC%88%A0-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-%EB%94%94%EC%9E%90%EC%9D%B8-%EB%A7%88%EC%8A%A4%ED%84%B0.jpg',
        'name': '기술이전',
        'content': '기업당 연매출 평균 3.9억원 향상 이전기술 영향도 20.3% 기술이전 기업대상 설문조사 결과',
    },
    {
        'category': '과학 기술적 성과_항우(연)',
        'url': 'https://previews.123rf.com/images/yupiramos/yupiramos1612/yupiramos161216287/68032893-%EA%B3%B5%EC%9E%A5-%EA%B3%B5%EC%9E%A5-%EA%B2%A9%EB%A6%AC-%EB%90%9C-%EC%95%84%EC%9D%B4%EC%BD%98-%EB%B2%A1%ED%84%B0-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-%EB%94%94%EC%9E%90%EC%9D%B8.jpg',
        'name': '기반시설 구축',
        'content': '총 29개 기반구축시설의 외부활용율 증가(27.1%→75.5%) *위성 및 항공분야에 한함',
    },
    {
        'category': '과학 기술적 성과_항우(연)',
        'url': 'https://thumb.silhouette-ac.com/t/12/125daebdd25848b425dc4ac0659fe8b8_w.jpeg',
        'name': '기술수준 증가',
        'content': '약 47.1%p 증가 1999년대 초, 미국(100)대비',
    },
    {
        'category': '분야별 참여 현황',
        'url': 'http://www.kasp.or.kr/common/images/industry/condition_01-1.jpg',
        'name': '분야별 참여 현황',
        'content': '매년 우주산업 각 분야의 참여 기관 수가 증가하는 추세로 위성활용 서비스 및 장비 분야에 가장 많은 기관이 참여, 산업체 : 주로 위성활용 서비스 및 장비 분야에 가장 많이 참여, 연구기관·대학 : 과학연구 분야 및 위성활용 분야 등 우주분야 전영역에 걸쳐 고루 참여 중',
    },

    {
        'category': '참여 기관의 소재 분포 현황',
        'url': 'http://www.kasp.or.kr/common/images/industry/condition_02-1.jpg',
        'name': '참여기관의 소재 분포현황',
        'content': '산업체 : 전체 우주산업체 절반이상 (58%) 이 수도권에 분포, 연구기관 : 전체 연구기관의 76%가 충청권(40%) 및 수도권(36%)에 분포',
    },
    {
        'category': '우주 분야 활동 금액',
        'url': 'http://www.kasp.or.kr/common/images/industry/condition_02_02-1.jpg',
        'name': '우주 분야 활동 금액',
        'content': '2019년 기준',
    },
    {
        'category': '우주 분야 수출입현황',
        'url': 'http://www.kasp.or.kr/common/images/industry/condition_04-1.jpg',
        'name': '우주 분야 수출입현황',
        'content': '총 수출액은 전년 대비 5,037억 원(28.3%p) 감소한 것으로 조사되었으며, 수출액의 감소는 위성방송통신 분야의 위성수신 셋톱박스 관련 수출액 감소가 주요 요인이다. 총 수입액은 전년 대비 2,061억 원(35.0%p) 감소한 것으로 조사되었으며, 수입액의 감소는 기업체의 위성방송통신 분야 수입액 감소가 주요 요인이다. 무역수지는 2013년 이후로 지속적으로 흑자를 기록하고 있지만, 2019년에는 전년대비 감소',
    },
    {
        'category': '국가별 수출입 현황',
        'url': 'http://www.kasp.or.kr/common/images/industry/condition_03_01-1.jpg',
        'name': '국가별 수·출입 현황',
        'content': '2014~2020 ',
    },
    {
        'category': '우주분야 인력 현황',
        'url': 'http://www.kasp.or.kr/common/images/industry/condition_04_02.jpg',
        'name': '우주 분야 인력현황',
        'content': '매년 우주분야 종사자 수는 꾸준히 증가중 절반 이상의 인력(53.5%)이 위성활용 분야에 종사하고 있음',
    },
    {
        'category': '우주분야 투자 현황',
        'url': 'http://www.kasp.or.kr/common/images/industry/condition_05_02.jpg',
        'name': '우주 분야 투자 현황',
        'content': '2014년 이후 시설투자비의 급증으로 전년대비 투자금액이 대폭 상승 세부 투자분야로는 시설투자비가 가장 큰 비중을 차지',
    },
    {
        'category': '총괄 로드맵',
        'url': "http://www.kasp.or.kr/common/images/industry/roadmap01.jpg",
        'name': ' ',
        'content': ' '
    },
    {
        'category': '발사체 분야',
        'url': "http://www.kasp.or.kr/common/images/industry/roadmap02.jpg",
        'name': '지향점',
        'content': '1.5톤급 위성 저궤도 발사능력 확보 후, 3톤급 정지궤도 발사까지 확대'
    },
    {
        'category': '발사체 분야',
        'url': "http://www.kasp.or.kr/common/images/industry/roadmap03.jpg",
        'name': '5년간 로드맵',
        'content': '2018~2022 '
    },
    {
        'category': '위성체 및 위성활용 분야',
        'url': "http://www.kasp.or.kr/common/images/industry/roadmap04.jpg",
        'name': '지향점',
        'content': '다양한 첨단위성 개발‧활용으로 국민생활 향상과 4차 산업혁명 견인'
    },
    {
        'category': '위성체 및 위성활용 분야',
        'url': "http://www.kasp.or.kr/common/images/industry/roadmap05.jpg",
        'name': '5년간 로드맵',
        'content': '2018~2022'
    },
    {
        'category': '우주 탐사 분야',
        'url': "http://www.kasp.or.kr/common/images/industry/roadmap06.jpg",
        'name': '지향점',
        'content': '한국형발사체를 이용한 달착륙, 소행성귀환 임무 완수와 전략기술 확보'
    },
    {
        'category': '우주 탐사 분야',
        'url': "http://www.kasp.or.kr/common/images/industry/roadmap07.jpg",
        'name': '5년간 로드맵',
        'content': '2018~2022'
    },
    {
        'category': '위성 항법 분야',
        'url': "http://www.kasp.or.kr/common/images/industry/roadmap08.jpg",
        'name': '지향점',
        'content': '지역항법시스템 구축을 통한 위성기반 위치·시각 인프라 자립성 강화 및 초정밀 위치정보, 시각정보 제공'
    },
    {
        'category': '위성 항법 분야',
        'url': "http://www.kasp.or.kr/common/images/industry/roadmap09.jpg",
        'name': '5년간 로드맵',
        'content': '2018~2022'
    },
    {
        'category': '우주 산업 분야',
        'url': "http://www.kasp.or.kr/common/images/industry/roadmap10.jpg",
        'name': '지향점',
        'content': '민간의 참여를 유도하여 우주시장 형성 초기단계로 진입'
    },
    {
        'category': '우주 산업 분야',
        'url': "http://www.kasp.or.kr/common/images/industry/roadmap11.jpg",
        'name': '5년간 로드맵',
        'content': '2018~2022'
    },
]




# st.sidebar.subheader('무엇이 궁금한가요?')
page = st.sidebar.radio('무엇이 궁금한가요?', ('우주 산업 특징', '국내 산업 현황', '국가 우주 개발'))

if page == '우주 산업 특징':
    menu1 = st.sidebar.selectbox('우주 산업 특징', ('과학 기술적 성과_항우(연)', '경제 성장 기여 효과_항우(연)'))
if page == '국내 산업 현황':
    menu1 = st.sidebar.selectbox('국내 산업 현황', ('분야별 참여 현황', '참여 기관의 소재 분포 현황', '우주 분야 활동 금액', '국가별 수출입 현황', '우주분야 인력 현황', '우주분야 투자 현황'))
if page == '국가 우주 개발':
    menu1 = st.sidebar.selectbox('국가 우주 개발', ('총괄 로드맵', '발사체 분야', '위성체 및 위성활용 분야', '우주 탐사 분야', '위성 항법 분야', '우주 산업 분야',))


def card_list(menu):
    result = ''
    for value in data:
        if value['category'] == menu:
            result = result +f"""
    <div class="col">
        <div class="card" style="width: 75rem;">      
          <img src="{value['url']}" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">{value['name']}</h5>
            <p class="card-text">{value['content']}</p>
          </div>
        </div>
    </div>
    """

    return result




components.html(
    f"""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>

    <div class="container">
      <div class="row">
            {card_list(menu = menu1)}
      </div>
    </div>

    """, height=6550
)

