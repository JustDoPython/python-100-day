import pandas as pd

#pd.set_option('display.width', None)

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

# 类型分析
types = d['type'].str.split('#', expand=True)
# print(types)

types.columns = ['zero', 'one', 'two', 'three', 'four']
types = types.apply(pd.value_counts).fillna(0)
types['counts'] = types.apply(lambda x: x.sum(), axis=1)
types = types.sort_values('counts', ascending=False)

print(types.head(10))

print('*' * 66)

# 国家分析
d['country'] = d['country'].str.replace(' ', '')
country = d['country'].str.split('/', expand=True)
print(country)

country.columns = ['zero', 'one', 'two', 'three', 'four', 'five']
country = country.apply(pd.value_counts).fillna(0)
country['counts'] = country.apply(lambda x: x.sum(), axis=1)
country = country.sort_values('counts', ascending=False)

print(country.head(10))

print('*' * 66)

# 导演分析
directors = d['director'].str.split('#').apply(pd.Series)
directors = directors.unstack().dropna().reset_index()
directors.columns.values[2] = 'name'
directors = directors.name.value_counts()

print(directors.head(10))

print('*' * 66)

# 演员分析
actor = d['actor'].str.split('#').apply(pd.Series)[[0, 1, 2]]
actor = actor.unstack().dropna().reset_index()
actor.columns.values[2] = 'name'
actor = actor.name.value_counts()

print(actor.head(10))

print('*' * 66)

# 标签分析
tags = d['tags'].str.split('#').apply(pd.Series)
tags = tags.unstack().dropna().reset_index()
tags.columns.values[2] = 'name'
tags = tags.name.value_counts()

print(tags.head(10))

print('*' * 66)

d['comments'] = d['comments'].str.split(' ').apply(pd.Series)[1]
d['comments'] = d['comments'].astype(int)

top10_comments_movie = d[['title', 'comments']].sort_values('comments', ascending=False).head(10).reset_index()
print(top10_comments_movie)

print('*' * 66)

d['votes'] = d['votes'].astype(int)
top10_votes_movie = d[['title', 'votes']].sort_values('votes', ascending=False).head(10).reset_index()
print(top10_votes_movie)