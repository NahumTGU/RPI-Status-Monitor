import numpy as np
import matplotlib.pyplot as plt
import datetime
log=np.genfromtxt("status_log.txt",dtype=str)
timestr=log[:,1]
datestr=log[:,0]
print(timestr)

dt_objects = [datetime.datetime.strptime(a+' '+b, "%Y-%m-%d %H:%M:%S.%f") for a,b in zip(datestr,timestr)]


status=log[:,2].astype(int)

plt.figure(figsize=(10, 5))
plt.step(dt_objects, status, marker="o", linestyle="-", color="blue", label="Online Status")
#plt.step(dt_objects, status) #plt.step used for discrete changes in state
plt.title("Status of RPI over time")
plt.xticks(rotation=15, fontsize=8)  # Rotate and resize x-axis labels
plt.yticks([0, 1])#, ["Offline", "Online"])
plt.xlabel("TIME")
plt.ylabel("STATUS")
plt.show
plt.show(block=True)