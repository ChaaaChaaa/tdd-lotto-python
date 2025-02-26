import unittest
from src.lotto.rewards import Reward, MatchCount


class TestRewards(unittest.TestCase):

    def test_reward_enum(self):
        self.assertEqual(Reward.MATCH_3.value, 5000)
        self.assertEqual(Reward.MATCH_4.value, 50000)
        self.assertEqual(Reward.MATCH_5.value, 1500000)
        self.assertEqual(Reward.MATCH_6.value, 2000000000)
        self.assertEqual(Reward.MATCH_BONUS, 30000000)

    def test_match_count_enum(self):
        self.assertEqual(MatchCount.THREE.count, 3)
        self.assertEqual(MatchCount.FOUR.count, 4)
        self.assertEqual(MatchCount.FIVE.count, 5)
        self.assertEqual(MatchCount.SIX.count, 6)
        self.assertEqual(MatchCount.BONUS, 7)

        self.assertEqual(MatchCount.THREE.reward, Reward.MATCH_3)
        self.assertEqual(MatchCount.FOUR.reward, Reward.MATCH_4)
        self.assertEqual(MatchCount.FIVE.reward, Reward.MATCH_5)
        self.assertEqual(MatchCount.SIX.reward, Reward.MATCH_6)
        self.assertEqual(MatchCount.BONUS.reward, Reward.MATCH_BONUS)

    def test_get_reward(self):
        self.assertEqual(MatchCount.get_reward(3), 5000)
        self.assertEqual(MatchCount.get_reward(4), 50000)
        self.assertEqual(MatchCount.get_reward(5), 1500000)
        self.assertEqual(MatchCount.get_reward(6), 2000000000)
        self.assertEqual(MatchCount.get_reward(7), 30000000)
        self.assertEqual(MatchCount.get_reward(2), 0)


if __name__ == '__main__':
    unittest.main()
