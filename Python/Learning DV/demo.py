import matplotlib.pyplot as plt

x=["pyhton","rust","java","c++"]
y=[40,30,10,20]

c=["r","g","b","y"]

plt.title("Audience Analyser")
plt.xlabel("Languages")
plt.ylabel("No. of liked people")

plt.bar(x,y,width=0.4,color="m",align="center",label="popularity",edgecolor="r",linestyle=":",alpha=0.35)
plt.legend()
plt.show()