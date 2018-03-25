# -*- coding: utf-8 -*-

#load data
file=open("weibo_train_data.txt",encoding="utf-8")

lines=file.readlines()
rows=len(lines)

dict={}
#key:uid  value:[max_f,min_f,all_f,max_c,min_c,all_c,max_l,min_l,all_l]

for line in lines:
    datamat=[0,0,0,0,0,0,0,0,0,1]
    line=line.strip().split('\t')
    if line[0] in dict:
        if dict[line[0]][0]<int(line[3]):
            dict[line[0]][0]=int(line[3])
        if dict[line[0]][1]>int(line[3]):
            dict[line[0]][1]=int(line[3])
        if dict[line[0]][3]<int(line[4]):
            dict[line[0]][3]=int(line[4])
        if dict[line[0]][4]>int(line[4]):
            dict[line[0]][4]=int(line[4])
        if dict[line[0]][6] < int(line[5]):
            dict[line[0]][6] = int(line[5])
        if dict[line[0]][7] > int(line[5]):
            dict[line[0]][7] = int(line[5])
        dict[line[0]][2] += int(line[3])
        dict[line[0]][5] += int(line[4])
        dict[line[0]][8] += int(line[5])
        dict[line[0]][9]+=1
    else:
        dict[line[0]]=datamat

#print(dict['731df6bc96df275923b455a8e2927da7'])
user_file=open('uer_total.txt','w',encoding="utf-8")
for uid in dict:
    write_str=str(uid)+' '
    for i in range(10):
        write_str+=str(dict[uid][i])+' '
    write_str+='\n'
    user_file.write(write_str)
user_file.close()
