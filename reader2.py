from GoogleNews import GoogleNews
import pandas as pd

news = GoogleNews(start='11/01/2022',end='11/29/2022',lang='es',encode='utf-8')
news.search("Banco Central de Chile",)
result = news.result()
data = pd.DataFrame.from_dict(result)
data = data.drop(columns=["img"])
data.head()
for res in result:
  print("Title : ",res["title"])
  print("News : ",res["desc"])
  print("Detailed news : ",res["link"])