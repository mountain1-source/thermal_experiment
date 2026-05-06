from water_physic import get_water_properties
from experiment01 import calcuate_kesi
import math
import os
import numpy as np

if __name__=='__main__':
    ts = 0 # 沸腾水饱和温度
    t1 =0 # 管内壁温度
    V = 0 # 管子ab间电压降
    I = 0 # 管子ab间工作电流

    # input_data = [104.1, 104.6, 49.3, 20.4]
    # input_data = [104.2, 104.9, 72.3, 30.0]
    # input_data = [104.1, 105.2, 96.2, 40.0]
    # input_data = [104.1, 105.9, 119.4, 49.9]
    # input_data = [104.2, 106.4, 142.3, 59.8]
    # ts, t1, V, I = input_data
    print("the writer:Junyu Pan, Guibin Zhang, Kai Zhang")
    print("\n")
    print("实验二 大容器内水沸腾换热实验")
    print("请以此输入单组的数据，沸腾水饱和温度，管内壁温度，管子ab间工作电压降， 管子ab间工作电流。如104.1, 104.6, 49.3, 20.4 但数字间的逗号用英文")
    input_data = input("请输入单组数据")
    ts, t1, V, I = map(float, input_data.split(','))

    fi = I*(V*1e-3)  # 管子放热量

    L = 0.075  # 0.75米 工件ab间的长度
    namda = 16.3  # 16.3W/(m*K) 不锈钢管导热系数
    r1 = 0.5  # 0.5mm 管子内半径
    r2 = 1.5  # 1.5mm 管子外半径
    kesi = 0  # 计算系数
    kesi = calcuate_kesi(L, namda, r1, r2)
    t2 = t1 - kesi*fi # 管子外壁温度
    q = fi/(2*math.pi*(r2*1e-3)*L) # 管子表面热负荷
    delat_t = t2-ts # 沸腾放热温差
    h = q/delat_t  # 水沸腾放热系数

    print("管子放热量fi:", fi)
    print("管子外壁温度t2:", t2)
    print("管子表面热负荷q:", q)
    print("沸腾放热温差delat_t:",delat_t)
    print("水沸腾放热系数h:",h)

    print("\n")
    print("\n")
    print("试验管直径:0.003m")
    print("工作段长度L",L,"m")
    print("工作段面积A:",2*math.pi*(r2*1e-3)*L,"平方米")
    print("系数kesi:",kesi)

    print("按任意键返回")
    os.system("pause")



