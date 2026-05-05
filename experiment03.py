from air_physics import get_air_properties
import math
import numpy as np
import os

if __name__ =='__main__':
    # my_data = [174.0, 198.8, 207.9, 28.0, 25.7, 4.4, 232.9]
    # my_data = [199.4, 226.1, 234.2, 29.8, 26.2, 3.7, 234.1]
    # my_data = [219.8, 248.0, 254.6, 31.5, 26.7, 2.9, 233.9]
    # my_data = [238.3, 267.8, 273.6, 31.8, 26.8, 2.1, 234.7]
    print("the writer:Junyu Pan, Guibin Zhang, Kai Zhang")
    print("\n")
    print("实验三 强迫对流单管管外换热系数测定实验")
    print("请以此输入单组的数据，管壁温度T1, 管壁温度T2,管壁温度T3,空气温度T5, 空气温度T6,空气动压差，加热器功率。"
          "如174.0, 198.8, 207.9, 28.0, 25.7, 4.4, 232.9 但数字间的逗号用英文")
    input_data = input("请输入单组数据")
    T1, T2, T3, T5, T6, delt_h, P = map(float, input_data.split(','))
    # T1, T2, T3, T5, T6, delt_h, P = my_data #T1-T4是管壁的温度。T5 ,T6空气温度。delt_h空气动压差 mmH2O。P 加热器功率 W
    tw = float(np.mean([T1, T2, T3]))  # 管壁温度的平均值
    tf = float(np.mean([T5, T6]))    # 空气平均温度

    D = 0.03 # 管径 单位米
    L = 0.29 # 管长 单位米
    F = math.pi*D*L  # 管壁换热面积 单位平方米
    Tg = tw -tf # 过余温度， 管壁平均温度-空气平均温度
    h = P/(F*Tg)  #  平均换热系数

    props = get_air_properties((tw+tf)/2.0)
    p, nameda, v = props[0], props[1], props[2]  # p 空气的密度， nameda 1e2空气的导热系数， v 1e6空气的运动粘度
    Uce = math.sqrt(2*9.81*delt_h/p) # 测试段流速  米每秒
    Ushi = ((0.09*0.11)*Uce)/((0.19*0.29)-(math.pi*((D/2)**2)))  # 试验段流速 米每秒
    tm = (tw+tf)/2.0   # 定性温度
    Nu = h*D/(nameda*1e-2) # 努谢尔系数
    Re = Ushi*D/(v*1e-6)  # 雷诺数

    print("管壁的平均温度tw:",tw)
    print("空气的平均温度tf", tf)
    print("管壁的换热面积F", F)
    print("过余温度Tg",Tg)
    print("平均换热系数h",h)
    print("测试段流速Uce",Uce)
    print("试验段流速Ushi", Ushi)
    print("定性温度tm",tm)
    print("空气的导热系数nameda", nameda*1e-2)
    print("空气的运动粘度v",v*1e-6)
    print("努谢尔系数Nu",Nu)
    print("雷诺数Re",Re)

    print("按任意键返回")
    os.system("pause")











