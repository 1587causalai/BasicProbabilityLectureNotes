# 高维柯西分布与正态分布之比的性质

本文档旨在梳理高维柯西分布和两个独立正态分布随机变量之比的数学性质与推导过程。

## 一、高维柯西分布 (High-dimensional Cauchy Distribution)

高维柯西分布是多元 t 分布的一个重要特例。要理解高维柯西分布，我们首先需要了解多元 t 分布。

### 1. 背景：多元 t 分布 (Multivariate t-distribution)

**定义与构造背景：**
多元 t 分布是一元 t 分布向多维空间的自然推广。它通常由一个服从多元正态分布的随机向量，除以一个独立的、经自由度调整的卡方分布随机变量的平方根来定义。这种构造使其具有比多元正态分布更"重"的尾部，从而在处理含有异常值的数据时更为稳健。

**数学定义：**
假设有一个 $p$ 维随机向量 $\mathbf{Z}$ 服从均值为 $\mathbf{0}$、协方差矩阵为 $\mathbf{\Sigma}$ (一个 $p \times p$ 的正定矩阵) 的多元正态分布，记为 $\mathbf{Z} \sim N_p(\mathbf{0}, \mathbf{\Sigma})$。
同时，有一个独立的随机变量 $U$ 服从自由度为 $\nu > 0$ 的卡方分布，记为 $U \sim \chi^2(\nu)$。

则 $p$ 维随机向量 $\mathbf{T}$ 定义为：
$$
\mathbf{T} = \frac{\mathbf{Z}}{\sqrt{U/\nu}}
$$
这个随机向量 $\mathbf{T}$ 就服从自由度为 $\nu$、位置参数为 $\mathbf{0}$、尺度矩阵为 $\mathbf{\Sigma}$ 的多元 t 分布。如果引入位置参数 $\mathbf{\mu}$，则 $\mathbf{T} = \mathbf{\mu} + \frac{\mathbf{Z}}{\sqrt{U/\nu}}$ 服从 $t_p(\mathbf{\mu}, \mathbf{\Sigma}, \nu)$。

**密度函数 (PDF) 推导：**
我们推导位置参数为 $\mathbf{\mu}$ 的情况。令 $\mathbf{X} = \mathbf{T} - \mathbf{\mu} = \frac{\mathbf{Z}}{\sqrt{U/\nu}}$。
给定 $U=u$，则 $\mathbf{X} | (U=u) \sim N_p(\mathbf{0}, \frac{\nu}{u}\mathbf{\Sigma})$。
其条件密度函数为：
$$
f_{\mathbf{X}|U}(\mathbf{x}|u) = \frac{1}{(2\pi)^{p/2} |\frac{\nu}{u}\mathbf{\Sigma}|^{1/2}} \exp\left(-\frac{1}{2} \mathbf{x}' \left(\frac{\nu}{u}\mathbf{\Sigma}\right)^{-1} \mathbf{x}\right)
$$
$$
= \frac{1}{(2\pi)^{p/2} (\frac{\nu}{u})^{p/2} |\mathbf{\Sigma}|^{1/2}} \exp\left(-\frac{u}{2\nu} \mathbf{x}' \mathbf{\Sigma}^{-1} \mathbf{x}\right)
$$
随机变量 $U \sim \chi^2(\nu)$ 的密度函数为：
$$
f_U(u) = \frac{1}{2^{\nu/2} \Gamma(\nu/2)} u^{\nu/2 - 1} e^{-u/2}, \quad u > 0
$$
$\mathbf{X}$ 的边际密度函数 $f_{\mathbf{X}}(\mathbf{x})$ 通过对 $u$ 积分得到：
$$
f_{\mathbf{X}}(\mathbf{x}) = \int_0^\infty f_{\mathbf{X}|U}(\mathbf{x}|u) f_U(u) du
$$
$$
= \int_0^\infty \frac{1}{(2\pi)^{p/2} (\frac{\nu}{u})^{p/2} |\mathbf{\Sigma}|^{1/2}} \exp\left(-\frac{u}{2\nu} \mathbf{x}' \mathbf{\Sigma}^{-1} \mathbf{x}\right) \frac{1}{2^{\nu/2} \Gamma(\nu/2)} u^{\nu/2 - 1} e^{-u/2} du
$$
整理常数项和 $u$ 的幂次：
$$
f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{(2\pi)^{p/2} \nu^{p/2} |\mathbf{\Sigma}|^{1/2} 2^{\nu/2} \Gamma(\nu/2)} \int_0^\infty u^{p/2 + \nu/2 - 1} \exp\left(-\frac{u}{2} \left(1 + \frac{1}{\nu}\mathbf{x}' \mathbf{\Sigma}^{-1} \mathbf{x}\right)\right) du
$$
令 $A = \frac{p+\nu}{2}$ 和 $B = \frac{1}{2} \left(1 + \frac{1}{\nu}\mathbf{x}' \mathbf{\Sigma}^{-1} \mathbf{x}\right)$。
积分部分为 $\int_0^\infty u^{A-1} e^{-Bu} du$。
这是一个 Gamma 函数的形式。我们知道 $\int_0^\infty y^{k-1} e^{-y} dy = \Gamma(k)$。
通过换元 $y = Bu$，则 $u = y/B$, $du = dy/B$。
$$
\int_0^\infty \left(\frac{y}{B}\right)^{A-1} e^{-y} \frac{1}{B} dy = \frac{1}{B^A} \int_0^\infty y^{A-1} e^{-y} dy = \frac{\Gamma(A)}{B^A}
$$
代回 $A$ 和 $B$：
$$
\frac{\Gamma\left(\frac{p+\nu}{2}\right)}{\left[\frac{1}{2} \left(1 + \frac{1}{\nu}\mathbf{x}' \mathbf{\Sigma}^{-1} \mathbf{x}\right)\right]^{\frac{p+\nu}{2}}} = \frac{\Gamma\left(\frac{p+\nu}{2}\right) 2^{\frac{p+\nu}{2}}}{\left(1 + \frac{1}{\nu}\mathbf{x}' \mathbf{\Sigma}^{-1} \mathbf{x}\right)^{\frac{p+\nu}{2}}}
$$
代入 $f_{\mathbf{X}}(\mathbf{x})$ 的表达式：
$$
f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{(2\pi)^{p/2} \nu^{p/2} |\mathbf{\Sigma}|^{1/2} 2^{\nu/2} \Gamma(\nu/2)} \frac{\Gamma\left(\frac{p+\nu}{2}\right) 2^{\frac{p+\nu}{2}}}{\left(1 + \frac{1}{\nu}\mathbf{x}' \mathbf{\Sigma}^{-1} \mathbf{x}\right)^{\frac{p+\nu}{2}}}
$$
简化常数项中 $2$ 的幂次 ($2^{\frac{p+\nu}{2}} / (2^{p/2} 2^{\nu/2}) = 1$ ) 和 $\pi$ 的幂次：
$$
f_{\mathbf{X}}(\mathbf{x}) = \frac{\Gamma\left(\frac{\nu+p}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right) (\nu\pi)^{p/2} |\mathbf{\Sigma}|^{1/2}} \left(1 + \frac{1}{\nu}\mathbf{x}' \mathbf{\Sigma}^{-1} \mathbf{x}\right)^{-\frac{\nu+p}{2}}
$$
由于 $\mathbf{X} = \mathbf{T} - \mathbf{\mu}$, 所以 $\mathbf{T}$ 的密度函数 $f_{\mathbf{T}}(\mathbf{t})$ 为：
$$
f_{\mathbf{T}}(\mathbf{t}; \mathbf{\mu}, \mathbf{\Sigma}, \nu) = \frac{\Gamma\left(\frac{\nu+p}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right) (\nu\pi)^{p/2} |\mathbf{\Sigma}|^{1/2}} \left[1 + \frac{1}{\nu}(\mathbf{t}-\mathbf{\mu})' \mathbf{\Sigma}^{-1} (\mathbf{t}-\mathbf{\mu})\right]^{-\frac{\nu+p}{2}}
$$
这就是多元 t 分布的密度函数。

### 2. 高维柯西分布 (High-dimensional Cauchy Distribution)

**与多元 t 分布的联系：**
高维（或多元）柯西分布是多元 t 分布在自由度 $\nu=1$ 时的特例。

**密度函数推导：**
我们将 $\nu=1$ 代入上述多元 t 分布的 PDF 中：
$$
f_{\text{Cauchy}}(\mathbf{t}; \mathbf{\mu}, \mathbf{\Sigma}) = f_{\mathbf{T}}(\mathbf{t}; \mathbf{\mu}, \mathbf{\Sigma}, \nu=1)
$$
$$
= \frac{\Gamma\left(\frac{1+p}{2}\right)}{\Gamma\left(\frac{1}{2}\right) (1 \cdot \pi)^{p/2} |\mathbf{\Sigma}|^{1/2}} \left[1 + (\mathbf{t}-\mathbf{\mu})' \mathbf{\Sigma}^{-1} (\mathbf{t}-\mathbf{\mu})\right]^{-\frac{1+p}{2}}
$$
已知 Gamma 函数的特殊值 $\Gamma(1/2) = \sqrt{\pi}$。
所以，分母中的 $\Gamma(1/2) \pi^{p/2} = \sqrt{\pi} \cdot \pi^{p/2} = \pi^{1/2} \pi^{p/2} = \pi^{(p+1)/2}$。

因此，高维柯西分布的密度函数为：
$$
f_{\text{Cauchy}}(\mathbf{t}; \mathbf{\mu}, \mathbf{\Sigma}) = \frac{\Gamma\left(\frac{p+1}{2}\right)}{\pi^{(p+1)/2} |\mathbf{\Sigma}|^{1/2}} \left[1 + (\mathbf{t}-\mathbf{\mu})' \mathbf{\Sigma}^{-1} (\mathbf{t}-\mathbf{\mu})\right]^{-\frac{p+1}{2}}
$$
其中：
*   $\mathbf{\mu}$ 是 $p$ 维位置参数向量。
*   $\mathbf{\Sigma}$ 是 $p \times p$ 尺度矩阵 (必须是正定对称矩阵)。它类似于协方差矩阵的角色，但柯西分布本身没有定义好的均值和协方差。
*   $p$ 是数据的维度。

**标准高维柯西分布：**
如果位置参数 $\mathbf{\mu} = \mathbf{0}$ (零向量) 且尺度矩阵 $\mathbf{\Sigma} = \mathbf{I}$ (单位矩阵)，则得到标准高维柯西分布：
$$
f_{\text{Cauchy}}(\mathbf{t}; \mathbf{0}, \mathbf{I}) = \frac{\Gamma\left(\frac{p+1}{2}\right)}{\pi^{(p+1)/2}} \left[1 + \mathbf{t}'\mathbf{t}\right]^{-\frac{p+1}{2}}
$$
其中 $\mathbf{t}'\mathbf{t} = \sum_{i=1}^p t_i^2$ 是向量 $\mathbf{t}$ 的平方欧几里得范数。

### 3. 线性组合的性质 (Property of Linear Combinations)

高维柯西分布 $\mathbf{T} \sim \text{Cauchy}_p(\mathbf{\mu}, \mathbf{\Sigma})$ 拥有一个重要的"稳定性"质：其任意（非零）线性组合仍然是一个（一维）柯西分布。

假设 $\mathbf{a} = (a_1, a_2, \dots, a_p)'$ 是一个非零的 $p$ 维常数向量。我们关注标量随机变量 $Y = \mathbf{a}' \mathbf{T} = \sum_{i=1}^p a_i T_i$ 的分布。

结论是：
\[ Y = \mathbf{a}' \mathbf{T} \sim \text{Cauchy}(x_0, \gamma_{eff}) \]
其中：
*   **位置参数** (Location parameter) 为： $x_0 = \mathbf{a}' \mathbf{\mu}$
*   **有效尺度参数** (Effective scale parameter) 为： $\gamma_{eff} = \sqrt{\mathbf{a}' \mathbf{\Sigma} \mathbf{a}}$
    (注意：这里的 $\mathbf{\Sigma}$ 是高维柯西分布的尺度矩阵，$\mathbf{a}' \mathbf{\Sigma} \mathbf{a}$ 是一个正标量，其平方根 $\gamma_{eff}$ 定义了结果柯西分布的尺度。)

**推导简述 (基于构造法)：**
高维柯西分布 $\mathbf{T}$ 可以通过 $\mathbf{T} = \mathbf{\mu} + \frac{\mathbf{Z}}{\sqrt{U}}$ 构造得到，其中 $\mathbf{Z} \sim N_p(\mathbf{0}, \mathbf{\Sigma})$ 是一个多元正态随机向量，而 $U \sim \chi^2(1)$ 是一个独立的自由度为1的卡方随机变量 ($\sqrt{U}$ 服从半正态分布)。
考虑线性组合：
\[ \mathbf{a}' \mathbf{T} = \mathbf{a}' (\mathbf{\mu} + \frac{\mathbf{Z}}{\sqrt{U}}) = \mathbf{a}' \mathbf{\mu} + \frac{\mathbf{a}' \mathbf{Z}}{\sqrt{U}} \]
我们知道，多元正态分布的线性组合仍然是正态分布：$\mathbf{a}' \mathbf{Z} \sim N(0, \mathbf{a}' \mathbf{\Sigma} \mathbf{a})$。
令 $\gamma_{eff}^2 = \mathbf{a}' \mathbf{\Sigma} \mathbf{a}$ (这是一个正标量，代表了投影方向上的尺度平方)。则 $\gamma_{eff} = \sqrt{\mathbf{a}' \mathbf{\Sigma} \mathbf{a}}$。
我们可以将 $\mathbf{a}' \mathbf{Z}$ 写成 $\gamma_{eff} W$，其中 $W = \frac{\mathbf{a}' \mathbf{Z}}{\gamma_{eff}} \sim N(0, 1)$ 是一个标准正态随机变量。
代入上式：
\[ \mathbf{a}' \mathbf{T} = \mathbf{a}' \mathbf{\mu} + \frac{\gamma_{eff} W}{\sqrt{U}} = \mathbf{a}' \mathbf{\mu} + \gamma_{eff} \left( \frac{W}{\sqrt{U/1}} \right) \]
关键在于识别括号中的项：$\frac{W}{\sqrt{U/1}}$。由于 $W \sim N(0, 1)$ 且 $U \sim \chi^2(1)$ 独立，这个比率正好是标准柯西分布 $\text{Cauchy}(0, 1)$ 的构造方式之一（标准正态除以独立的自由度为1的卡方变量的平方根）。
令 $C = \frac{W}{\sqrt{U/1}} \sim \text{Cauchy}(0, 1)$。
那么 $\mathbf{a}' \mathbf{T} = \mathbf{a}' \mathbf{\mu} + \gamma_{eff} C$。
根据一维柯西分布的线性变换性质：如果 $C \sim \text{Cauchy}(x_c, \gamma_c)$，则 $b + aC \sim \text{Cauchy}(b + ax_c, |a|\gamma_c)$。
在此处，$x_c=0$, $\gamma_c=1$, $b = \mathbf{a}' \mathbf{\mu}$, $a = \gamma_{eff}$。
因此：
\[ \mathbf{a}' \mathbf{T} \sim \text{Cauchy}(\mathbf{a}' \mathbf{\mu} + \gamma_{eff} \cdot 0, |\gamma_{eff}| \cdot 1) = \text{Cauchy}(\mathbf{a}' \mathbf{\mu}, \gamma_{eff}) \]
代回 $\gamma_{eff} = \sqrt{\mathbf{a}' \mathbf{\Sigma} \mathbf{a}}$，即得到最终结果。

这个性质表明高维柯西分布对于线性变换是"封闭"的，其投影到任意方向上仍然保持柯西分布的形式，只是位置和尺度参数会相应调整。

### 4. 特例：对角尺度矩阵 (Special Case: Diagonal Scale Matrix)

为了更深入地理解高维柯西分布的结构，我们考虑一个重要的特例：假设 $p$ 维随机向量 $\mathbf{T}$ 服从高维柯西分布 $\text{Cauchy}_p(\mathbf{\mu}, \mathbf{\Sigma})$，且其尺度矩阵 $\mathbf{\Sigma}$ 是一个对角矩阵。

设 $\mathbf{\mu} = (\mu_1, \mu_2, \dots, \mu_p)'$ 为位置参数向量。尺度矩阵 $\mathbf{\Sigma}$ 具有以下形式：
\[ \mathbf{\Sigma} = \text{diag}(\gamma_1^2, \gamma_2^2, \dots, \gamma_p^2) = \begin{pmatrix} \gamma_1^2 & 0 & \dots & 0 \\ 0 & \gamma_2^2 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \gamma_p^2 \end{pmatrix} \]
这里，$\gamma_i > 0$ 是与第 $i$ 个分量 $T_i$ 相关联的**尺度参数**，这与一维柯西分布 $\text{Cauchy}(\mu_i, \gamma_i)$ 中的尺度参数 $\gamma_i$ 相对应。

**边际分布与分量依赖性：**
在此设定下，每个分量 $T_i$ 的边际分布确实是一个一维柯西分布，即 $T_i \sim \text{Cauchy}(\mu_i, \gamma_i)$。
然而，需要特别注意的是，即使尺度矩阵 $\mathbf{\Sigma}$ 是对角的，向量 $\mathbf{T}$ 的各个分量 $T_1, \dots, T_p$ **通常也不是相互统计独立的**。这源于高维柯西分布的一种构造方式：它可以看作是一个多元正态向量 $\mathbf{Z} \sim N_p(\mathbf{0}, \mathbf{\Sigma})$ 除以一个独立的 $\sqrt{U}$，其中 $U \sim \chi^2(1)$。当 $\mathbf{\Sigma}$ 是对角时，$\mathbf{Z}$ 的分量 $Z_i \sim N(0, \gamma_i^2)$ 是独立的。但是，由于所有 $T_i = \mu_i + Z_i/\sqrt{U}$ 都依赖于**同一个**随机变量 $U$，这就在 $T_i$ 之间引入了相关性。因此，高维柯西分布的联合密度函数**不能**简单地写成各边际柯西分布密度函数的乘积。

**概率密度函数 (PDF)：**
当 $\mathbf{\Sigma}$ 是对角矩阵 $\text{diag}(\gamma_1^2, \dots, \gamma_p^2)$ 时，其逆矩阵为 $\mathbf{\Sigma}^{-1} = \text{diag}(1/\gamma_1^2, \dots, 1/\gamma_p^2)$，其行列式的平方根为 $|\mathbf{\Sigma}|^{1/2} = \prod_{j=1}^p \gamma_j$。
此时，高维柯西分布的概率密度函数 (PDF) 具体化为：
\[ f_{\text{Cauchy}}(\mathbf{t}; \mathbf{\mu}, \mathbf{\Sigma}) = \frac{\Gamma\left(\frac{p+1}{2}\right)}{\pi^{(p+1)/2} \left(\prod_{j=1}^p \gamma_j\right)} \left[1 + \sum_{i=1}^p \left(\frac{t_i-\mu_i}{\gamma_i}\right)^2\right]^{-\frac{p+1}{2}} \]

**线性组合性质的验证：**
我们来验证之前提到的线性组合性质。考虑线性组合 $Y = \mathbf{a}' \mathbf{T} = \sum_{i=1}^p a_i T_i$。根据一般性质， $Y$ 应服从 $\text{Cauchy}(x_0, \gamma_{eff})$，其中 $x_0 = \mathbf{a}' \mathbf{\mu}$ 且 $\gamma_{eff} = \sqrt{\mathbf{a}' \mathbf{\Sigma} \mathbf{a}}$。
在此特例中：
*   位置参数为：$x_0 = \sum_{i=1}^p a_i \mu_i$
*   有效尺度参数 $\gamma_{eff}$ 的平方为：
    \[ \gamma_{eff}^2 = \mathbf{a}' \mathbf{\Sigma} \mathbf{a} = (a_1, \dots, a_p) \begin{pmatrix} \gamma_1^2 & & \\ & \ddots & \\ & & \gamma_p^2 \end{pmatrix} \begin{pmatrix} a_1 \\ \vdots \\ a_p \end{pmatrix} = \sum_{i=1}^p a_i^2 \gamma_i^2 \]
*   因此，有效尺度参数为：$\gamma_{eff} = \sqrt{\sum_{i=1}^p a_i^2 \gamma_i^2}$

结论是，对于具有对角尺度矩阵的高维柯西分布，其线性组合 $Y = \mathbf{a}'\mathbf{T}$ 服从：
\[ Y \sim \text{Cauchy}\left(\sum_{i=1}^p a_i \mu_i, \sqrt{\sum_{i=1}^p a_i^2 \gamma_i^2}\right) \]
这与一般公式的结果一致，并清楚地展示了当尺度矩阵为对角时，新柯西分布的参数是如何由原始参数和线性系数决定的。

## 二、两个独立正态分布随机变量之比

我们来探讨两个独立正态分布随机变量的商如何形成柯西分布。

### 1. 情况一：两个独立的标准正态分布之比

假设 $X \sim N(0, 1)$ 和 $Y \sim N(0, 1)$，且 $X$ 和 $Y$ 相互独立。
我们想求随机变量 $Z = X/Y$ 的分布。

**推导 (使用变量替换法)：**
令 $Z = X/Y$。我们引入一个辅助变量，例如 $W = Y$。
则反函数为 $X = ZW$ 和 $Y = W$。
计算雅可比行列式 $J$ 的绝对值：
$$
J = \begin{vmatrix} \frac{\partial x}{\partial z} & \frac{\partial x}{\partial w} \\ \frac{\partial y}{\partial z} & \frac{\partial y}{\partial w} \end{vmatrix} = \begin{vmatrix} w & z \\ 0 & 1 \end{vmatrix} = w \cdot 1 - z \cdot 0 = w
$$
所以 $|J| = |w|$。

$X$ 和 $Y$ 的联合密度函数 $f_{X,Y}(x,y)$ 由于独立性为：
$$
f_{X,Y}(x,y) = f_X(x) f_Y(y) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2} \cdot \frac{1}{\sqrt{2\pi}} e^{-y^2/2} = \frac{1}{2\pi} e^{-(x^2+y^2)/2}
$$
$Z$ 和 $W$ 的联合密度函数 $f_{Z,W}(z,w)$ 为：
$$
f_{Z,W}(z,w) = f_{X,Y}(zw, w) |J|
$$
$$
= \frac{1}{2\pi} e^{-((zw)^2+w^2)/2} |w| = \frac{1}{2\pi} |w| e^{-w^2(z^2+1)/2}
$$
为了得到 $Z$ 的边际密度函数 $f_Z(z)$，我们需要对 $w$ 进行积分：
$$
f_Z(z) = \int_{-\infty}^{\infty} f_{Z,W}(z,w) dw = \int_{-\infty}^{\infty} \frac{1}{2\pi} |w| e^{-w^2(z^2+1)/2} dw
$$
由于被积函数关于 $w$ 是偶函数 ($|w|$ 和 $w^2$ 都是偶函数)，我们可以简化积分：
$$
f_Z(z) = 2 \int_{0}^{\infty} \frac{1}{2\pi} w e^{-w^2(z^2+1)/2} dw = \frac{1}{\pi} \int_{0}^{\infty} w e^{-w^2(z^2+1)/2} dw
$$
进行变量替换，令 $u = \frac{w^2(z^2+1)}{2}$。
那么 $du = w(z^2+1) dw$，所以 $w dw = \frac{du}{z^2+1}$。
积分限：当 $w=0$, $u=0$；当 $w \to \infty$, $u \to \infty$。
积分变为：
$$
\int_{0}^{\infty} e^{-u} \frac{1}{z^2+1} du = \frac{1}{z^2+1} \int_{0}^{\infty} e^{-u} du
$$
$$
= \frac{1}{z^2+1} [-e^{-u}]_{0}^{\infty} = \frac{1}{z^2+1} (0 - (-1)) = \frac{1}{z^2+1}
$$
代回 $f_Z(z)$：
$$
f_Z(z) = \frac{1}{\pi} \frac{1}{1+z^2}
$$
这就是标准柯西分布 Cauchy(0,1) 的密度函数。其位置参数 $x_0=0$，尺度参数 $\gamma=1$。
(标准柯西PDF: $f(z; x_0, \gamma) = \frac{1}{\pi\gamma} \frac{1}{1 + ((z-x_0)/\gamma)^2}$)

### 2. 情况二：两个独立的零均值正态分布之比 (不同方差)

假设 $X \sim N(0, \sigma_X^2)$ 和 $Y \sim N(0, \sigma_Y^2)$，且 $X$ 和 $Y$ 独立。
令 $Z = X/Y$。

我们可以通过标准化变量来利用情况一的结果：
令 $X' = X/\sigma_X \sim N(0,1)$ 和 $Y' = Y/\sigma_Y \sim N(0,1)$。
从情况一我们知道 $C = X'/Y' \sim \text{Cauchy}(0,1)$。

现在看 $Z$：
$$
Z = \frac{X}{Y} = \frac{\sigma_X X'}{\sigma_Y Y'} = \frac{\sigma_X}{\sigma_Y} \cdot \frac{X'}{Y'} = \frac{\sigma_X}{\sigma_Y} C
$$
如果一个随机变量 $C \sim \text{Cauchy}(x_0, \gamma)$，那么 $aC+b \sim \text{Cauchy}(ax_0+b, |a|\gamma)$。
在这里，$x_0=0$, $\gamma=1$, $a = \sigma_X/\sigma_Y$, $b=0$。
所以，$Z$ 服从柯西分布：
$$
Z \sim \text{Cauchy}\left(\left(\frac{\sigma_X}{\sigma_Y}\right) \cdot 0 + 0, \left|\frac{\sigma_X}{\sigma_Y}\right| \cdot 1\right)
$$
$$
Z \sim \text{Cauchy}\left(0, \frac{\sigma_X}{\sigma_Y}\right)
$$
因此，**位置参数为 $0$，尺度参数为 $\sigma_X/\sigma_Y$**。

其密度函数为：
$$
f_Z(z) = \frac{1}{\pi \left(\frac{\sigma_X}{\sigma_Y}\right)} \frac{1}{1 + \left(\frac{z - 0}{\sigma_X/\sigma_Y}\right)^2} = \frac{\sigma_Y}{\pi \sigma_X} \frac{1}{1 + \frac{z^2 \sigma_Y^2}{\sigma_X^2}}
$$
$$
= \frac{\sigma_Y}{\pi \sigma_X} \frac{\sigma_X^2}{\sigma_X^2 + z^2 \sigma_Y^2} = \frac{\sigma_X \sigma_Y}{\pi (\sigma_X^2 + z^2 \sigma_Y^2)}
$$

### 3. 更一般情况的引申

如果 $X \sim N(\mu_X, \sigma_X^2)$ 和 $Y \sim N(\mu_Y, \sigma_Y^2)$ 独立，那么：
考虑 $X^* = X - \mu_X \sim N(0, \sigma_X^2)$ 和 $Y^* = Y - \mu_Y \sim N(0, \sigma_Y^2)$。
根据情况二，随机变量：
$$
W = \frac{X^*}{Y^*} = \frac{X - \mu_X}{Y - \mu_Y}
$$
将服从柯西分布：
$$
W \sim \text{Cauchy}\left(0, \frac{\sigma_X}{\sigma_Y}\right)
$$
这里的**位置参数是 $0$，尺度参数是 $\sigma_X/\sigma_Y$**。

注意：直接的商 $X/Y$ 当 $\mu_Y \neq 0$ 时，其分布通常不是标准的柯西分布，而是更复杂的比率分布 (Ratio Distribution)。



## 三、柯西分布参数的稳健估计 (Robust Estimation of Cauchy Parameters)

由于柯西分布的均值、方差以及更高阶的矩均未定义，传统的基于样本矩（如样本均值和样本方差）的参数估计方法不适用于柯西分布。实际上，对于柯西分布的样本，样本均值的分布与单个观测值的分布相同，这意味着增大样本量并不会提高样本均值作为位置参数估计的精度。因此，我们需要依赖于稳健统计方法，特别是基于排序统计量 (order statistics) 或分位数 (quantiles) 的方法。

假设我们有一组来自柯西分布 $X_1, X_2, \dots, X_n \sim \text{Cauchy}(x_0, \gamma)$ 的独立同分布样本。我们的目标是估计位置参数 $x_0$ 和尺度参数 $\gamma$。

### 1. 位置参数 $x_0$ 的估计

对于柯西分布，**样本中位数 (sample median)** 是其位置参数 $x_0$ 的一个简单且稳健的估计量。
记排序后的样本为 $X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$。
样本中位数 $\hat{x}_0$ 定义为：
*   如果 $n$ 是奇数, $\hat{x}_0 = X_{((n+1)/2)}$
*   如果 $n$ 是偶数, $\hat{x}_0$ 通常取 $X_{(n/2)}$ 和 $X_{(n/2+1)}$ 的平均值，或者其中任意一个。

样本中位数对于柯西分布的极端值（即其“重尾”特性）不敏感，因此能够提供比样本均值稳定得多的估计。

### 2. 尺度参数 $\gamma$ 的估计

尺度参数 $\gamma$ 可以通过样本分位数来估计。
对于标准柯西分布 $\text{Cauchy}(0, 1)$，其累积分布函数 (CDF) 为 $F(x; 0, 1) = \frac{1}{\pi} \arctan(x) + \frac{1}{2}$。
*   第一四分位数 (First Quartile, $Q_1$) 对应于 $F(Q_1) = 0.25$。解 $\frac{1}{\pi} \arctan(Q_1) + \frac{1}{2} = 0.25$ 得到 $\arctan(Q_1) = -\frac{\pi}{4}$，所以 $Q_1 = -1$。
*   第三四分位数 (Third Quartile, $Q_3$) 对应于 $F(Q_3) = 0.75$。解 $\frac{1}{\pi} \arctan(Q_3) + \frac{1}{2} = 0.75$ 得到 $\arctan(Q_3) = \frac{\pi}{4}$，所以 $Q_3 = 1$。

对于一般的柯西分布 $\text{Cauchy}(x_0, \gamma)$，其分位数与标准柯西分布的分位数有如下关系：
如果 $C \sim \text{Cauchy}(0,1)$，那么 $X = x_0 + \gamma C \sim \text{Cauchy}(x_0, \gamma)$。
因此，柯西分布 $\text{Cauchy}(x_0, \gamma)$ 的：
*   第一四分位数 $Q_1(X) = x_0 + \gamma Q_1(C) = x_0 - \gamma$
*   第三四分位数 $Q_3(X) = x_0 + \gamma Q_3(C) = x_0 + \gamma$

从这两个等式，我们可以得到四分位距 (Interquartile Range, IQR)：
$$ \text{IQR} = Q_3(X) - Q_1(X) = (x_0 + \gamma) - (x_0 - \gamma) = 2\gamma $$
因此，尺度参数 $\gamma$ 可以表示为：
$$ \gamma = \frac{\text{IQR}}{2} $$
这个量有时也被称为半四分位距 (Half Interquartile Range 或 Semi-Interquartile Range, HIQR 或 SIQR)。

基于此，我们可以使用样本的四分位数来估计 $\gamma$：
令 $\hat{Q}_1$ 和 $\hat{Q}_3$ 分别为样本的第一和第三四分位数。
则尺度参数 $\gamma$ 的一个稳健估计量为：
$$ \hat{\gamma} = \frac{\hat{Q}_3 - \hat{Q}_1}{2} $$

**计算样本四分位数 $\hat{Q}_1$ 和 $\hat{Q}_3$：**
有多种计算样本分位数的方法。一种常见方法是：
1.  对样本 $X_1, \dots, X_n$ 进行排序得到 $X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$。
2.  $\hat{Q}_1$ 是位于排序后数据 $1/4$ 位置的值。
3.  $\hat{Q}_3$ 是位于排序后数据 $3/4$ 位置的值。
具体计算可能涉及线性插值，取决于所使用的分位数定义。

例如，一种简单的方法是取 $p(n+1)$ 位置的秩（如果不是整数则进行插值）。对于 $Q_1$，取 $0.25(n+1)$ 位置的值；对于 $Q_3$，取 $0.75(n+1)$ 位置的值。

**优点：**
这种基于分位数的估计方法对于柯西分布的长尾特性具有很强的稳健性，因为它们只依赖于数据的中心部分，而忽略了极端值的影响。

### 3. 其他稳健估计方法

除了基于中位数和四分位距的方法外，还有其他更复杂的稳健估计技术，例如：
*   **最大似然估计 (Maximum Likelihood Estimation, MLE)：** 对于柯西分布，似然函数可以被写出，并且可以通过数值优化方法求解得到 $x_0$ 和 $\gamma$ 的MLE估计。MLE估计量通常具有良好的渐近性质（如一致性和渐近正态性），但可能需要迭代计算。
*   **基于其他分位数的估计：** 例如，可以使用对称的 $p$-分位数和 $(1-p)$-分位数来估计 $\gamma$。
*   **M-估计量 (M-estimators)：** 更广义的一类稳健估计量。

然而，对于柯西分布的参数估计，基于中位数和四分位距的方法因其简单性和直观性而广受欢迎，并且通常能提供足够好的初始估计或最终估计。


## QA


### 1. 希望更好地理解多元t分布！



简单来说，一个统计量会服从多元t分布，通常是在我们处理**多元正态分布的数据，但是其真实的协方差矩阵未知，需要从数据中估计**时出现的。

你可以这样理解它的构造过程：

1.  **基础是多元正态分布**：
    想象你有一个 $p$ 维的随机向量 $\mathbf{Z}$，它服从均值为 $\mathbf{0}$、协方差矩阵为 $\mathbf{\Sigma}$ 的多元正态分布。这代表了你的数据在理想情况下（即协方差已知）的分布形态。

2.  **引入不确定性 (卡方分布)**：
    现在，假设协方差矩阵 $\mathbf{\Sigma}$ 不是完全已知的，或者说，我们用一个随机的缩放因子来调整它。这个缩放因子来源于一个独立的、服从卡方分布 (Chi-squared distribution) 的随机变量 $U$，自由度为 $\nu$。卡方分布常常和方差的估计联系在一起。

3.  **构造统计量**：
    我们将前面那个多元正态分布的随机向量 $\mathbf{Z}$，**除以** $\sqrt{U/\nu}$ (也就是卡方变量 $U$ 除以其自由度 $\nu$ 后再开根号)。
    得到的新的 $p$ 维随机向量 $\mathbf{T} = \frac{\mathbf{Z}}{\sqrt{U/\nu}}$ 就服从多元t分布。

    如果原始的多元正态分布的均值不是 $\mathbf{0}$ 而是 $\mathbf{\mu}$，那么统计量 $\mathbf{T} = \mathbf{\mu} + \frac{\mathbf{Z}}{\sqrt{U/\nu}}$ 也会服从多元t分布 (只不过位置参数变成了 $\mathbf{\mu}$)。

**直观类比 (一元t分布)：**

这和我们熟悉的一元t分布的产生方式非常类似。回想一下，一元t统计量通常是这样构造的：
$$t = \frac{\bar{X} - \mu_0}{S/\sqrt{n}}$$
其中：
*   $\bar{X}$ 是样本均值 (来自正态分布的数据)。
*   $\mu_0$ 是假设的总体均值。
*   $S$ 是样本标准差 (用于估计未知的总体标准差 $\sigma$)。
*   $n$ 是样本量。

这里的关键是，当我们用样本标准差 $S$ 来代替未知的总体标准差 $\sigma$ 时，这个统计量就不再服从标准正态分布，而是服从t分布。分母中的 $S$ 就扮演了类似上面多元情况中 $\sqrt{U/\nu}$ 的角色，引入了因估计方差而产生的不确定性。

**总结来说：**

多元t分布的统计量可以看作是**一个标准化的多元正态随机向量，但其标准化过程用到的"方差"或"尺度"本身也是一个随机量（由卡方分布派生而来）**。这使得多元t分布比多元正态分布具有更"重"的尾部，能更好地描述那些包含异常值或者方差不完全确定的数据。

文档 `appendix_a_cauchy_distribution.md` 中给出的数学定义：
$$ \mathbf{T} = \mathbf{\mu} + \frac{\mathbf{Z}}{\sqrt{U/\nu}} $$
其中 $\mathbf{Z} \sim N_p(\mathbf{0}, \mathbf{\Sigma})$ 且 $U \sim \chi^2(\nu)$ 且 $\mathbf{Z}$ 与 $U$ 独立，这个 $\mathbf{T}$ 就服从 $t_p(\mathbf{\mu}, \mathbf{\Sigma}, \nu)$。



