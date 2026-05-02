from water_physic import get_water_properties
import math
import os
import numpy as np

def calcuate_kesi(L, namda, r1, r2):
    return 1.0/(4*math.pi*L*namda)*(1-(2*(r1**2)*math.log(r2/r1)/(r2**2-r1**2)))

if __name__ == "__main__":
    tf = 0  # 蒸馏水的温度
    t1 = 0  # 管内壁温度
    V = 0  # 工件ab间的工作电压
    I = 0  # 工件ab间的工作电流

    L = 0.075  # 0.075米 工件ab间的长度
    namda = 16.3  # 16.3W/(m*K) 不锈钢管导热系数
    r1 = 0.5  # 0.5mm 管子内半径
    r2 = 1.5  # 1.5mm 管子外半径

    # input_ata = np.random((5,4))
    # input_data = [81.6, 83.4, 47.9, 20.3]
    # input_data = [80.4, 82.8, 71.7, 30.4]
    # input_data = [78.6, 82.3, 93.7, 39.9]
    # input_data = [77.1, 82.6, 116.8, 50.0]
    # input_data = [75.8, 82.9,139.7, 59.9]
    print("the writer:Junyu Pan, Guibin Zhang, Kai Zhang, Anshuo Li")
    print("\n")
    print("实验一 自然对流传热系数测定实验")
    print("请以此输入单组的数据，蒸馏水温度，管内壁温度，ab间工作电压， ab间工作电流。如81.6, 83.4, 47.9, 20.3。但数字间的逗号用英文")
    input_data = input("请输入单组数据")
    tf, t1, V, I = map(float, input_data.split(','))
    V =V*1e-3 # 单位mv到V

    fi = I * V  # fi表示工件ab间的发热量
    kesi = 0  # 计算系数
    kesi = calcuate_kesi(L, namda, r1, r2)
    t2 = t1 - kesi * fi  # t2 管外壁温度
    delat_t = t2-tf # 温差
    h = fi/(2*math.pi*(r2*1e-3)*L*delat_t) # 换热系数
    tm = 1.0/2*(t2+tf) # 定性温度

    nameda_L =0 # 该温度下水的流体导热系数   1*W/(1e-2*m*K)
    a =0 # 体积膨胀系数   1/(1e-4 * K)
    nl = 0 # 流体动力粘度    1/(1e-5 * Pa*s)
    Cp = 0 # 流体比热容    kJ/(kg*K)
    p =0 # 流体密度        kg/me3
    props = get_water_properties(tf)
    nameda_L, a,nl, Cp, p = props[4],props[6], props[5], props[3], props[1]

    D = 0.003 # 管外径，单位米
    Nu = h*D/(nameda_L*1e-2) # 努谢特系数
    g = 10 # m/s**2
    Ra = ((p**2)*(Cp*1e3)*g*(a*1e-4)*(t2-tf)*(D**3))/((nameda_L*1e-2)*(nl*1e-5))


    print("发热量fi:",fi)
    print("管外壁温度t2",t2)
    print("温差delat_t:", delat_t)
    print("换热系数h:",h)
    print("定性温度tm:",tm)
    print("导热系数nameda_L:",nameda_L*1e-2)
    print("体积膨胀系数a:",a)
    print("流体动力粘度nl:",nl*1e-1)
    print("流体比热容Cp:",Cp)
    print("流体密度p:",p)
    print("努谢特数Nu:",Nu)
    print("雷利数Ra:", Ra)

    print("按任意键返回")
    os.system("pause")



