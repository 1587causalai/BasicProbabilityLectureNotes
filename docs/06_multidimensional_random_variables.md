# 6. 多维随机变量及其分布 (Multidimensional Random Variables and Their Distributions)

本章将一维随机变量的概念推广到多维，重点讨论二维随机变量及其联合分布、边缘分布、条件分布和独立性。

## 6.1 二维随机变量 (Two-Dimensional Random Variables)

设 E 是一个随机试验，其样本空间为 Ω。设 X = X(ω) 和 Y = Y(ω) 是定义在 Ω 上的两个随机变量，则由它们组成的向量 (X, Y) 称为一个**二维随机变量**或随机向量。

*   **二维离散型随机变量**：如果 X 和 Y 都是离散型随机变量，则 (X, Y) 是二维离散型随机变量。
*   **二维连续型随机变量**：如果存在一个非负函数 f(x, y) 使得对任意区域 D，P((X,Y)∈D) = ∬<sub>D</sub> f(x,y) dxdy，则 (X, Y) 是二维连续型随机变量。

## 6.2 联合分布函数 (Joint Distribution Function)

对于二维随机变量 (X, Y)，其**联合分布函数 (Joint Cumulative Distribution Function, Joint CDF)** 定义为：
\[ F(x, y) = P(X \leq x, Y \leq y) \]

性质：
1.  0 ≤ F(x, y) ≤ 1
2.  F(x, y) 是关于 x 和 y 的单调不减函数。
3.  F(-∞, y) = 0, F(x, -∞) = 0, F(-∞, -∞) = 0
4.  F(+∞, +∞) = 1
5.  F(x, y) 右连续，即 F(x+0, y) = F(x, y), F(x, y+0) = F(x, y)。
6.  对于任意 x<sub>1</sub> < x<sub>2</sub>, y<sub>1</sub> < y<sub>2</sub>，P(x<sub>1</sub> < X ≤ x<sub>2</sub>, y<sub>1</sub> < Y ≤ y<sub>2</sub>) = F(x<sub>2</sub>, y<sub>2</sub>) - F(x<sub>1</sub>, y<sub>2</sub>) - F(x<sub>2</sub>, y<sub>1</sub>) + F(x<sub>1</sub>, y<sub>1</sub>) ≥ 0。

## 6.3 联合概率质量函数/概率密度函数 (Joint PMF/PDF)

*   **二维离散型随机变量的联合概率质量函数 (Joint PMF)**：
    设 (X, Y) 的所有可能取值为 (x<sub>i</sub>, y<sub>j</sub>)，其联合分布律或联合 PMF 为：
    \[ P(X=x_i, Y=y_j) = p_{ij}, \quad i, j = 1, 2, ... \]
    其中 p<sub>ij</sub> ≥ 0，且 Σ<sub>i</sub>Σ<sub>j</sub> p<sub>ij</sub> = 1。

*   **二维连续型随机变量的联合概率密度函数 (Joint PDF)**：
    如果二维随机变量 (X, Y) 的联合分布函数 F(x, y) 可以表示为：
    \[ F(x, y) = \int_{-\infty}^{x} \int_{-\infty}^{y} f(u, v) dv du \]
    则称 f(x, y) 为 (X, Y) 的联合概率密度函数 (Joint PDF)。
    性质：
    1.  f(x, y) ≥ 0
    2.  ∫<sub>-∞</sub><sup>+∞</sup>∫<sub>-∞</sub><sup>+∞</sup> f(x, y) dx dy = 1
    3.  在 f(x, y) 的连续点处，∂²F(x,y) / (∂x∂y) = f(x, y)。
    4.  P((X,Y) ∈ D) = ∬<sub>D</sub> f(x,y) dxdy，其中 D 是 xOy 平面上的一个区域。

## 6.4 边缘分布 (Marginal Distributions)

边缘分布描述的是多维随机变量中单个分量的分布。

*   **边缘分布函数 (Marginal CDF)**：
    F<sub>X</sub>(x) = P(X ≤ x) = P(X ≤ x, Y < +∞) = F(x, +∞)
    F<sub>Y</sub>(y) = P(Y ≤ y) = P(X < +∞, Y ≤ y) = F(+∞, y)

*   **边缘概率质量函数 (Marginal PMF)** (对于离散型)：
    P(X=x<sub>i</sub>) = p<sub>i·</sub> = Σ<sub>j</sub> p<sub>ij</sub>
    P(Y=y<sub>j</sub>) = p<sub>·j</sub> = Σ<sub>i</sub> p<sub>ij</sub>

*   **边缘概率密度函数 (Marginal PDF)** (对于连续型)：
    f<sub>X</sub>(x) = ∫<sub>-∞</sub><sup>+∞</sup> f(x, y) dy
    f<sub>Y</sub>(y) = ∫<sub>-∞</sub><sup>+∞</sup> f(x, y) dx

## 6.5 条件分布 (Conditional Distributions)

条件分布描述的是在给定一个随机变量（或多个随机变量）取特定值的条件下，另一个随机变量（或其余随机变量）的概率分布。

*   **离散型条件分布**：
    在 Y=y<sub>j</sub> (假设 P(Y=y<sub>j</sub>) > 0) 的条件下，X 的条件分布律为：
    \[ P(X=x_i | Y=y_j) = \frac{P(X=x_i, Y=y_j)}{P(Y=y_j)} = \frac{p_{ij}}{p_{\cdot j}} \]
    类似地，可以定义 P(Y=y<sub>j</sub> | X=x<sub>i</sub>)。

*   **连续型条件分布**：
    在 Y=y (假设 f<sub>Y</sub>(y) > 0) 的条件下，X 的条件概率密度函数为：
    \[ f_{X|Y}(x|y) = \frac{f(x,y)}{f_Y(y)} \]
    类似地，f<sub>Y|X</sub>(y|x) = f(x,y) / f<sub>X</sub>(x) (假设 f<sub>X</sub>(x) > 0)。
    注意：条件 PDF 仍然是一个关于 x (或 y) 的 PDF，对 x (或 y) 积分等于1。

## 6.6 随机变量的独立性 (Independence of Random Variables)

如果二维随机变量 (X, Y) 的联合分布等于其边缘分布的乘积，则称随机变量 X 和 Y 相互独立。

*   **对于任意 x, y**：
    \[ F(x, y) = F_X(x) F_Y(y) \]
*   **对于离散型随机变量** (等价条件)：
    对于所有可能的 x<sub>i</sub>, y<sub>j</sub>，
    \[ P(X=x_i, Y=y_j) = P(X=x_i) P(Y=y_j) \]
    即 p<sub>ij</sub> = p<sub>i·</sub> p<sub>·j</sub>
*   **对于连续型随机变量** (等价条件，几乎处处成立)：
    \[ f(x, y) = f_X(x) f_Y(y) \]

独立性的重要推论：若 X, Y 相互独立，则 E(XY) = E(X)E(Y)，Cov(X,Y) = 0，ρ<sub>XY</sub> = 0。
（但反之不一定成立，除非是二维正态分布）。
若 X, Y 相互独立，则 g(X) 和 h(Y) 也相互独立，其中 g, h 为任意函数。

## 6.7 二维随机变量的函数的分布 (Distribution of Functions of Two Random Variables)

已知 (X, Y) 的联合分布，求其函数 Z = g(X, Y) 的分布。例如 Z = X+Y, Z = XY, Z = max(X,Y) 等。
这通常比一维情况复杂，一般方法是先求 Z 的 CDF：
F<sub>Z</sub>(z) = P(Z ≤ z) = P(g(X,Y) ≤ z) = ∬<sub>g(x,y)≤z</sub> f(x,y) dxdy
然后通过求导得到 Z 的 PDF (如果 Z 是连续的)。
对于特定函数如和、商、积、最大/最小值，有时有特定的公式或技巧。 