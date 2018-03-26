# -*- coding: utf-8 -*-

class Weibo:
    def __init__(self,mid,uid,content,time,like=0,comment=0,forward=0):
        self.mid = mid
        self.uid = uid
        self.content = content
        self.time = time
        self.like = like
        self.comment = comment
        self.forward = forward
    def showWeibo(self):
        print("mid:",self.mid)
        print("uid:",self.uid)
        print("content:",self.content)
        print("time:",self.time)
        print("like:",self.like)
        print("comment:",self.comment)
        print("forward:",self.forward)
path = 'weibo_train_data.txt'
file=open(path,encoding="utf-8")
lines=file.readlines()
rows=len(lines)
print(rows)
dict = {}
sum = 0
userList = list()
for line in lines:
    line=line.strip().split('\t')
    # dict[line[0]] =
    # 有一个数据没有7个属性，就不考虑了
    if len(line) == 7:
        weibo = Weibo(line[1],line[0],line[6],line[2],line[5],line[4],line[3])
        if line[0] not in dict:
            dict[line[0]] = []
            userList.append(line[0])
        dict[line[0]].append(weibo)
        sum = sum+1
print(len(dict.keys()))  # 37263个用户
print(sum) # 1229617
print(userList)
print(len(dict[userList[2580]])) # 该用户发了167个微博



