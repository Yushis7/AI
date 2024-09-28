import pandas as pd

# data = {'Name':['Alice','Bob','Charlie'],
#         'Age':[25,30,22],
#         'City':['New York','San Francisco','Los Angelos']}

# df = pd.DataFrame(data)

# # print("Original DataFrame:")
# print(df)


# s1 = pd.Series([10,20,30,40])
# print(s1)
# print(s1.sum()) #총합
# print(s1.mean()) #평균값


# s2 = pd.Series(['분식이','쏘니','홍길동','변사또'],index=['2','3','4','되나'])
# print(s2)

s3 = pd.Series({'name':'김분식','age':30,'gender':'male','job':'분석가'})
# print(s3)
# print(s3['name'])
# print(s3[2:])
# print(s3[:2])
# print(s3[s3=='분석가'])


s4 = pd.Series(['국어','수학','사회','과학'])


s5 = pd.DataFrame([[10,20,30,40],
                   ['철수','영희','지수','은희']])
# print(s5)

df1= pd.DataFrame([[1000,'과자','2019-12-31','반품'],
                   [2000,'음료','2020-03-02','정상'],
                   [3000,'아이스크림','2020-02-03','정상'],
                   [1000,'과자','2019-12-31','반품']],
                   columns=['가격','종류','판매일자','반품여부'])
# print(df1)
# print(df1['가격'].sum())
# print(df1['가격'].mean()) #평균
# print(df1[['가격']]) #데이터 프레임 형태로 보려면 [] 한 번 더 감싸기
# print(df1[['가격','종류']])


# https://www.youtube.com/watch?v=q4UFSZPjLyo&list=PLhdHuKlSngGxvB0bMYigcn8zwD4zmewtt&index=7


