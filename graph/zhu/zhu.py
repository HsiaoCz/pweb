import matplotlib.pyplot as plt

# 数据
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]

# 创建图表
plt.bar(categories, values)

# 添加标题和标签
plt.title('示例柱状图')
plt.xlabel('类别')
plt.ylabel('值')

# 显示图表
plt.show()