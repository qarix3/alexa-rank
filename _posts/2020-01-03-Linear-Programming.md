---
layout: post
title:  "Linear Programming"
date:   2020-01-03 23:22:40 +0300
---

Decision variables:

$$
\text{Let}  x_1 = \text{number of television unit} \\
x_2 = \text{number of radio unit} \\
x_3 = \text{number of newspaper unit}\\
x_4 = \text{number of magazine unit}\\
$$

Constrains: The restriction on the advertising bugdet is 

$$
60x_1 + 25x_2 + 20x_3 + 12x_4 \leq 700
$$

The other constrains, 

1. A
2. B
3. C


Thus, the LP model may be written as:

$$
\text{Intercept}\\
(x_1,x_2);(x_1,x_2)\\
(x_1,x_2);(x_1,x_2)\\
(x_1,x_2);(x_1,x_2)\\

\begin{alignat}{5}
\max \quad & z = & 30x_1  & + & 45x_2  &&&&& \\
\mbox{s.t.} \quad && 2x_1 & + & 5x_2 & + && \geq 100  &&\\
& & 4x_1 & & 8x_2 & + && \leq 240 && \\
& & & & x_2 & & & \geq 20 && \\
& & x_1, x_2 \geq 0 &&&
\end{alignat}

\\
\begin{array}{|r|r|r|r|} \hline
\text{Point} & x & y & z      \\ \hline
          A &   0 &  -3 &  0  \\
          B &   0 &  -9 & 0   \\
          C &   0 &   6 & 0   \\
          D &   1 &   0 &  0  \\ \hline
\end{array}
\\
$$
