import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import cnames

plt.figure(figsize=(10, 10))
plt.xlim(-60, 60)
plt.ylim(-60, 60)


class Analytics:
    def __init__(self, buffer):
        self.buffer = buffer

    def get_pitch_movement_data(self, csv_name):
        """
        csvファイルからボールの変化量のデータを抽出してグラフにし、画像として出力する関数
        """
        df = pd.read_csv(csv_name)
        pitch_types = [
            "4-Seam Fastball",
            "2-Seam Fastball",
            "Cutter",
            "Sinker",
            "Split-Finger",
            "Slow Curve",
            "Slider",
            "Curveball",
            "Sweeper",
            "Screwball",
        ]
        colors = [
            "red",
            "brown",
            "orange",
            "aqua",
            "olive",
            "magenta",
            "lime",
            "pink",
            "purple",
            "navy",
            "gray",
            "silver",
            "tan",
            "peru",
        ]

        s = set()
        for index, row in df.iterrows():
            if row["pitch_name"] not in pitch_types:
                pitch_types.append(row["pitch_name"])
                for color in cnames.keys():
                    if color not in colors:
                        colors.append(color)
                        break
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
