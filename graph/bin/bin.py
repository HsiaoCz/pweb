import matplotlib.pyplot as plt

# 数据
labels = "Frogs", "Hogs", "Dogs", "Logs"
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # 只“弹出”第二个切片（即'Hogs'）

# 创建图表
fig1, ax1 = plt.subplots()
ax1.pie(
    sizes, explode=explode, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90
)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

# 显示图表
plt.show()
