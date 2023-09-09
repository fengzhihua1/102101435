import jieba
import wordcloud
import imageio
butterfly = imageio.imread('butterfly.png')
# 词云 统计哪些词语出现次数比较多, 次数出现的越多的话 字体显示越大
f = open('msg.txt', encoding='utf-8')
txt = f.read()
# print(txt)
txt_list = jieba.lcut(txt)
string = ' '.join(txt_list)
wc = wordcloud.WordCloud(
    width=500, # 宽度
    height=500, # 高度
    background_color='white',#背景颜色
    font_path='msyh.ttc',#字体文件
    mask=butterfly,
    stopwords={'了', '这个', '啊', '我', '的'},#停用词
)
wc.generate(string)
wc.to_file('output3.png')