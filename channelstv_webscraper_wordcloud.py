from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup as bs


url1 = 'https://www.channelstv.com/category/politics'

# Retrieve page with the requests module
response = requests.get(url1)

# Create a Beautiful Soup object
soup1 = bs(response.text, "html5lib")
type(soup1)

summation = ""
for index in range(0,6):
	#extract the text from the h3 tag using text.strip()
	news_title = soup1.find_all('h3', class_='item-heading item-heading_md item-heading_lead')[index].text.strip()
	summation += news_title

cloud = WordCloud(background_color="white").generate(summation)

plt.imshow(cloud)
plt.axis('off')
plt.show()