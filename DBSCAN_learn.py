from numpy import *
import numpy as np
import matplotlib.pyplot as plt

#DBSCAN的核心是，半径为1，minSample = 5，先以a个核心搜索，设有b，c，d点然后在a内的所有的点进行搜索
#DBSCAn计算量也特别的大，而且还暂用内存
 #数据集：每三个是一组分别是西瓜的编号，密度，含糖量
data = """
1,0.697,0.46,2,0.774,0.376,3,0.634,0.264,4,0.608,0.318,5,0.556,0.215,
6,0.403,0.237,7,0.481,0.149,8,0.437,0.211,9,0.666,0.091,10,0.243,0.267,
11,0.245,0.057,12,0.343,0.099,13,0.639,0.161,14,0.657,0.198,15,0.36,0.37,
16,0.593,0.042,17,0.719,0.103,18,0.359,0.188,19,0.339,0.241,20,0.282,0.257,
21,0.748,0.232,22,0.714,0.346,23,0.483,0.312,24,0.478,0.437,25,0.525,0.369,
26,0.751,0.489,27,0.532,0.472,28,0.473,0.376,29,0.725,0.445,30,0.446,0.459"""
data = data.strip().split(',')
data = [(float(data[i]),float(data[i+1])) for i in range(1,len(data),3)]
print(data)
#计算距离
def distance(a,b): #a b分别为元组
    return sqrt(pow(a[0]-b[0],2) + pow(a[1] - b[1],2))


#算法模型
def dbscan(dataSet,e,Minpts):#数据，半径和最小的个数
    T = set()
    for d in dataSet:
        if len([i for i in dataSet if distance(d,i) <= e]) >= Minpts:
            T.add(d) #可以作为核心的点的集合
    p = set(dataSet)  # 整个的数据集
    C = []  # 用来保存每个族
    k = 0  # 用来计数族的个数的

    i = 0
    while len(T):
        p_old = p.copy() #用来寄存数据 这里有个大坑，如果p_old = p 则无论p怎么变，p_old就怎么变会进入一个死循环，因为两个是只想的一个位置一个东西
        o = list(T)[np.random.randint(0,len(T))] #先随机的选取一个核心点
        p -=set(o) #从原始的数据中去掉o点
        Q = []#用来存放以一个核心点搜集到的所有的数据
        Q.append(o)
        while len(Q):
            q = Q[0] #取出Q内的一个点

            Nq = [i for i in dataSet if distance(i,q) <= e] #求以q为核心的附近的所有的点
            if len(Nq) >= Minpts: #如果点的个数大于设置的阈值
                S = p & set(Nq) #取出所有的交集
                Q += list(S) #将S即q附近的所有的点加入到Q中
                p -= S #减去所有的已经满足条件的点
                i += 1
            Q.remove(q)


        k += 1 #用来记录簇的个数
        Ck = list(p_old - p) #是以q点为中心的所有的密度可达的所有的点
        T -= set(Ck) #从T中删除所有已经包含在q内的核心的点
        C.append(Ck)
    print(C)
    return C
C = dbscan(data,0.11,5)
#绘画
def draw(C):
    colValue = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
    num_cluster = len(C)
    for i in range(num_cluster):
        X = []
        y = [] #每个族的x，y坐标
        for j in range(len(C[i])):#第i个族的里面的元素
            X.append(C[i][j][0])
            y.append(C[i][j][1])
        plt.scatter(X,y,color = colValue[i],label = i,marker = 'x')
    plt.legend()
    plt.show()
draw(C)