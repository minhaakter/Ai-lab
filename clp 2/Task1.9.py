import matplotlib.pyplot as plt
temp_data = list(map(int, input("Enter temperatures for a week separated by space: ").split()))
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
plt.plot(days, temp_data, marker='o')
plt.title("Temperature Variations Over a Week")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.show()