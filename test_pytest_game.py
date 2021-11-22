import pytest
from game_durak import Durak, Player

class Test_game_durak:

    def test_durak_init(self):
        d = Durak()
        assert d.attacker_index == 0
        assert len(d.deck) == 36 - 2 * 6

        d.finish_turn()

        assert d.attacker_index == 1
        assert len(d.deck) == 36 - 12

    def test_player(self):
        d = Durak()

        d.attack(d.current_player[0])
        d.finish_turn()

        assert d.attacker_index == 0
        assert d.current_player.n_cards != d.opponent_player.n_cards == 7

        assert d.opponent_player.n_cards != 6
        assert d.current_player.n_cards == 6
        assert len(d.deck) == 36 - 13

    def test_trump_not_ace(self):
        for _ in range(10000):
            d = Durak()
            assert d.trump[0] != 'A'
            assert d.trump == d.deck[0][1]