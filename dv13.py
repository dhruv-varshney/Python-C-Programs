import pandas as pd
p1 = pd.Series({'name':'dhv',
                'item':'qwe',
                'cost':'34'  })
p2 = pd.Series({'name':'sanu',
                'item':'dfgh',
                'cost':'56'})
df = pd.DataFrame([p1, p2], index = ['store 1', 'store2'])
a =df.head()
print(a)
b = df.loc[:,['name','cost']]
print(b)
c = df['item']
print(c)
d = df.drop('store 1')
print(d)
