


import requests
import numpy as np
#import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator




Url=("https://api.pushshift.io/reddit/search/comment/?fields=body&limit=25000&link_id=c2vixn")
print(Url)

res=requests.get(Url)
data_arr=res.json()['data']

c_string=" ".join(comment['body'] for comment in data_arr)
print(len(data_arr))
wc=WordCloud().generate(c_string)
image=wc.to_file("new.png")

'''plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()'''

# store to file
#wc.to_file("img/wine.png")
