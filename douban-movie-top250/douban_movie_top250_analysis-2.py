import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
from wordcloud import WordCloud

my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
file = './doubanTop250.txt'
content = []

with open(file) as f:
    line = f.readline()
    while line:
        line = eval(line)
        content.append(line)
        line = f.readline()

d = pd.DataFrame(content)
print(d.info())
print(len(d.title.unique()))

print('*' * 66)

d['votes'] = d['votes'].astype(int)
d['comments'] = d['comments'].str.split(' ').apply(pd.Series)[1]
d['comments'] = d['comments'].astype(int)


def show_votes():
    plt.figure(figsize=(20, 5))
    plt.subplot(1, 2, 1)

    plt.scatter(d['votes'], d['index'])
    plt.xlabel('votes')
    plt.ylabel('rank')
    plt.gca().invert_yaxis()

    # 绘制直方图
    plt.subplot(1, 2, 2)
    plt.hist(d['votes'])
    plt.show()


def show_comments():
    plt.figure(figsize=(20, 5))
    plt.subplot(1, 2, 1)

    plt.scatter(d['comments'], d['index'])
    plt.xlabel('comments')
    plt.ylabel('rank')
    plt.gca().invert_yaxis()

    # 绘制直方图
    plt.subplot(1, 2, 2)
    plt.hist(d['comments'])

    d['comments'].corr(d['index'])
    plt.show()


def show_country():
    d['country'] = d['country'].str.replace(' ', '')
    country = d['country'].str.split('/', expand=True)
    # print(country)

    country.columns = ['zero', 'one', 'two', 'three', 'four', 'five']
    country = country.apply(pd.value_counts).fillna(0)
    country['counts'] = country.apply(lambda x: x.sum(), axis=1)
    country = country.sort_values('counts', ascending=False)

    plt.figure(figsize=(20, 6))
    plt.title("国家&电影数量", fontproperties=my_font)
    plt.xticks(fontproperties=my_font, rotation=45)
    plt.bar(country.index.values, country['counts'])
    plt.show()


def show_types():
    types = d['type'].str.split('#', expand=True)
    types.columns = ['zero', 'one', 'two', 'three', 'four']
    types = types.apply(pd.value_counts).fillna(0)
    types['counts'] = types.apply(lambda x: x.sum(), axis=1)
    types = types.sort_values('counts', ascending=False)
    types['counts'] = types['counts'].astype(int)

    plt.figure(figsize=(20, 6))
    plt.title("类型&电影数量", fontproperties=my_font)
    plt.xticks(fontproperties=my_font, rotation=45)
    plt.bar(types.index.values, types['counts'])
    plt.show()


def show_word_cloud():
    tags = d['tags'].str.split('#').apply(pd.Series)
    text = tags.to_string(header=False, index=False)

    wc = WordCloud(font_path='/System/Library/Fonts/PingFang.ttc', background_color="white", scale=2.5,
                   contour_color="lightblue", ).generate(text)

    # 读入背景图片
    wordcloud = WordCloud(background_color='white', scale=1.5).generate(text)
    plt.figure(figsize=(16, 9))
    plt.imshow(wc)
    plt.axis('off')
    plt.show()


# show_votes()
# show_comments()
# show_country()
# show_types()
# show_word_cloud()
