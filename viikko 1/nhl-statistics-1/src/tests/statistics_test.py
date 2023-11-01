import unittest
from statistics_service import StatisticsService
from player import Player
from index import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = str(self.stats.search('Semenko'))
        self.assertEqual(player, str(Player("Semenko", "EDM", 4, 12)))

    def test_search_not_existing_player(self):
        player = self.stats.search('Testi')
        self.assertEqual(player, None)

    def test_team(self):
        players = self.stats.team('PIT')
        self.assertEqual(list(map(str, players)), [str(Player("Lemieux", "PIT", 45, 54))])

    def test_top(self):
        top = self.stats.top(2)
        self.assertEqual(list(map(str, top)), [str(Player("Gretzky", "EDM", 35, 89)), str(Player("Lemieux", "PIT", 45, 54)), str(Player("Yzerman", "DET", 42, 56))])

    def test_sort_by_goals(self):
        top = self.stats.top(0, SortBy.GOALS)
        self.assertEqual(list(map(str, top)), [str(Player("Lemieux", "PIT", 45, 54))])

    def test_sort_by_assists(self):
        top = self.stats.top(0, SortBy.ASSISTS)
        self.assertEqual(list(map(str, top)), [str(Player("Gretzky", "EDM", 35, 89))])
