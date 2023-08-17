# Opening a file
import matplotlib.pyplot as plt
file = open("sample.txt", "r")
Counter = 0

# Reading from file
file_content = file.read()
content_list = file_content.split("\n")


meta_data_raw = content_list[:5]

meta_data = {}
for item in meta_data_raw:
    key, val = item.split(":", 1)
    meta_data[key.strip()] = val.strip()


pressure_data_raw = content_list[5:]

pressures = []
for item in pressure_data_raw:
    key, val = item.split(":", 1)
    pressures.append(float(val.strip()))

print(len(pressures))

for i in range(len(pressures)):
    pressures[i] = 1.0


for i in range(len(pressures)):
    if i <= 10:
        pressures[i] = 8.0
    if 10 < i < 20:
        # tryck från 8 till 5 under tiden 10-20 sekunder
        step = (8-5)/(20-10)
        print(step)
        pressures[i] = last_pressure-step

    last_pressure = pressures[i]


print(pressures)

# adds pressures to the dict
meta_data['PRESSURES'] = pressures

# print(pressures)
# print(meta_data)

plt.plot(pressures)
plt.show()
