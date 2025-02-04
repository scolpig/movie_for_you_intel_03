import pandas as pd
from wordcloud import WordCloud
import collections
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_path = './malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family='NanumBarunGothic')

df = pd.read_csv('./crawling_data/cleaned_reviews.csv')
words = df.iloc[396, 1].split()
print(df.iloc[396, 0])

worddict = collections.Counter(words)
worddict = dict(worddict)
print(worddict)

wordcloud_img = WordCloud(
    background_color='white', font_path=font_path).generate_from_frequencies(worddict)
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud_img, interpolation='bilinear')
plt.axis('off')
plt.show()
















