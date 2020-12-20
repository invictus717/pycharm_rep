import wordcloud, jieba
c = wordcloud.WordCloud(font_path="msyh.ttc")
s = "新时代中国特色社会主义思想是全党全国人民为实现中华民族伟大复兴而奋斗的行动指南"
c.generate(" ".join(jieba.lcut(s)))
c.to_file("outfile.png")