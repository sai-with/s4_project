## 크롤링해야하는 카테고리별 링크 dict

BASE_URL = "https://hotping.co.kr/product/"
cat = ['new', 'dresses', 'outwear', 'tops', 'bottoms', 'skirts', 'sale']
link = ['list_new.html?cate_no=25', 'list.html?cate_no=26', 'list.html?cate_no=27', 'list.html?cate_no=29',\
    'list.html?cate_no=31', 'list.html?cate_no=535', 'list.html?cate_no=447']
link_dict = dict(zip(cat, link))