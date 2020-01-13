import newspaper
# 词频统计库
import collections
# numpy库
import numpy as np
# 结巴分词
import jieba
# 词云展示库
import wordcloud
# 图像处理库
from PIL import Image
# 图像展示库
import matplotlib.pyplot as plt

# 获取文章
article = newspaper.Article('https://news.sina.com.cn/o/2019-11-28/doc-iihnzahi3991780.shtml')
# 下载文章
article.download()
# 解析文章
article.parse()
# 对文章进行 nlp 处理
article.nlp()
# nlp 处理后的文章拼接
article_words = "".join(article.keywords)
# 精确模式分词(默认模式)
seg_list_exact = jieba.cut(article_words, cut_all=False)
# 存储分词结果
object_list = []
# 移出的词
rm_words = ['迎', '以来', '将']
# 迭代分词对象
for word in seg_list_exact:
    if word not in rm_words:
        object_list.append(word)
# 词频统计
word_counts = collections.Counter(object_list)
# 获取前 10 个频率最高的词
word_top10 = word_counts.most_common(10)
# 词条及次数
for w, c in word_top10:
    print(w, c)

# 词频展示
# 定义词频背景
mask = np.array(Image.open('bg.jpg'))
wc = wordcloud.WordCloud(
    # 设置字体格式
    font_path='C:/Windows/Fonts/simhei.ttf',
    # 背景图
    mask=mask,
    # 设置最大显示的词数
    max_words=100,
    # 设置字体最大值
    max_font_size=80
)
# 从字典生成词云
wc.generate_from_frequencies(word_counts)
# 从背景图建立颜色方案
image_colors = wordcloud.ImageColorGenerator(mask)
# 显示词云
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
plt.savefig('wc.jpg')
# 显示图像
plt.show()

