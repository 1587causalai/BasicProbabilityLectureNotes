# 高维柯西分布与正态分布之比的性质

本文档旨在梳理高维柯西分布和两个独立正态分布随机变量之比的数学性质与推导过程。

## 一、高维柯西分布 (High-dimensional Cauchy Distribution)

高维柯西分布是多元 t 分布的一个重要特例。要理解高维柯西分布，我们首先需要了解多元 t 分布。

### 1. 背景：多元 t 分布 (Multivariate t-distribution)

**定义与构造背景：**
多元 t 分布是一元 t 分布向多维空间的自然推广。它通常由一个服从多元正态分布的随机向量，除以一个独立的、经自由度调整的卡方分布随机变量的平方根来定义。这种构造使其具有比多元正态分布更“重”的尾部，从而在处理含有异常值的数据时更为稳健。

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
$t = \frac{\bar{X} - \mu_0}{S/\sqrt{n}}$
其中：
*   $\bar{X}$ 是样本均值 (来自正态分布的数据)。
*   $\mu_0$ 是假设的总体均值。
*   $S$ 是样本标准差 (用于估计未知的总体标准差 $\sigma$)。
*   $n$ 是样本量。

这里的关键是，当我们用样本标准差 $S$ 来代替未知的总体标准差 $\sigma$ 时，这个统计量就不再服从标准正态分布，而是服从t分布。分母中的 $S$ 就扮演了类似上面多元情况中 $\sqrt{U/\nu}$ 的角色，引入了因估计方差而产生的不确定性。

**总结来说：**

多元t分布的统计量可以看作是**一个标准化的多元正态随机向量，但其标准化过程用到的“方差”或“尺度”本身也是一个随机量（由卡方分布派生而来）**。这使得多元t分布比多元正态分布具有更“重”的尾部，能更好地描述那些包含异常值或者方差不完全确定的数据。

文档 `appendix_a_cauchy_distribution.md` 中给出的数学定义：
$$ \mathbf{T} = \mathbf{\mu} + \frac{\mathbf{Z}}{\sqrt{U/\nu}} $$
其中 $\mathbf{Z} \sim N_p(\mathbf{0}, \mathbf{\Sigma})$ 且 $U \sim \chi^2(\nu)$ 且 $\mathbf{Z}$ 与 $U$ 独立，这个 $\mathbf{T}$ 就服从 $t_p(\mathbf{\mu}, \mathbf{\Sigma}, \nu)$。

