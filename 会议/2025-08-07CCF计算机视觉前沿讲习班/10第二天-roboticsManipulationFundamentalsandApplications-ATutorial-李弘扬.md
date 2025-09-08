什么是 Robotics Manipulation？
- 在机器人和物体之间, 在环境中的交互
- 将一些 observation 转换为 action.
	- Observation: 如指令、参数、
	- Action: 对现实世界的交互

任务分解: 任务可以分解为 High Level Planner 与 Low level Policy, 即决策与执行这两个方面.

训练分类: 第一部分为强化学习. 如果没有一种显式的数据, 就要使用强化学习. 另一部分为模仿学习, 在上一份编号为 9 的报告中有记录.