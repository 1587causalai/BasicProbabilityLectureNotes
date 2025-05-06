# 2. 概率的定义与性质 (Definitions and Properties of Probability)

本章将介绍概率的几种主要定义方法，并探讨其基本性质。

## 2.1 古典概型 (Classical Probability)

如果一个随机试验满足：
1.  样本空间 Ω 只包含有限个基本事件 (有限性)。
2.  每个基本事件发生的可能性都相同 (等可能性)。

则称此随机试验为古典概型。对于古典概型中的任一事件 A，其概率定义为：
\[ P(A) = \frac{\text{事件 A 包含的基本事件数}}{\text{样本空间 Ω 中基本事件的总数}} = \frac{k}{n} \]

*   例子：掷一颗均匀的骰子，求点数为偶数的概率。

## 2.2 几何概型 (Geometric Probability)

如果一个随机试验的样本空间 Ω 是一个可以度量其"大小"（如长度、面积、体积）的区域，并且每个基本事件（样本点）发生的可能性是均匀分布在该区域上的，则称此随机试验为几何概型。
对于任一事件 A（Ω 中的一个可度量子区域），其概率定义为：
\[ P(A) = \frac{\text{构成事件 A 的区域大小}}{\text{样本空间 Ω 的区域大小}} \]

*   例子：蒲丰投针问题 (Buffon's needle problem)，约会问题。

## 2.3 频率与统计概率 (Frequency and Statistical Probability)

在相同的条件下，进行 n 次重复独立的随机试验，事件 A 出现了 n<sub>A</sub> 次，则称比值 n<sub>A</sub>/n 为事件 A 在这 n 次试验中发生的**频率 (Frequency)**，记作 f<sub>n</sub>(A)。
当试验次数 n 很大时，频率 f<sub>n</sub>(A) 通常会稳定在某个常数 p 附近。这个稳定的常数 p 就被认为是事件 A 的**统计概率 (Statistical Probability)**。
\[ P(A) \approx f_n(A) = \frac{n_A}{n} \text{ (当 n 很大时)} \]
这种定义是基于经验的，是大数定律的体现。

## 2.4 公理化定义 (Axiomatic Definition of Probability)

由柯尔莫哥洛夫 (Kolmogorov) 提出，概率 P(A) 是定义在样本空间 Ω 的事件域 F (一个事件代数或 σ-代数) 上的一个实值函数，它满足以下三条公理：
1.  **非负性公理 (Non-negativity)** ：对于任意事件 A ∈ F，P(A) ≥ 0。
2.  **正则性公理/规范性公理 (Normalization)**：P(Ω) = 1。
3.  **可列可加性公理 (Countable Additivity)**：若 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>n</sub>, ... 是一列两两互不相容的事件 (即 A<sub>i</sub> ∩ A<sub>j</sub> = ∅，当 i ≠ j)，则：
    \[ P(\bigcup_{i=1}^{\infty} A_i) = \sum_{i=1}^{\infty} P(A_i) \]
    如果事件个数有限，则为有限可加性。

## 2.5 概率的基本性质 (Basic Properties of Probability)

由概率的公理化定义可以推导出以下重要性质：
1.  **不可能事件的概率**：P(∅) = 0。
2.  **有限可加性**：若 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>n</sub> 是两两互不相容的事件，则 P(∪<sub>i=1</sub><sup>n</sup> A<sub>i</sub>) = Σ<sub>i=1</sub><sup>n</sup> P(A<sub>i</sub>)。
3.  **概率的界限**：对于任意事件 A，0 ≤ P(A) ≤ 1。
4.  **对立事件的概率**：P(Aᶜ) = 1 - P(A)。
5.  **更一般事件的概率**：P(A - B) = P(A) - P(AB)。
6.  **单调性**：若 A ⊂ B，则 P(A) ≤ P(B)，且 P(B - A) = P(B) - P(A)。

## 2.6 加法公式与减法公式 (Addition and Subtraction Rules)

*   **两个事件的加法公式**：对于任意两个事件 A 和 B，
    \[ P(A \cup B) = P(A) + P(B) - P(A \cap B) \]
*   **三个事件的加法公式**：对于任意三个事件 A, B, C，
    \[ P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C) \]
*   **容斥原理 (Inclusion-Exclusion Principle)**：上述公式可以推广到 n 个事件。 