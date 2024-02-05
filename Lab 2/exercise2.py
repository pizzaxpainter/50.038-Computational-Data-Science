import pandas as pd

set1 = pd.Series(['this', 'is', 'a', 'sample'])
term_count1 = pd.Series([1, 1, 2, 1])
set2 = pd.Series(['this', 'is', 'another', 'example'])
term_count2 = pd.Series([1, 1, 2, 3])

df1 = pd.DataFrame({'Term': set1, 'Term Count': term_count1})
df2 = pd.DataFrame({'Term': set2, 'Term Count': term_count2})

print(df1)
print(df2)

import math
def tf(w,d):
    idx = d['Term'].tolist().index(w)
    term_count = d['Term Count'][idx]

    max_frequency = d['Term Count'].max()

    return term_count / max_frequency

def idf(w,d):
        total = 0 
        if ((df1['Term'] == w).any() and (df2["Term"] == w).any()):
            idf = math.log10(total / 2)
        else:
            idf = math.log10(total / 1)
        return idf
    
def tfidf(w,d):
     tf = tf(w,d)
     idf = idf(w,d)
     return tf * idf

print(tf('is', df2))

  
  
