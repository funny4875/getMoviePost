import requests
from lxml import etree
#引入colab中秀圖函式
import cv2
def getMoviePosterImg(title):
  # if len(title)>25:
  #   i=title.rfind(' ')
  #   if i>=0:title=title[:i]
  #   i=title.rfind(':')
  #   if i>=0:title=title[:i]
  
  url = 'https://www.movieposterdb.com/search?q='+title
  res = requests.get(url)
  # 請求並接收
  response = requests.get(url)
  content = response.content.decode()
  # 把string轉為hmtl node tree，回傳根節點
  html = etree.HTML(content)
  #xpath='/html/body/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/a/img'
  xpath='/html/body/div[1]/div/div/div[1]/div[3]//img[contains(@data-src,".jpg")]'
  
  imgs = html.xpath(xpath)
  if len(html.xpath(xpath))==0:return []
  imurl = html.xpath(xpath)[0].get('data-src')
  print(imurl)
  img = requests.get(imurl)  # 下載圖片
  with open("test.jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
      file.write(img.content)  # 寫入圖片的二進位碼
  img=cv2.imread('test.jpg')
  return img
