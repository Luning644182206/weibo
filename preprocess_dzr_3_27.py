# -*- coding: utf-8 -*-
from Text_emotion import senti_python
import string
import os
import pickle
class Weibo:
    def __init__(self,mid,uid,content,time,like=0,comment=0,forward=0,positive=0):
        self.mid = mid
        self.uid = uid
        self.content = content
        self.time = time
        self.like = like
        self.comment = comment
        self.forward = forward
        self.positive = positive
    def showWeibo(self):
        print("mid:",self.mid)
        print("uid:",self.uid)
        print("content:",self.content)
        print("time:",self.time)
        print("like:",self.like)
        print("comment:",self.comment)
        print("forward:",self.forward)
        print("positive:",self.positive)
path = 'weibo_train_data.txt'
file=open(path,encoding="utf-8")
lines=file.readlines()
rows=len(lines)
print(rows)
dict = {}
sum = 0
userList = list()
daySet = set()
for line in lines:
    line=line.strip().split('\t')
    # dict[line[0]] =
    # positive =
    # 有一个数据没有7个属性，就不考虑了
    if len(line) == 7:
        content = line[6]
        weibo = Weibo(line[1],line[0],line[6],line[2],line[5],line[4],line[3])
        if line[0] not in dict:
            dict[line[0]] = []
            userList.append(line[0])
        day = line[2].split(' ')[0]
        daySet.add(day)
        dict[line[0]].append(weibo)
        sum = sum+1
print(len(dict.keys()))  # 37263个用户
print(sum) # 1229617
# print(userList)
# print(daySet)
# for user in dict.keys():
#     weiboList = dict[user]
#     for weibo in weiboList:
#         content = weibo.content
#         positive = senti_python.sentiment_score(senti_python.sentiment_score_list(content))
#         weibo.positive = positive
# print(len(dict[userList[2580]])) # 该用户发了167个微博
# # data = '天之禁送红包壕礼# 《天之禁》5.15不限号开测。差点被剁手，还好我用0.252秒成功躲过，还抢到了0.29元红包~一亿玩家挚爱网游大作果然豪气！点击领红包： http://t.cn/RABmxgZ'
# #
# # print(senti_python.sentiment_score(senti_python.sentiment_score_list(data)))
dict[userList[2580]][0].showWeibo()
#'2015-04-15'
def getWeiboAtDay(day = '',dict = {}):
    t_list = list()
    for user in dict.keys():
        weiboList = dict[user]
        for weibo in weiboList:
            time1 = weibo.time.split(' ')[0]
            if time1 == day:
                t_list.append(weibo)
    return t_list
# dayWeiboList = getWeiboAtDay('2015-04-15',dict) # '2015-04-15' 7641条微博
# print(len(dayWeiboList))
# dayWeiboList[0].showWeibo()
def saveWeiboListAtDay(day='',list=[]):
    path = "WeiboAtDay\\" + day + ".txt"
    # path = 'weibo-2015-04-15.txt'
    f = open(path,"wb+")
    pickle.dump(list, f)
    f.close()
# f = open(path,"rb+")

# weiboList = pickle.load(f)
# weiboList[0].showWeibo()
def loadWeiboListAtDay(day=''):
    path = "WeiboAtDay\\" + day + ".txt"
    if os.path.exists(path):
        f = open(path,"rb+")
        weiboList = pickle.load(f)
        weiboList[0].showWeibo()
        return  weiboList
    else:
        return []

# saveWeiboListAtDay('2015-04-15',dayWeiboList)
# loadWeiboListAtDay('2015-04-15')
def saveWeiboOfUser(user='',list=[]):
    path = "WeiboOfUser\\user_" + user + ".txt"
    # path = 'weibo-2015-04-15.txt'
    f = open(path,"wb+")
    pickle.dump(list, f)
    f.close()

def loadWeiboListAtDay(user=''):
    path = "WeiboOfUser\\" + day + ".txt"
    if os.path.exists(path):
        f = open(path,"rb+")
        weiboList = pickle.load(f)
        weiboList[0].showWeibo()
        return  weiboList
    else:
        return []
# #  保存每一个用户所发的微博到一个txt 文件里
# for user in dict.keys():
#     weiboList = dict[user]
#     saveWeiboOfUser(user,weiboList)
# #  每一天的所有微博存到一个文件里,方便以后分析每一天的热词
# for day in daySet:
#     weiboList = getWeiboAtDay(day,dict)
#     saveWeiboListAtDay(day,weiboList)