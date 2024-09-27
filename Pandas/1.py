import pandas as pd
data_frame = pd.read_csv('data/friend_list.csv')
data_frame.head()

# 데이터프레임이 가지고 있는 함수의 예제입니다.
data_frame.head()

type(data_frame.job)

# 시리즈의 함수 예제입니다.
data_frame.job = data_frame.job.str.upper()
data_frame.head()

s1 = pd.core.series.Series(['one', 'two', 'three'])
s2 = pd.core.series.Series([1, 2, 3])

pd.DataFrame(data=dict(word=s1, num=s2))

df = pd.read_csv('data/friend_list.csv')

df

df.head()

df = pd.read_csv('data/friend_list_tab.txt', delimiter = "\t")

df.head()

df = pd.read_csv('data/friend_list_no_head.csv', header = None)


df.head()

df = pd.read_csv('data/friend_list_no_head.csv', header = None, names=['name', 'age', 'job'])


df.head()

friend_dict_list = [{'name': 'Jone', 'age': 20, 'job': 'student'},
         {'name': 'Jenny', 'age': 30, 'job': 'developer'},
         {'name': 'Nate', 'age': 30, 'job': 'teacher'}]
df = pd.DataFrame(friend_dict_list)


df.head()

from collections import OrderedDict

friend_ordered_dict = OrderedDict([ ('name', ['John', 'Jenny', 'Nate']),
          ('age', [20, 30, 30]),
          ('job', ['student', 'developer', 'teacher']) ] )
df = pd.DataFrame.from_dict(friend_ordered_dict)

df.head()


