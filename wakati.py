import csv
import pandas as pd
import os
import MeCab
import ipadic


CHASEN_ARGS = r' -F "%m\t%f[7]\t%f[6]\t%F-[0,1,2,3]\t%f[4]\t%f[5]\n"'
CHASEN_ARGS += r' -U "%m\t%m\t%m\t%F-[0,1,2,3]\t\t\n"'
wakati = MeCab.Tagger(ipadic.MECAB_ARGS + CHASEN_ARGS)

data = pd.read_csv("0.csv")
t = data['レビュー内容'][0]

result = wakati.parse(t)

result = result.split("\n")

for line in result:
    wakati_text = line.split("\t")
    if wakati_text[0] != "EOS" and wakati_text[0] != "":
        print(wakati_text[0])

from time import time
t1 = time()
CHASEN_ARGS = r' -F "%m\t%f[7]\t%f[6]\t%F-[0,1,2,3]\t%f[4]\t%f[5]\n"'
CHASEN_ARGS += r' -U "%m\t%m\t%m\t%F-[0,1,2,3]\t\t\n"'
wakati = MeCab.Tagger(ipadic.MECAB_ARGS + CHASEN_ARGS)
t2 = time()
print(t2-t1)
def extract_hinshi(text:str, hinshi:str,wakati):
    CHASEN_ARGS = r' -F "%m\t%f[7]\t%f[6]\t%F-[0,1,2,3]\t%f[4]\t%f[5]\n"'
    CHASEN_ARGS += r' -U "%m\t%m\t%m\t%F-[0,1,2,3]\t\t\n"'
    wakati = MeCab.Tagger(ipadic.MECAB_ARGS + CHASEN_ARGS)

    result = wakati.parse(text)
    for line in result:
        wakati_text = line.split("\t")
        if wakati_text[0] != "EOS" and wakati_text[0] != "":
            pass

