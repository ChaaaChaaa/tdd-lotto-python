from enum import Enum


class Reward(Enum):
    MATCH_3 = 5000
    MATCH_4 = 50000
    MATCH_5 = 1500000
    MATCH_6 = 2000000000
    MATCH_BONUS = 30000000


# class MATCH(Enum): #이름 마음에 안들음
#     3 = "MATCH_3"

class MatchCount(Enum):
    THREE = (3,Reward.MATCH_3)
    FOUR = (4,Reward.MATCH_4)
    FIVE = (5,Reward.MATCH_5)
    SIX = (6,Reward.MATCH_6)
    BONUS = (7,Reward.MATCH_BONUS)

    def __init__(self,count,reward):
        self.count = count
        self.reward = reward

    @staticmethod
    def get_reward(count):
        for match in MatchCount:
            if match.count == count:
                return match.reward.value
        return 0
