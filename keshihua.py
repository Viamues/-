import matplotlib.pyplot as plt

with open("2.txt", "r") as f:
    a1 = f.readlines()
    f.close()
a2 = []
time = []
b = 0y
for a3 in a1:
   a2.append(a3[13:18])
for i in range(0,170,10):
    time.append(i)
time.reverse()
y = a2
x = time
plt.plot(x,y,color = "green")
plt.ylabel("Unit: 10000 people")  #轴注释
plt.xlabel("min")                 #x轴注释
plt.title("xxx's fans")
plt.show()
