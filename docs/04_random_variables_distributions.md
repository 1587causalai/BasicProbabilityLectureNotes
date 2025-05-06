# 4. 随机变量及其分布 (Random Variables and Their Distributions)

本章引入随机变量的概念，它是将随机试验的结果数量化的重要工具，并讨论其概率分布。

## 4.1 随机变量的概念 (Concept of Random Variable)

**随机变量 (Random Variable)** 是一个定义在样本空间 Ω 上的实值函数，通常用大写字母 X, Y, Z 等表示。即 X = X(ω)，其中 ω ∈ Ω。
随机变量使得我们可以用数字来描述随机试验的各种结果，从而方便地运用数学工具进行分析。

例如，抛两枚硬币，样本空间 Ω = {(正,正), (正,反), (反,正), (反,反)}。
可以定义随机变量 X 为"出现正面的次数"，则：
X(正,正) = 2
X(正,反) = 1
X(反,正) = 1
X(反,反) = 0

随机变量根据其取值情况分为离散型和连续型。

## 4.2 离散型随机变量 (Discrete Random Variables)

如果随机变量 X 的所有可能取值是有限个或可列无限多个，则称 X 为**离散型随机变量 (Discrete Random Variable)**。

### 4.2.1 概率质量函数 (Probability Mass Function, PMF)

描述离散型随机变量 X 的概率分布的是其**概率质量函数 (PMF)**，也称为分布律。它给出了 X 取各个可能值的概率：
\[ P(X=x_k) = p_k, \quad k=1, 2, ... \]
其中 p<sub>k</sub> ≥ 0，且 Σ<sub>k</sub> p<sub>k</sub> = 1。
可以用表格或公式的形式表示。

### 4.2.2 常见离散分布 (Common Discrete Distributions)

1.  **两点分布/伯努利分布 (Bernoulli Distribution)**：X ~ B(1, p) 或 Bernoulli(p)
    一次试验只有两个结果（成功/失败），P(X=1) = p (成功), P(X=0) = 1-p (失败)。
2.  **二项分布 (Binomial Distribution)**：X ~ B(n, p)
    n 重伯努利试验中成功次数的分布。
    \[ P(X=k) = C_n^k p^k (1-p)^{n-k}, \quad k=0, 1, ..., n \]
3.  **泊松分布 (Poisson Distribution)**：X ~ P(λ) 或 Poisson(λ)
    描述单位时间（或单位面积、单位长度等）内某事件发生次数的分布。
    \[ P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k=0, 1, 2, ... \]
    其中 λ > 0 是单位时间/空间内事件发生的平均次数。泊松分布是二项分布在 n 很大，p 很小时的极限形式 (当 np → λ)。
4.  **几何分布 (Geometric Distribution)**：
    在重复独立的伯努利试验中，首次成功发生时的试验次数 X 的分布。
    \[ P(X=k) = (1-p)^{k-1}p, \quad k=1, 2, ... \]
5.  **超几何分布 (Hypergeometric Distribution)**：
    从 N 件产品（其中 M 件次品，N-M 件正品）中不放回地抽取 n 件，其中次品数 X 的分布。
    \[ P(X=k) = \frac{C_M^k C_{N-M}^{n-k}}{C_N^n} \]
    其中 max(0, n-(N-M)) ≤ k ≤ min(n, M)。

## 4.3 连续型随机变量 (Continuous Random Variables)

如果随机变量 X 的所有可能取值充满一个区间（有限或无限），则称 X 为**连续型随机变量 (Continuous Random Variable)**。
对于连续型随机变量，我们关注的是 X 落在某个区间内的概率，而不是取某个特定值的概率（通常为0）。

### 4.3.1 概率密度函数 (Probability Density Function, PDF)

描述连续型随机变量 X 的概率分布的是其**概率密度函数 (Probability Density Function, PDF)**，记作 f(x)。f(x) 满足：
1.  f(x) ≥ 0
2.  ∫<sub>-∞</sub><sup>+∞</sup> f(x) dx = 1
3.  对于任意实数 a < b，
    \[ P(a < X \leq b) = \int_a^b f(x) dx \]
    PDF 本身不是概率，f(x)dx 才近似表示 X 落在 (x, x+dx) 这个微小区间内的概率。

### 4.3.2 累积分布函数 (Cumulative Distribution Function, CDF)

对于任意随机变量 X (离散或连续)，其**累积分布函数 (Cumulative Distribution Function, CDF)** 定义为：
\[ F(x) = P(X \leq x) \]
CDF 的性质：
1.  0 ≤ F(x) ≤ 1
2.  F(x) 是一个单调不减函数。
3.  F(-∞) = lim<sub>x→-∞</sub> F(x) = 0
4.  F(+∞) = lim<sub>x→+∞</sub> F(x) = 1
5.  F(x) 是右连续的，即 F(x+0) = F(x)。

对于离散型随机变量： F(x) = Σ<sub>x<sub>k</sub>≤x</sub> P(X=x<sub>k</sub>)
对于连续型随机变量： F(x) = ∫<sub>-∞</sub><sup>x</sup> f(t) dt，且在其连续点上有 f(x) = F'(x)。

### 4.3.3 常见连续分布 (Common Continuous Distributions)

1.  **均匀分布 (Uniform Distribution)**：X ~ U(a, b)
    在区间 [a, b] 上等可能取值。
    \[ f(x) = \begin{cases} \frac{1}{b-a}, & a \leq x \leq b \\ 0, & \text{otherwise} \end{cases} \]
2.  **指数分布 (Exponential Distribution)**：X ~ Exp(λ)
    描述独立事件首次发生所需等待时间的分布，或无记忆性的寿命分布。
    \[ f(x) = \begin{cases} \lambda e^{-\lambda x}, & x > 0 \\ 0, & x \leq 0 \end{cases} \]
    其中 λ > 0 是失效率。
3.  **正态分布/高斯分布 (Normal/Gaussian Distribution)**：X ~ N(μ, σ²)
    在自然界和实际应用中极为常见，由中心极限定理保证其重要性。
    \[ f(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \quad -\infty < x < +\infty \]
    其中 μ 是均值，σ² 是方差。标准正态分布 N(0, 1) 的 PDF 常用 φ(x) 表示，CDF 常用 Φ(x) 表示。

## 4.4 随机变量的函数的分布 (Distribution of Functions of Random Variables)

已知随机变量 X 的分布，求其函数 Y = g(X) 的分布是一个常见问题。
*   **离散情况**：若 X 是离散的，则 Y 也是离散的 (通常情况下)。可以通过列举 Y 的所有可能取值 y<sub>j</sub>，然后计算 P(Y=y<sub>j</sub>) = P(g(X)=y<sub>j</sub>) = Σ<sub>{k|g(x<sub>k</sub>)=y<sub>j</sub>}</sub> P(X=x<sub>k</sub>)。
*   **连续情况**：
    1.  **CDF 法**：先求 Y 的 CDF，F<sub>Y</sub>(y) = P(Y ≤ y) = P(g(X) ≤ y)。将 g(X) ≤ y 转化为 X 的不等式，然后利用 X 的 CDF 或 PDF 计算该概率。最后通过 F<sub>Y</sub>'(y) = f<sub>Y</sub>(y) 求得 Y 的 PDF。
    2.  **公式法 (若 g(x) 单调)**：若 y = g(x) 是严格单调函数，其反函数为 x = h(y)，且 h(y) 可导。则 Y 的 PDF 为：
        \[ f_Y(y) = f_X(h(y)) |h'(y)| \]
        需要确定 y 的取值范围。 