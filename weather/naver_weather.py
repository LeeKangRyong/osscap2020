from bs4 import BeautifulSoup as bs
import requests


html =  requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%82%A0%EC%94%A8&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%82%A0%EC%94%A8&tqi=UI4%2Fzlprvmsssh2CEaKssssssCG-319091')

soup = bs(html.text,'html.parser')

temperature = soup.findAll('span',{'class':'todaytemp'})
print(tempearture[0].text)

