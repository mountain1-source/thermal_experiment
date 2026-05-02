import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# ==================== 1. 输入你的实验数据 ====================
print("the writer:Junyu Pan, Kimi")
input_str = input("请输入一组雷利数，用英文逗号分隔: ")
Ra = np.array([float(x.strip()) for x in input_str.split(',')])

input_str2 = input("请输入一组努谢特数，用英文逗号分隔: ")
Nu = np.array([float(x.strip()) for x in input_str2.split(',')])
# Ra = np.array([3.4857, 5.9687, 6.6860, 7.0548, 7.8869])  # 雷利数
# Nu = np.array([5086.92, 6508.31, 9608.13, 13790.18, 17209.15])  # 努谢特数

# ==================== 2. 最小二乘法计算 ====================
# 对数转换: lg(Nu) = a + m * lg(Ra)
log_Ra = np.log10(Ra)
log_Nu = np.log10(Nu)

# 构造矩阵并求解: [1, lg(Ra)] * [a, m]^T = lg(Nu)
A = np.vstack([np.ones_like(log_Ra), log_Ra]).T
b = log_Nu
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

a, m = x[0], x[1]
C = 10**a  # C = 10^a

# ==================== 3. 拟合优度 R² ====================
log_Nu_pred = a + m * log_Ra
SS_res = np.sum((log_Nu - log_Nu_pred)**2)
SS_tot = np.sum((log_Nu - np.mean(log_Nu))**2)
R_squared = 1 - SS_res / SS_tot

# ==================== 4. 输出结果 ====================
print("=" * 50)
print("Least Squares Fitting Results")
print("=" * 50)
print(f"Nu = {C:.6f} * Ra^{m:.6f}")
print(f"lg(Nu) = {a:.6f} + {m:.6f} * lg(Ra)")
print(f"C  = {C:.6f}")
print(f"a  = {a:.6f}  (lg C)")
print(f"m  = {m:.6f}")
print(f"R² = {R_squared:.6f}")
print("=" * 50)

# ==================== 5. 绘图 ====================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 左图: 线性坐标
ax1 = axes[0]
ax1.scatter(Ra, Nu, color='red', s=80, zorder=5, label='Exp. Data')
Ra_fit = np.logspace(np.log10(Ra.min()), np.log10(Ra.max()), 200)
Nu_fit = C * Ra_fit**m
ax1.plot(Ra_fit, Nu_fit, 'b-', lw=2, label=f'Fit: $Nu={C:.3f}Ra^{{{m:.3f}}}$')
ax1.set_xlabel('Ra')
ax1.set_ylabel('Nu')
ax1.set_title('Nu vs Ra (Linear Scale)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# 右图: 对数坐标
ax2 = axes[1]
ax2.scatter(log_Ra, log_Nu, color='red', s=80, zorder=5, label='Exp. Data')
log_Ra_fit = np.linspace(log_Ra.min(), log_Ra.max(), 200)
log_Nu_fit = a + m * log_Ra_fit
ax2.plot(log_Ra_fit, log_Nu_fit, 'b-', lw=2, label=f'Fit: $lg(Nu)={a:.3f}+{m:.3f}lg(Ra)$')
ax2.set_xlabel('lg(Ra)')
ax2.set_ylabel('lg(Nu)')
ax2.set_title('lg(Nu) vs lg(Ra) (Log Scale)')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()