import jieba#引入jieba分词库
txt = open("白鹿原.txt", "r", encoding="utf-8").read()#打开文本
words = jieba.lcut(txt)#进行分词处理并形成列表
print(type(words))
counts = {}#构造字典，逐一遍历words中的中文单词进行处理，并用字典计数
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())#转换列表类型并排序
items.sort(key=lambda x:x[1], reverse=True)
for i in range(15):#输出前15位单词
    word, count = items[i]
    print("{0:<10}{1:<5}".format(word, count))
