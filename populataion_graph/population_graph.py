import matplotlib.pyplot as plt 

file = open('UE5_EcoSystemSim_2025_10_16.log', 'r')
read = file.readlines()
file.close()

dataset = []

print("read line: " + str(len(read)))

for line in read:
    if ('BP_GameMode' in line):
        dataset.append(line)


print("dataset num: " + str(len(dataset)))

Foxes = []
Hares = []
Plants = []

for data in dataset:
    if 'Foxes' in data:
        Foxes.append(int(data.split('Foxes: ')[1].split(',')[0]))
    if 'Hares' in data:
        Hares.append(int(data.split('Hares: ')[1].split(',')[0]))
    if 'Plants' in data:
        Plants.append(int(data.split('Plants: ')[1].split(',')[0]))

print("Foxes num: " + str(len(Foxes)))
print("Hares num: " + str(len(Hares)))
print("Plants num: " + str(len(Plants)))

time_axis = [i * 5 for i in range(len(Foxes))]

plt.plot(time_axis, Foxes, label='Foxes', color='red')
plt.plot(time_axis, Hares, label='Hares', color='blue')
plt.plot(time_axis, Plants, label='Plants', color='green')
plt.xlabel('Simulation time [seconds]')
plt.ylabel('Population')
plt.title('Ecosystem Simulation')
plt.legend()
plt.show()
