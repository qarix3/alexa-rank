---
layout: post
title:  "Inventory Control Models"
date:   2020-01-05 23:22:40 +0300
---

$$
\text{Number of order made in a year = (anual demand)/(reorder quatity)} = D/Q \\
\text{Total ordering cost for one year} = C_o \times \text{(number of orders)} = C_oD/Q \\
\text{Maximum inventory level}= I_m = Q\\
The inventory cycle time = Q/D (in years)\\
The average inventory level = (minimum level + maximum level)/2 = (0 + Q)/2 = Q/2\\
Total holding cost for one year = C_h \times (average inventory) = C_hQ/2\\
Total cost of having stock (T) for one year = C_oD/Q + C_hQ/2\\

lead time = delivery time = reorder point \\
ROP = (\text{demand per day or week}) \times (lead time for an order in days or weeks) = D X L\\


D = \text{ demand forecast in units for a given period} \\
C_o = \text{cost of making one order} \\
C_h = \text{holding cost per unit of average stock over the same period}\\
Q = \text{the order quantity} \\

\text{Demand rate}, D = 1500 boxes/year \\
\text{Purchase cost}, C = RM 3.50/unit \\
\text{Holding cost}, Ch = 0.25 \\
\text{Ordering cost}, Co =  RM30/order \\

\begin{array}{|r|r|} \hline
\text{Quatity} &\text{Discount} & \text{C} \\ \hline
0 - 299 & 0\% & 3.50\\
300 - 499 & 5\% & 0.95(3.50) = 3.325\\
500 - more & 10\% & 0.90(3.50) = 3.15 \\ \hline

\end{array}
\\
\begin{align}
EOQ & = \sqrt{\frac{2C_oD}{C_h}} \\
EOQ_1 & = \sqrt{\frac{2\left(1500\right)\left(30\right)}{0.25\left(3.5\right)}} \approx 320.71 \tag{No adjustment}\\ 
EOQ_2 & = \sqrt{\frac{2\left(1500\right)\left(30\right)}{0.25\left(3.325\right)}} \approx 329 \tag{No adjustment}\\
EOQ_3 & = \sqrt{\frac{2\left(1500\right)\left(30\right)}{0.25\left(3.315\right)}} \approx 338 \tag{Adjust to 500}\\ 
\end{align}

\\
TC = DC + \frac{D}{Q} C_o + \frac{Q}{2} C_h \\
TC_2 = (1500)(3.325) + \frac{1500}{329}(30) + \frac{329}{2}(0.25) = RM 5261 \\
TC_3 = (1500)(3.15) + \frac{1500}{500}(30) + \frac{500}{2}(0.25) = RM 4991.22\\

\therefore\text{The optimal order quality is when order quality, Q = 500 boxes}

$$

