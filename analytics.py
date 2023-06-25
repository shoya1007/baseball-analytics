import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ShoheiOhtani_20230602_pitching_data.csv")

plt.figure(figsize=(10, 10))
plt.xlim(-60, 60)
plt.ylim(-60, 60)

class Analytics:
    def __init__(self, buffer):
        self.buffer = buffer

    def get_analytiics_result(self):
        pitch_types = ["4-Seam Fastball", "2-Seam Fastball", "Cutter", "Sinker", "Split-Finger", "Slow Curve", "Slider", "Curveball", "Sweeper", "Screwball"]
        colors = ["red", "brown", "orange", "aqua", "olive", "magenta", "lime", "pink", "purple", "navy", "gray", "silver", "tan", "peru"]

        s = set()
        for index, row in df.iterrows():
            x = row["pfx_x"] * (-30.48)
            z = row["pfx_z"] * 30.48
            n = pitch_types.index(row["pitch_name"])
            if n not in s:
                s.add(n)
                plt.scatter(x, z, color=colors[n], label=row["pitch_name"])
            else:
                plt.scatter(x, z, color=colors[n])

        plt.legend(loc="upper left", fontsize=14)
        plt.savefig(self.buffer, format="png")
        self.buffer.seek(0)
        plt.close()
