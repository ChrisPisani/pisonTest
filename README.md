# pisonTest
![](https://i.gyazo.com/a31e922456c12109aaa714aec4db4fa7.png)

The process that I used to go about solving this problem involved using python to parse the data and print statistics that I thought would be important to evaluate the problem. those data points that I thought were important consisted of the maximum, minimum, and average latency of the file based off the timestamps. Using this data, it became apparant that the CD23 device had much larger average latency's then that of the F0AC and E638 devices. With latency's as high as 250, and averages that ranged from 8-17ms, it was clear that the CD23 device was not performing as well as the F0AC and E638 devices, who both had average latency's around 3ms. This major difference in performance leads to the conclusion that the CD23 device is the one that is malfunctioning.

---

## Running Project

1. Clone the project to a repository

2. Download Python (The version I am using is 3.7.4)

3. Go to repository and type: 
```
py parse.py
```

4. Statistics should print to the console
