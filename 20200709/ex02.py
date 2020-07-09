import re
from urllib.request import urlopen

# ハムレット第1幕第2場
URL = "http://shakespeare.mit.edu/hamlet/hamlet.1.2.html"

# ディクショナリdicを用いてkeyの数を数える関数
def count_by_dic(dic, key):
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1

# ディクショナリdicにkeyがあればその値を，なければ0を返す関数
def count_in_dic(dic, key):
    if key in dic:
        return dic[key]
    else:
        return 0

# main
with urlopen(URL) as fh:
    count = {}    # 文字毎の出現数を覚えるディクショナリ
    for rawline in fh:
        line = rawline.decode("utf-8").rstrip()                 # 文字コード変換，改行除去
        match = re.search(r"<A NAME=[0-9]+>(.+)</A>", line)     # せりふを取り出す正規表現
        if match:                                               # 一致するものがあれば
            sentence = match.group(1).lower()                   # 一致した部分を小文字に変換
            sentence = re.sub(r"[.,?!:;]", "", sentence)        # 記号を削除
            for word in sentence.split():                       # 単語ごとに分割，繰り返し
                for char in list(word):                         # 文字毎に分割，繰り返し
                    count_by_dic(count, char)                   # 文字をカウント

for alphabet in "abcdefghijklmnopqrstuvwxyz":                   # a〜zについて繰り返す
    print(alphabet, "...", count_in_dic(count, alphabet))
   