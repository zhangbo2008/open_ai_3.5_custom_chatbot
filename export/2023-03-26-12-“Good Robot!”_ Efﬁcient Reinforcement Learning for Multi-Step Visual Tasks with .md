## Paper:1




1. Title: "Good Robot!": Efficient Reinforcement Learning for Multi-Step Visual Tasks with Sim to Real Transfer


                 2. Authors: Andrew Hundt, Benjamin Killeen, Nicholas Greene, Hongtao Wu, Heeyeon Kwon, Chris Paxton, and Gregory D. Hager


                 3. Affiliation: Andrew Hundt, Benjamin Killeen, Nicholas Greene, Hongtao Wu, Heeyeon Kwon, and Gregory D. Hager are with The Johns Hopkins University, Baltimore, MD 21218 USA. Chris Paxton is with NVIDIA, Seattle, WA, 98105 USA.


                 4. Keywords: Reinforcement learning, computer vision, grasping and manipulation, sim to real transfer.


                 5. Urls: Paper: https://ieeexplore.ieee.org/document/9143366, Github: https://github.com/jhulcsr/good_robot


                 6. Summary: 
                    - (1): 该论文研究的背景是关于长时间视觉任务的强化学习算法。
  
                    - (2): 过去的方法往往无法处理长期任务，时间长、问题多，本文提出的方法在动作安全区域内探索，并能在不探索不安全区域的情况下学习。本文的方法通过在保证前进方向的情况下进行训练来学习。
  
                    - (3): 本文提出了一种 “SPOT” 框架，其中包括了安全约束条件以及优化学习的策略。此框架完成了各种任务，对于任务的成功率表现明显优于基线模型。此外我们对于学习结果进行了 sim 到 real 的转移，并且再理实践中表现良好。 
  
                    - (4): 本文使用 sim to real transfer 方法在长期视觉任务中表现出色，成功率从13%提升至100%。本文提出的方法不但成功率高，而且出奇的高效，且已经应用于实际机器人任务中。
7. Methods: 

- (1): 本文研究长时间视觉任务的强化学习算法，通过四个措施提高算法的学习效率，包括捕捉数据不变性、使用传统算法优化、保证奖励不通过失败动作传播以及引入不必要的探索算法。文章将问题转化为马尔可夫决策过程来解决，采用Q-learning算法训练。 

- (2): 本文针对reward shaping技术进行优化，提出了SPOT框架，其中包括了安全约束条件以及优化学习的策略，使得算法可用于保证动作安全区域内的探索。文章提出了基于状态转移概率函数P的奖励函数R，以及一种利用SR和RP的dynamic action space来训练的SPOT-Q学习算法。

- (3): 论文还介绍了一些实验环节，通过对实验结果的分析和总结发现，SPOT-Q算法具有显著的训练效率和表现优势，从而在长期视觉任务中提升了成功率和操作效率，实验结果证明了该方法的可行性。 

- (4): 文章还使用了sim to real的转移方法来转化学习结果，使得算法具有实际应用的可能性，并可以应用于机器人任务中。





8. Conclusion:  

- (1): 本文的意义在于提出了一种针对长时间视觉任务的强化学习算法，并通过SPOT框架提高了算法的学习效率和任务成功率。在实验中还引入了sim to real的转移方法，使得算法具有实际应用的可能性。

- (2): 创新点：文章提出了基于SPOT框架的奖励函数和dynamic action space，增加了算法对任务完成情况的监测和对探索的控制。表现：文章的算法成功率高且出奇的高效，已经应用于实际机器人任务中。工作量：文章的实验较为详细，但还有一些可以优化的地方，如学习任务结构等。




