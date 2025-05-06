# 3. 条件概率与事件的独立性 (Conditional Probability and Independence of Events)

本章讨论在一个事件发生的条件下另一个事件发生的概率，以及事件之间相互独立的性质。

## 3.1 条件概率 (Conditional Probability)

设 A, B 是两个事件，且 P(B) > 0，则在事件 B 发生的条件下事件 A 发生的**条件概率 (Conditional Probability)** 定义为：
\[ P(A|B) = \frac{P(AB)}{P(B)} \]
条件概率满足概率的所有公理和性质。
*   例子：已知掷出的骰子点数为偶数，求点数为2的概率。

## 3.2 乘法公式 (Multiplication Rule)

由条件概率的定义，可以直接得到概率的乘法公式：
*   如果 P(B) > 0，则 P(AB) = P(B)P(A|B)
*   如果 P(A) > 0，则 P(AB) = P(A)P(B|A)

推广到多个事件 (例如三个事件 A, B, C)：
\[ P(ABC) = P(A)P(B|A)P(C|AB) \]
要求 P(A) > 0, P(AB) > 0。

## 3.3 全概率公式 (Law of Total Probability)

设 B<sub>1</sub>, B<sub>2</sub>, ..., B<sub>n</sub> 是样本空间 Ω 的一个划分 (Partition)，即 B<sub>i</sub> 两两互不相容，且 ∪<sub>i=1</sub><sup>n</sup> B<sub>i</sub> = Ω，并且 P(B<sub>i</sub>) > 0 (i=1, 2, ..., n)。则对任意事件 A，有：
\[ P(A) = \sum_{i=1}^{n} P(B_i)P(A|B_i) \]
全概率公式的意义在于，它可以将一个复杂事件的概率计算分解为若干个在不同条件下发生的简单事件的概率计算。

## 3.4 贝叶斯公式 (Bayes' Theorem)

在全概率公式的条件下，若 P(A) > 0，则有：
\[ P(B_k|A) = \frac{P(B_k A)}{P(A)} = \frac{P(B_k)P(A|B_k)}{\sum_{i=1}^{n} P(B_i)P(A|B_i)} \]
其中 k = 1, 2, ..., n。
贝叶斯公式是"执果索因"的工具：已知结果 A 发生了，我们想知道这个结果是由哪个原因 B<sub>k</sub> 引起的概率。P(B<sub>k</sub>) 称为先验概率 (Prior Probability)，P(B<sub>k</sub>|A) 称为后验概率 (Posterior Probability)。
*   例子：医学诊断，产品质量检测。

## 3.5 事件的独立性 (Independence of Events)

*   **两个事件的独立性**：
    设 A, B 为两个事件，如果其中一个事件的发生不影响另一个事件发生的概率，则称事件 A 与事件 B 相互独立。数学定义为：
    \[ P(AB) = P(A)P(B) \]
    若 P(A) > 0, P(B) > 0，则事件 A, B 独立的充要条件是 P(B|A) = P(B) 或 P(A|B) = P(A)。
    *   性质：若 A, B 独立，则 A 与 Bᶜ，Aᶜ 与 B，Aᶜ 与 Bᶜ 也相互独立。
*   **多个事件的相互独立性**：
    设 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>n</sub> 是 n 个事件，如果对于任意 k (2 ≤ k ≤ n) 和任意的下标组合 1 ≤ i<sub>1</sub> < i<sub>2</sub> < ... < i<sub>k</sub> ≤ n，都有：
    \[ P(A_{i_1} A_{i_2} ... A_{i_k}) = P(A_{i_1}) P(A_{i_2}) ... P(A_{i_k}) \]
    则称这 n 个事件相互独立。
    注意：多个事件两两独立并不一定能推出它们相互独立。
*   例子：从一副扑克牌中抽牌，有放回抽样和无放回抽样。

## 3.6 条件独立性 (Conditional Independence)

给定事件 C 发生的条件下，事件 A 和 B 相互独立，则称 A 和 B 关于 C 条件独立，记为 A ⊥ B | C。
数学定义为：
\[ P(AB|C) = P(A|C)P(B|C) \]
或者等价地，若 P(A|C) > 0, P(B|C) > 0，则 P(A|BC) = P(A|C) 或 P(B|AC) = P(B|C)。
条件独立性在概率图模型 (如贝叶斯网络) 中有重要应用。 