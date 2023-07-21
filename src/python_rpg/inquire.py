from InquirerPy.resolver import prompt


class Inquire:
    def __init__(self,name):
        self.name = name
        self.job_obj = {
            "魔法職": ["魔法使い", "僧侶", "賢者"],
            "近接職": ["戦士", "騎士", "忍者"],
            "遠距離職": ["弓使い", "狩人", "銃士"],
            "その他": ["踊り子", "吟遊詩人", "侍"],
        }
        pass

    # function to menu inquirer
    def menu(self):
        menu = [
            {
                "type": "list",
                "message": "--メニュー--",
                "choices": ["冒険にいく", "パーティーをみる", "終了する"],
                "default": "ダンジョン",
            },
        ]
        answer = prompt(menu)
        if answer.get(0) == "冒険にいく":
            return self.dungeon()
        return answer

    def dungeon(self):
        dungeon = [
            {
                "type": "list",
                "message": "--冒険にいく--",
                "choices": ["はじまりの森", "終了する"],
                "default": "はじまりの森",
            },
        ]
        answer = prompt(dungeon)
        return answer

    def party(self, obj):
        depth = obj

    def job(self):
        self.ans_job:object
        while True:
            job_list = [
                {
                    "type": "list",
                    "message": f"--{self.name}職業を選択してください--",
                    "choices": ["魔法職", "近接職", "遠距離職", "その他"],
                    "default": "魔法職",
                },
            ]
            ans_job_list = prompt(job_list)
            job_choices = self.job_obj[str(ans_job_list.get(0))]
            job_choices.append("戻る")
            job = [
                {
                    "type": "list",
                    "message": f"--{self.name}の職業を選択してください--",
                    "choices": job_choices,
                    "default": job_choices[0],
                },
            ]
            self.ans_job = prompt(job)
            if self.ans_job.get(0) == "戻る":
                continue
            break
        return self.ans_job.get(0)