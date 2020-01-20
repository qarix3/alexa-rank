---
layout: post
title:  "Decision Theory"
date:   2020-01-02 23:22:40 +0300
---

- Magazine cost = RM 4
- Magazine sell = RM 6
- Reclaim = RM 3
- Loss = RM 0.50

## Decision Table or Payoff
$$
\begin{array}{|r|r|r|r|}\hline
& \text{Payoffs} & \text{Demand 100} & \text{Demand 150} & \text{Demand 200} & \text{Demand 250} & \text{Demand 300}\\ \hline
         & 100 & 100(6-4)=200 & 100(6-4)-50(0.5)=175 & 100(6-4)-100(0.5)=150 & 100(6-4)-150(0.5)=125 & 100(6-4)-200(0.5)=100 \\
         & 150 & 100(6-4)-50(4-3)=150 & 150(6-4)=300 & 150(6-4)-50(0.5) = 275 & 150(6-4)-100(0.5)=250 & 150(6-4)-150(0.5)=225 \\
         & 200 & 100(6-4)-100(4-3)=100 & 150(6-4)-50(4-3)=250 & 200(6-4)=400 & 200(6-4)-50(0.5)=375 & 200(6-4)-100(0.5)=350 \\
         & 250 & 100(6-4)-150(4-3)=50 & 150(6-4)-(4-3)=200 & 200(6-4)-50(4-3)=350 & 250(6-4)=500 & 250(6-4)-50(0.5) = 475\\
         & 300 & 100(6-4)-200(4-3)=0 & 150(6-4)-150(4-3)=150 & 200(6-4)-100(4-3)=300 & 250(6-4)-50(4-3)=200 & 300(6-4)=600 \\ \hline
\end{array}
$$

Maximum Criterion: (optimistic)

***tips:find largest value in table***

$$
\begin{array}{r|r}
\text{Alternative} & \text{Maximum payoff(RM)}\\ \hline
         100 & 200  \\
         150 & 300  \\
         200 & 400  \\
         250 & 500  \\
         300 & 600 \leftarrow\\
\end{array}
$$

Minimum Criterion: (pessimistic)

***tips:find lowest value in table then cari yg plg bsar***

$$
\begin{array}{r|r}
\text{Alternative} & \text{Minimum payoff(RM)}\\ \hline
         100 & 100  \\
         150 & 150  \leftarrow\\
         200 & 100  \\
         250 & 50  \\
         300 & 0 \\
\end{array}
$$

***tips:paling besar row tolak each column***

 $$

\begin{array}{|r|r|r|r|}\hline
& \text{Opportunity Loss} & \text{100} & \text{150} & \text{200} & \text{250} & \text{300} \\ \hline
         & 100 & 0 & 300-175 & 400-150 & 500-125 & 600-100\\
         & 150 & 200-150=50 & 0 & 275 & 500-250 & 600-225 \\
         & 200 & 200-100=100 & 300-250=50 & 0 & 500-375 & 600-350 \\
         & 250 & 200-150-50 & 300-200=100 & 400-1350 & 0 & 600-475\\
         & 300 & 200-0-200  & 300-150=150 & 400-1300 & 500-200 & 0 \\ \hline
\end{array}
$$

Minimax regret: (opportunity loss)

***tips:find lowest value in table***

$$
\begin{array}{r|r}
\text{Alternative} & \text{Minimum payoff(RM)}\\ \hline
         100 & 500  \\
         150 & 375  \\
         200 & 250  \\
         250 & 150 \leftarrow\\
         300 & 200 \\
\end{array}
$$

$$
EMV = \sum_{j=1}^kP_jp_{ij}\\

\begin{array}{|r|r|r|r|}\hline
& \text{Expected Payoffs} & \text{Demand 100} & \text{Demand 150} & \text{Demand 200} & \text{Demand 250} & \text{Demand 300} &  \text{EMV}  \\ \hline
         & 100 & 200 \times 0.1 = 20 & 175 \times 0.2 = 20 & 150 \times 0.3 = 20 & 125 \times 0.3 = 20 & 100 \times 0.1 = 20 & 147.5\\
         & 150 & 150 \times 0.1 = & 300 \times 0.1 = 20 & 275 & 250 & 225 \\
         & 200 & 100 \times 0.1 = & 250 \times 0.1 = 20 & 400 & 375 & 350 \\
         & 250 & 50 \times 0.1 = & 200 \times 0.1 = 20 & 350 & 500 & 475\\
         & 300 & 0 \times 0.1 = & 150 \times 0.1 = 20 & 300 & 200 & 600 \\ \hline
         & \text{Probability} & 0.1 & 0.2 & 0.3 & 0.3 & 0.1 \\ \hline
\end{array}
$$


***jawapan daripada opportunity loss kali dgn probabilility***

$$
EOL_i = \sum_{j=1}^kP_jl_{ij} \\
\begin{array}{|r|r|r|r|}\hline
& \text{Expected Losses} & \text{Demand 100} & \text{Demand 150} & \text{Demand 200} & \text{Demand 250} & \text{Demand 300} &  \text{EOL}  \\ \hline
         & 100 & 0 \times 0.1 = 0 & 125 \times 0.2 = 25 & 250 \times 0.3 = 75 & 375 \times 0.3 =112.5 & 500 \times 0.1=50 & 262.5\\
         & 150 & 150 \times 0.1 = & 0 & 0 & 250 & 225 \\
         & 200 & 100 \times 0.1 = & 250 & 0 & 375 & 350 \\
         & 250 & 50 \times 0.1 = & 200 & 350 & 0 & 475\\
         & 300 & 0 \times 0.1 = & 150 & 300 & 200 & 0 \\ \hline
         & \text{Probability} & 0.1 & 0.2 & 0.3 & 0.3 & 0.1 \\ \hline
\end{array}
\\

EVPI = EP_{with}PI - EP{without}PI = \sum_{i=1}^k P_im_i - max(EMV)

$$

***tips: cari highest kat table EMV pastu tambah semua column yg highest***
