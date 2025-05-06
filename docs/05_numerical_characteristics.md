# 5. 随机变量的数字特征 (Numerical Characteristics of Random Variables)

本章介绍用于描述随机变量概率分布某些方面特性的数字，如期望、方差等。

## 5.1 期望 (Expectation / Mean)

随机变量的**数学期望 (Mathematical Expectation)**，简称期望或均值，是随机变量取值的加权平均，权重为其对应的概率。它刻画了随机变量取值的平均水平。

*   **离散型随机变量的期望**：设离散型随机变量 X 的分布律为 P(X=x<sub>k</sub>) = p<sub>k</sub>, k=1, 2, ...
    若级数 Σ<sub>k</sub> |x<sub>k</sub>|p<sub>k</sub> 收敛，则期望定义为：
    \[ E(X) = \sum_k x_k p_k \]
*   **连续型随机变量的期望**：设连续型随机变量 X 的 PDF 为 f(x)。
    若积分 ∫<sub>-∞</sub><sup>+∞</sup> |x|f(x) dx 收敛，则期望定义为：
    \[ E(X) = \int_{-\infty}^{+\infty} x f(x) dx \]
*   **随机变量函数的期望**：设 Y = g(X)。
    *   若 X 为离散型： E(Y) = E(g(X)) = Σ<sub>k</sub> g(x<sub>k</sub>)p<sub>k</sub>
    *   若 X 为连续型： E(Y) = E(g(X)) = ∫<sub>-∞</sub><sup>+∞</sup> g(x)f(x) dx
    (上述期望存在的条件是对应的级数或积分绝对收敛)

**期望的性质**：
1.  E(c) = c (c 是常数)
2.  E(cX) = cE(X) (c 是常数)
3.  E(X + Y) = E(X) + E(Y) (无论 X, Y 是否独立)
4.  若 X, Y 相互独立，则 E(XY) = E(X)E(Y)。 (注意：反之不一定成立，不相关不代表独立)

## 5.2 方差与标准差 (Variance and Standard Deviation)

**方差 (Variance)** 刻画了随机变量取值相对于其期望值的离散程度。记作 D(X) 或 Var(X)。
\[ D(X) = E[ (X - E(X))^2 ] \]

*   **离散型随机变量的方差**：
    \[ D(X) = \sum_k (x_k - E(X))^2 p_k \]
*   **连续型随机变量的方差**：
    \[ D(X) = \int_{-\infty}^{+\infty} (x - E(X))^2 f(x) dx \]

计算方差的常用公式：
\[ D(X) = E(X^2) - [E(X)]^2 \]

**标准差 (Standard Deviation)** 是方差的算术平方根，记作 σ(X) 或 SD(X)。
\[ \sigma(X) = \sqrt{D(X)} \]
标准差与随机变量本身具有相同的量纲。

**方差的性质**：
1.  D(c) = 0 (c 是常数)
2.  D(cX) = c²D(X) (c 是常数)
3.  D(X + c) = D(X) (c 是常数)
4.  若 X, Y 相互独立，则 D(X + Y) = D(X) + D(Y) 且 D(X - Y) = D(X) + D(Y)。 (注意：不独立时 D(X+Y) = D(X) + D(Y) + 2Cov(X,Y))

## 5.3 协方差与相关系数 (Covariance and Correlation Coefficient)

*   **协方差 (Covariance)**：度量两个随机变量 X 和 Y 之间线性关系的强度和方向。记作 Cov(X, Y)。
    \[ Cov(X, Y) = E[ (X - E(X))(Y - E(Y)) ] \]
    计算协方差的常用公式：
    \[ Cov(X, Y) = E(XY) - E(X)E(Y) \]
    协方差的性质：
    1.  Cov(X, Y) = Cov(Y, X)
    2.  Cov(aX, bY) = ab Cov(X, Y) (a, b 是常数)
    3.  Cov(X<sub>1</sub> + X<sub>2</sub>, Y) = Cov(X<sub>1</sub>, Y) + Cov(X<sub>2</sub>, Y)
    4.  D(X ± Y) = D(X) + D(Y) ± 2Cov(X, Y)
    5.  若 X, Y 相互独立，则 Cov(X, Y) = 0。 (注意：Cov(X,Y)=0 仅表示 X,Y 不相关，不一定独立，除非是二维正态分布)

*   **相关系数 (Correlation Coefficient)**：是标准化的协方差，消除了量纲的影响，用于度量两个随机变量之间线性相关程度。记作 ρ<sub>XY</sub> 或 Corr(X, Y)。
    \[ \rho_{XY} = \frac{Cov(X, Y)}{\sqrt{D(X)D(Y)}} \]
    (假设 D(X) > 0, D(Y) > 0)
    相关系数的性质：
    1.  |ρ<sub>XY</sub>| ≤ 1
    2.  |ρ<sub>XY</sub>| = 1 的充要条件是存在常数 a, b (a≠0) 使得 P(Y = aX + b) = 1，即 X 和 Y 之间存在完美的线性关系。
        *   若 ρ<sub>XY</sub> = 1，称为完全正相关。
        *   若 ρ<sub>XY</sub> = -1，称为完全负相关。
    3.  若 ρ<sub>XY</sub> = 0，称 X 和 Y 不相关。

## 5.4 矩与中心矩 (Moments and Central Moments)

*   **k 阶原点矩 (k-th Origin Moment)**： α<sub>k</sub> = E(X<sup>k</sup>)
    *   一阶原点矩 α<sub>1</sub> = E(X) 即为期望。
*   **k 阶中心矩 (k-th Central Moment)**： μ<sub>k</sub> = E[(X - E(X))<sup>k</sup>]
    *   一阶中心矩 μ<sub>1</sub> = 0。
    *   二阶中心矩 μ<sub>2</sub> = D(X) 即为方差。
    *   三阶中心矩 μ<sub>3</sub> 与分布的偏度有关。
    *   四阶中心矩 μ<sub>4</sub> 与分布的峰度有关。

偏度 (Skewness) 和 峰度 (Kurtosis) 是描述概率分布形状特征的两个重要指标。
*   **偏度**： S = μ<sub>3</sub> / σ³，度量分布的对称性。S=0 对称，S>0 右偏 (正偏)，S<0 左偏 (负偏)。
*   **峰度**： K = μ<sub>4</sub> / σ⁴ - 3 (有时定义为 μ<sub>4</sub> / σ⁴)，度量分布尾部的厚度或峰部的尖峭程度。与正态分布相比，K>0 更尖峭厚尾 (leptokurtic)，K<0 更平缓薄尾 (platykurtic)，K=0 与正态分布峰度一致 (mesokurtic)。 