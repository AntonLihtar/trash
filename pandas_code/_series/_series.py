import pandas as pd

s = pd.Series({
    'a': 21,
    'b': 22,
    'c': 33,
    'y': 24,
    'f': 19
},
    name='t1'
)

a = pd.Series([1, 2, 3])
print(s.equals(a))

res = s[s > 21]
print(res.info)

print(isinstance(res, pd.Series))  # True проверка на Series

print(s[(s != 22) & (s != 33)])

print(s[0:2])

print(list(s.items()))


def get(x, number):
    return x + number


print(s.apply(func=get, number=56))

print(s.describe())
