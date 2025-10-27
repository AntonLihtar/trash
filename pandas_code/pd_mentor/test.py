import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv('students_performance.csv')
print(df.head(10))

print(df.dtypes)
print(len(df))
print(df.shape)
print(len(df[df['gender'] == 'male']))
print(len(df[df['gender'] == 'female']))

# print(df['gender'].value_count()['female'])

gender_distr = df['gender'].value_counts()['female']
print(gender_distr)
#
# gender_dist.sum()
# gender_dist['female']



df = pd.read_csv('students_performance.csv')

# Подсчёт по полу
gender_distr = df['gender'].value_counts()

# Построение столбчатой диаграммы
gender_distr.plot(kind='bar', color=['#4A90E2', '#F06292'])

plt.title('Распределение студентов по полу')
plt.xlabel('Пол')
plt.ylabel('Количество студентов')
plt.show()

gender_distr.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Распределение по полу')
plt.ylabel('')
plt.show()

