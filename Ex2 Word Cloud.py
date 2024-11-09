!pip install wordcloud

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

with open("/content/drive/My Drive/PS3 Ex 2.txt", "r") as file:
  text = file.read()

wordcloud = WordCloud( width=800,
height=400, background_color="lightyellow",
stopwords=set(STOPWORDS),
min_font_size=10, ).generate(text)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
