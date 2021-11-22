import unittest
from game_durak import Durak, Player

class Test_game_durak_unittest(unittest.TestCase):

    def test_durak_init(self):
        d = Durak()
        self.assertTrue(d.attacker_index == 0)
        self.assertTrue(len(d.deck) == 36 - 2 * 6)

        d.finish_turn()

        self.assertEqual(d.attacker_index, 1)
        self.assertTrue(len(d.deck) == 36 - 12)

    def test_player(self):
        d = Durak()

        d.attack(d.current_player[0])
        d.finish_turn()

        self.assertEqual(d.attacker_index,0)
        self.assertTrue((d.current_player.n_cards != d.opponent_player.n_cards)&(d.opponent_player.n_cards == 7))
        self.assertTrue(d.opponent_player.n_cards != 6)
        self.assertEqual(d.current_player.n_cards, 6)
        self.assertTrue(len(d.deck) == 36 - 13)

    def test_trump_not_ace(self):
        for _ in range(10000):
            d = Durak()
            self.assertTrue(d.trump[0] != 'A')
            self.assertTrue(d.trump == d.deck[0][1])