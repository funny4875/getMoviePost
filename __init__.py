import requests
from lxml import etree
#引入colab中秀圖函式
import cv2
def getMoviePosterImg(title):
  if len(title)>25:
    i=title.rfind(' ')
    if i>=0:title=title[:i]
    i=title.rfind(':')
    if i>=0:title=title[:i]

  url = 'https://movies.yahoo.com.tw/moviesearch_result.html?keyword='+title
  res = requests.get(url)
  xpath='//*[@id="content_l"]/div/div[1]/ul/li[1]/div[1]/a/div/img/@src'  
  # 請求並接收
  response = requests.get(url)
  content = response.content.decode()
  # 把string轉為hmtl node tree，回傳根節點
  html = etree.HTML(content)
  if len(html.xpath(xpath))==0:return []
  imurl = html.xpath(xpath)[0]
  img = requests.get(imurl)  # 下載圖片
  with open("test.jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
    file.write(img.content)  # 寫入圖片的二進位碼
  img=cv2.imread('test.jpg')
  print(img.size)
  return cv2.resize(img,(150,200))
  # response.status_code 回傳狀態 200,404,...
  # response.content 回傳內容編碼 (純二進制)
  # response.text 回傳Unicode型數據
  # 解析內容 (轉為string)
