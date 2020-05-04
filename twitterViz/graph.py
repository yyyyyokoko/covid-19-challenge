import os
import pandas as pd
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud

plt.rcParams.update({'figure.max_open_warning': 0})

basepath = "covid19_twitter/dailies/"

for subdir, dirs, files in os.walk(basepath):
    date = subdir.split('/')[-1]
    if len(date) == 10:
        #read file
        biname = subdir + '/' + date + '_top1000bigrams.csv'
        triname = subdir + '/' + date + '_top1000trigrams.csv'
        bi = pd.read_csv(biname)
        tri = pd.read_csv(triname)

        #clean data
        combined = pd.concat([bi, tri]).sort_values(by='counts', ascending = False).reset_index(drop = True)
        words = set(nltk.corpus.words.words())
        combined = combined.dropna()

        #preprocess
        newdict = {}
        for i in range(0, len(combined)):
            val = combined.iloc[i,0]
            deci = [word for word in val.split() if word in words] 
            if len(val.split()) == len(deci):
                newdict[" ".join(deci)] = combined.iloc[i,1]
        
        #top words
        # temp = pd.DataFrame(newdict.items(), columns = ['word', 'count'])[0:50]
        # filename = date + '.csv'
        # temp.to_csv(filename, index = False)

        #wordcloud
        wordcloud = WordCloud(width=1600, height=800, max_font_size=200, background_color="white")
        wordcloud.generate_from_frequencies(frequencies=newdict)
        plt.figure(figsize=(20,10))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        filename = date +'.png'
        plt.savefig(filename, bbox_inches='tight', pad_inches=0)
        