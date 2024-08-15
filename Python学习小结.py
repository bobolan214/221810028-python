import pandas as pd
import matplotlib.pyplot as plt

# 生成一些示例天气数据
data = {
    'date': pd.date_range(start='2024-08-01', end='2024-08-10'),
    'temperature': [30, 32, 31, 33, 34, 35, 36, 37, 38, 39],  # 假设的气温数据（单位：摄氏度）
    'humidity': [60, 65, 70, 55, 50, 45, 40, 35, 30, 25]  # 假设的湿度数据（单位：百分比）
}

df = pd.DataFrame(data)

# 绘制温度和湿度随时间的变化图
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['temperature'], marker='o', label='Temperature (°C)')
plt.plot(df['date'], df['humidity'], marker='o', label='Humidity (%)')

plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Weather Analysis')
plt.xticks(rotation=45)  # 设置横坐标标签旋转45度
plt.legend()
plt.grid(True)
plt.tight_layout()  # 调整布局，避免标签重叠
plt.show()
