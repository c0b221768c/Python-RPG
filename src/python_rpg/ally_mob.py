import random


class MagicalJob:
    """
    魔法職に関するクラス
    """

    def __init__(self, name, job):
        # 基本情報
        self.MP = random.randint(2, 5)
        # パラメータ
        self.parameter = {
            "STR": random.randint(1, 3),
            "VIT": random.randint(1, 3),
            "INT": random.randint(3, 5),
        }
        # 能力値
        self.ability_status = {
            "ATK": 1 * self.parameter["STR"],
            "DEF": 1 * self.parameter["VIT"],
            "RES": 3 * self.parameter["INT"],
            "AGI": random.randint(1, 3),
            "DEX": random.randint(1, 3),
            "LUK": random.randint(1, 5),
        }
        # 基本ステータス
        self.base_status = {
            "Name": name,
            "Job": job,
            "Level": 1,
            "HP": self.parameter["VIT"] + self.ability_status["DEF"],
            "MP": self.MP * self.parameter["INT"],
            "EXP": 0,
        }


class CloseRangeJob:
    """
    近接職に関するクラス
    """

    def __init__(self, name, job):
        # パラメータ
        self.parameter = {
            "STR": random.randint(5, 10),
            "VIT": random.randint(5, 10),
            "INT": random.randint(1, 3),
        }
        # 能力値
        self.ability_status = {
            "ATK": 1,
            "DEF": 1,
            "RES": 1,
            "AGI": 1,
            "DEX": 1,
            "LUK": 1,
        }
        # 基本ステータス
        self.base_status = {
            "Name": name,
            "Job": job,
            "Level": 1,
            "HP": 1,
            "MP": 1,
            "EXP": 0,
        }


class RemoteRangeJob:
    """
    遠距離職に関するクラス
    """

    def __init__(self, name, job):
        # パラメータ
        self.parameter = {
            "STR": random.randint(3, 7),
            "VIT": random.randint(3, 5),
            "INT": random.randint(1, 5),
        }
        # 能力値
        self.ability_status = {
            "ATK": 1,
            "DEF": 1,
            "RES": 1,
            "AGI": 1,
            "DEX": 1,
            "LUK": 1,
        }
        # 基本ステータス
        self.base_status = {
            "Name": name,
            "Job": job,
            "Level": 1,
            "HP": 1,
            "MP": 1,
            "EXP": 0,
        }


class OtherJob:
    """
    その他職に関するクラス
    """

    def __init__(self, name, job):
        # パラメータ
        self.parameter = {
            "STR": random.randint(1, 5),
            "VIT": random.randint(1, 5),
            "INT": random.randint(8, 10),
        }
        # 能力値
        self.ability_status = {
            "ATK": 1,
            "DEF": 1,
            "RES": 1,
            "AGI": 1,
            "DEX": 1,
            "LUK": 1,
        }
        # 基本ステータス
        self.base_status = {
            "Name": name,
            "Job": job,
            "Level": 1,
            "HP": 1,
            "MP": 1,
            "EXP": 0,
        }


a = MagicalJob("a", "b")
print(a.base_status, a.parameter, a.ability_status)
