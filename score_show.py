import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
#读取文件
data = pd.read_excel("D:/河北工业大学2019复试名单.xls",encoding="utf-8")
#获取专业课代码
list_daima=data["专业码"]
#获取专业课成绩
list_score=data["ywk2"]
#print(list_daima)
#print(list_score)
#print(list_daima[5])
#if list_daima[5]==70100:
   # print("right")
#用一个空数组来存放专业课为经济学的分数
list_jingjiscore=[]

for i in range(0,len(list_daima)):
    #获取专业课代码为020200（经济学）的分数、这里有坑需谨慎，Python中以0开头的被认为是8进制应当使用强制类型转换int（“number”）
    if list_daima[i] == int('020200'):
        list_jingjiscore.append(list_score[i])
    i=i+1
print(list_jingjiscore)

list_under90=[]
list_90_100=[]
list_100_110=[]
list_110_120=[]
list_120_130=[]
list_130_140=[]
list_140_150=[]
for i in range(0,len(list_jingjiscore)):
    if list_jingjiscore[i]<=90:
        list_under90.append(list_jingjiscore[i])
    elif list_jingjiscore[i]<=100:
        list_90_100.append(list_jingjiscore[i])
    elif list_jingjiscore[i]<=110:
        list_100_110.append(list_jingjiscore[i])
    elif list_jingjiscore[i]<=120:
        list_110_120.append(list_jingjiscore[i])
    elif list_jingjiscore[i]<=130:
        list_120_130.append(list_jingjiscore[i])
    elif list_jingjiscore[i] <= 140:
        list_130_140.append(list_jingjiscore[i])
    else:
        list_140_150.append(list_jingjiscore[i])
    i=i+1

print("专业课90分以下的人数为：",len(list_under90))
print("专业课90分-100分的人数为：",len(list_90_100))
print("专业课100分-110分的人数为：",len(list_100_110))
print("专业课110分-120分的人数为：",len(list_110_120))
print("专业课120分-130分的人数为：",len(list_120_130))
print("专业课130分-140分的人数为：",len(list_130_140))
print("专业课140分-150分的人数为：",len(list_140_150))

#计算平均分
sum = 0
for i in range(0,len(list_jingjiscore)):
    sum=sum+list_jingjiscore[i]
    i=i+1

average=int(sum/(len(list_jingjiscore)))

print("该学校的专业课的平均分为：",average,"分")

# 将全局的字体设置为黑体
plt.rcParams['font.family'] = 'SimHei'

x=["90分以下","90-100","100-110","110-120","120-130","130-140","140-150"]
y=[len(list_under90),len(list_90_100),len(list_100_110),len(list_110_120),len(list_120_130),len(list_130_140),len(list_140_150)]
p1 = plt.bar(x, height=y, width=0.5,color= "red", edgecolor = "black", log = False)
plt.xlabel("分数")#设置x轴标签
plt.ylabel("人数")#设置y轴标签
plt.title("河北工业大学2019年经济学在各分数段的人数分布")#设置图表标题
plt.text(0.01,16,"专业课平均分为")
#为每一个直方图添加说明文字
for a,b in zip(x,y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=14)
# 展示图形
plt.show()


x_1=["平均分"]
y_1=[average]
plt.figure()
plt.plot(x_1,y_1,":o",color="red")#点线
plt.xlabel("平均分")#设置x轴标签
plt.ylabel("分数")#设置y轴标签
plt.title("河北工业大学2019年经济学一志愿的专业课平均分 ")#设置图表标题
#为每一个直方图添加说明文字
for a,b in zip(x_1,y_1):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=14)
# 展示图形
plt.show()