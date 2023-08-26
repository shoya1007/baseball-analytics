from pybaseball import statcast_pitcher, playerid_lookup

class DataCollector:
    def __init__(self, first_name, last_name, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.player_id = self._get_player_id(first_name, last_name)
        self.player_name = first_name.capitalize() + last_name.capitalize()

    def _get_player_id(self, first_name, last_name):
        """
        選手IDを取得する関数
        """
        player_data = playerid_lookup(last_name, first_name)
        return player_data["key_mlbam"][0]

    def _get_pitching_stats(self):
        """
        ピッチングデータを取得する関数
        """
        stats = statcast_pitcher(self.start_date, self.end_date, self.player_id)
        return stats.dropna(subset=["pitch_name"])

    def create_pitching_stats_csv(self):
        """
        ピッチングデータをcsvに出力する関数
        """
        stats = self._get_pitching_stats()
        csv_name = f"./csv_data/{self.player_name}_{self.start_date}_{self.end_date}_pitching_data.csv"
        stats.to_csv(csv_name, index = False)
        return csv_name
