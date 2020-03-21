from wordcloud import WordCloud
import numpy as np, jieba
from PIL import Image

def jieba_():
    # 打开评论数据文件
    content = open('comment.csv', 'rb').read()
    # jieba 分词
    word_list = jieba.cut(content)
    words = []
    # 过滤掉的词
    remove_words = ['以及', '不会', '一些', '那个', '只有',
                    '不过', '东西', '这个', '所有', '这么',
                    '但是', '全片', '一点', '一部', '一个',
                    '什么', '虽然', '一切', '样子', '一样',
                    '只能', '不是', '一种', '这个', '为了']
    for word in word_list:
        if word not in remove_words:
            words.append(word)
    global word_cloud
    # 用逗号隔开词语
    word_cloud = '，'.join(words)

def cloud():
    # 打开词云背景图
    cloud_mask = np.array(Image.open('bg.jpg'))
    # 定义词云的一些属性
    wc = WordCloud(
        # 背景图分割颜色为白色
        background_color='white',
        # 背景图样
        mask=cloud_mask,
        # 显示最大词数
        max_words=100,
        # 显示中文
        font_path='./fonts/simhei.ttf',
        # 最大尺寸
        max_font_size=80
    )
    global word_cloud
    # 词云函数
    x = wc.generate(word_cloud)
    # 生成词云图片
    image = x.to_image()
    # 展示词云图片
    image.show()
    # 保存词云图片
    wc.to_file('anjia.png')

jieba_()
cloud()