import numpy as np
from PIL import Image
from wordcloud import WordCloud 
from matplotlib import pyplot as plt
text = open('shakespare.txt',encoding='utf-8').read()
word_cloud = WordCloud(max_font_size=50,max_words=100,background_color='white',min_word_length=1).generate(text)

plt.imshow(word_cloud)
plt.axis('off')

masque = np.array(Image.open("python-wordcloud.png"))
word_cloud_2 = WordCloud(max_font_size=50,max_words=1000,mask=masque,background_color='white',min_word_length=1).generate(text)
plt.imshow(word_cloud_2)
plt.axis('off')

plt.show()

