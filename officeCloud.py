from os import path, getcwd
from PIL import Image
import numpy as np
import re

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator 
import matplotlib.pyplot as plt 
import pandas as pd 
 
d = getcwd()
df = pd.read_csv(r"the-office-lines - scripts.csv", encoding ="utf-8", index_col = 0) 

print(df.head())
  
comment_words_michael = '' 
comment_words_jim = '' 
comment_words_pam = '' 
comment_words_dwight = '' 
stopwords = set(STOPWORDS) 
punctuation = "!?@#$%^&*<>,.?/\";:\\"

mask_michael = np.array(Image.open(path.join(d, "michael.png")))
mask_jim = np.array(Image.open(path.join(d, "jim.png")))
mask_pam = np.array(Image.open(path.join(d, "pam.png")))
mask_dwight = np.array(Image.open(path.join(d, "dwight.png")))

for ind in df.index:
    line = str(df['line_text'][ind]);
    newLine = ""
    # if(ind<10):
    #     print(line)
    for i in range(len(line)):
        if(line[i] in punctuation):
            newLine += " "
        else:
            newLine += line[i]
    newLine = re.sub(r"[\(\[].*?[\)\]]", " ", newLine) 
    tokens = newLine.split()
    if(str(df['speaker'][ind]) == "Michael"):
        comment_words_michael += " ".join(tokens)+" "
    if(str(df['speaker'][ind]) == "Jim"):
        comment_words_jim += " ".join(tokens)+" "
    if(str(df['speaker'][ind]) == "Pam"):
        comment_words_pam += " ".join(tokens)+" "
    if(str(df['speaker'][ind]) == "Dwight"):
        comment_words_dwight += " ".join(tokens)+" "

wordcloud_michael = WordCloud(width = 800, height = 800, 
                background_color ='white', mask = mask_michael, 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words_michael)

wordcloud_jim = WordCloud(width = 800, height = 800, 
                background_color ='white', mask = mask_jim, 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words_jim) 

wordcloud_pam = WordCloud(width = 800, height = 800, 
                background_color ='white', mask = mask_pam, 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words_pam) 

wordcloud_dwight = WordCloud(width = 800, height = 800, 
                background_color ='white', mask = mask_dwight, 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words_dwight)  
  
# plot the WordCloud image
image_colors_michael = ImageColorGenerator(mask_michael)                        
plt.figure(figsize = (8, 8)) 
plt.imshow(wordcloud_michael.recolor(color_func=image_colors_michael), interpolation="bilinear")
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 

image_colors_jim = ImageColorGenerator(mask_jim)                        
plt.figure(figsize = (8, 8)) 
plt.imshow(wordcloud_jim.recolor(color_func=image_colors_jim), interpolation="bilinear")
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 

image_colors_pam = ImageColorGenerator(mask_pam)                        
plt.figure(figsize = (8, 8)) 
plt.imshow(wordcloud_pam.recolor(color_func=image_colors_pam), interpolation="bilinear")
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 

image_colors_dwight = ImageColorGenerator(mask_dwight)                        
plt.figure(figsize = (8, 8)) 
plt.imshow(wordcloud_dwight.recolor(color_func=image_colors_dwight), interpolation="bilinear")
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 
