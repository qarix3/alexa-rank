---
layout: post
title:  "Project Management with PERT"
date:   2020-01-06 23:22:40 +0300
---
$$
\begin{array}{|r|r|r|r|} \hline
\text{Activity} & \text{Earlier Activity} & \text{a} & \text{m} & \text{b}\\ \hline
         A &   - &   & \\
         B &   - &   &  \\
         C &   A,B & &  \\
         D &   D,E & &   \\
         E &   C &   &   \\ \hline
\end{array} \\

\text{The estimated time} \left(t \right) \text{and variance}\left(s^2\right) \\

t = (\frac{a + 4m + b}{6})\\
s^2 = (\frac{b-a}{6})^2\\

\begin{array}{|r|r|} \hline
\text{Activity} & \text{Expected Time}\left(t\right) & \text{Variance} \left(s^2\right) & Slack \\ \hline
         A &   && 4   \\
         B &   && 0  \\
         C &   &&   \\
         D &   &&   \\
         E &   &&   \\ \hline
\end{array} \\
\text{The probability that project will be completed within 42 weeks}\\

P(X \leq x) = P(Z \leq (x - \mu)/\sigma)

x = \frac{\text{new duration-total duration}}{variance}
$$

**tips: dapat nombor bulat pergi tngok table**

![alt text](/assets/pert.jpg)