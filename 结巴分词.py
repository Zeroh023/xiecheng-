
import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from imageio import imread

import warnings
warnings.filterwarnings("ignore")

# 2 读取文本文件，并使用lcut()方法进行分词
with open("D:\携程酒店\评论4.txt",encoding="utf-8") as f:
    txt = f.read()
txt = txt.split()
data_cut = [jieba.lcut(x) for x in txt]
data_cut
# 3 读取停用词
with open(r"D:\携程酒店\stopwords-master\scu_stopwords.txt",encoding="utf-8") as f1:
    stop = f1.read()
with open(r"D:\携程酒店\stopwords-master\cn_stopwords.txt", encoding="utf-8") as f2:
        stop2 = f2.read()
with open(r"D:\携程酒店\stopwords-master\hit_stopwords.txt", encoding="utf-8") as f3:
    stop3 = f3.read()
stop = stop +stop2+stop3
stop = stop.split()

stop = [" ","道","说道","说",'的','酒店','乐山','房间','携程','驿'] + stop
# 4 去掉停用词之后的最终词
s_data_cut = pd.Series(data_cut)
all_words_after = s_data_cut.apply(lambda x:[i for i in x if i not in stop])
# 5 词频统计
all_words = []
for i in all_words_after:
    all_words.extend(i)
word_count = pd.Series(all_words).value_counts()
# 6 词云图的绘制
# 1）读取背景图片
#back_picture = imread(r"G:\6Tipdm\wordcloud\jay1.jpg")

# 2）设置词云参数
wc = WordCloud(font_path="G:\\6Tipdm\\wordcloud\\simhei.ttf",
               width = 1920,
               height=1080,
               #background_color="pink",
               max_words=80,
              # mask=back_picture,
               max_font_size=200,
               random_state=42
              )
wc2 = wc.fit_words(word_count)

# 3）绘制词云图
plt.figure(figsize=(16,8))
plt.imshow(wc2)
plt.axis("off")
plt.show()
wc.to_file("ciyun.png")