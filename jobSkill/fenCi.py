from jieba import analyse
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np

fenCi = {}
ciYunArray = []
def main():

    # 负责过滤的词语
    filterWords = ['熟悉', '熟练', '经验', '优先', '应用开发', '相关', '工作', '开发', '能力', '负责', '技术', '具备', '精通', '数据', 'ETC']

    # 结巴分词基于 TF-IDF 算法的关键词
    tfidf = analyse.extract_tags

    for zpInfo in open('sh.txt', 'r', encoding='utf-8'):

        if zpInfo.strip() == '':
            continue
        # 详情数据是用&&&分割的
        infos = zpInfo.split("&&&")
        words = tfidf(infos[-1])

        words = [x.upper() for x in words if x.upper() not in filterWords]

        for word in words:
            word = word.upper()
            num = fenCi.get(word, 0) + 1
            fenCi[word] = num

    print(sorted(fenCi.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
    print('分出了' + str(len(fenCi)) + '了词语')


def getWordCloud():
   path_img = "python.jpg"
   background_image = np.array(Image.open(path_img))

   wordcloud = WordCloud(
       font_path="/System/Library/Fonts/STHeiti Light.ttc", # 字体
       background_color="white",
       mask=background_image).generate(" ".join(list(fenCi.keys())))
   image_colors = ImageColorGenerator(background_image)
   plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
   plt.axis("off")
   plt.show()


if __name__ == '__main__':
    main()
    getWordCloud()
