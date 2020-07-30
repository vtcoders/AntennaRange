# PlotGraph.py
# Plots the provided data and shows the plot in a new window.


import math
import matplotlib.pyplot as plt


class PlotGraph():
    def __init__(self, data, title):
        # parse data
        self.title = title
        self.mast_angles = []
        self.arm_angles = []
        self.rssi = []
        for entry in data:
            mast_angle,arm_angle,background_rssi,transmit_rssi = entry
            self.mast_angles.append(float(mast_angle))
            self.arm_angles.append(float(arm_angle))
            self.rssi.append(float(transmit_rssi)-float(background_rssi))


    def show(self):
        # plot the data
        ax = plt.subplot(111, projection='polar')
        theta = [angle*(math.pi/180) for angle in self.mast_angles]
        ax.plot(theta, self.rssi)
        ax.set_rmax(60)
        ax.set_rticks([0, 20, 40, 60])
        ax.set_rlabel_position(-22.5)
        ax.set_xticklabels(['0', '45', '90', '135', '180', '-135', '-90', '-45'])
        ax.grid(True)
        ax.set_title(self.title, va="bottom")
        plt.show()

