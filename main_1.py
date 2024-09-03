from module_12_2 import Runner
from module_12_2 import Tournament
import unittest
from unittest import TestCase


# class TournamentTest(TestCase):
#     all_results = {}
#
#     @classmethod
#     def setUpClass(cls):
#         cls.all_results = {}
#
#     def setUp(self):
#         self.runners = [
#             Runner("Usain", 10),
#             Runner("Andrew", 9),
#             Runner("Nick", 3),
#         ]
#
#     @classmethod
#     def tearDownClass(cls):  # исправлено на cls вместо self
#         for key, value in cls.all_results.items():
#             print("{}:".format(key))
#             print("{}: {}".format(key, value))
#
#     def test_usain_and_nick(self):
#         tournament = Tournament(90, self.runners[0], self.runners[2])
#         result = tournament.start()
#         self.assertTrue(list(result.values())[-1].name == "Nick")
#         self.all_results["Результат первого забега"] = result
#     def test_andrey_and_nick(self):
#         tournament = Tournament(90, self.runners[1], self.runners[2])
#         result = tournament.start()
#         self.assertTrue(list(result.values())[-1].name == "Nick")
#         self.all_results["Результат второго забега"] = result
#     def test_usain_andrey_nick(self):
#         tournament = Tournament(90, *self.runners)
#         result = tournament.start()
#         self.assertTrue(list(result.values())[-1].name == "Nick")
#         self.all_results["Результат третьего забега"] = result
#
#     def test_usain_and_nick(self):
#         distance = 5
#         tournament = Tournament(90, *self.runners)
#         result = tournament.start()
#         self.assertTrue(list(result.values())[-1].name == "Nick")
#         self.all_results["Результат 4 забега"] = result
#
#
#
# if __name__ == "__main__":
#     unittest.main()


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = [
            Runner("Усейн", 10),
            Runner("Андрей", 9),
            Runner("Ник", 3),
        ]

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print("{}:".format(key))
            for k, v in value.items():
                print("{}: {}".format(k, v))

    def test_usain_and_nick(self):
        turn_1 = Tournament(90, self.runners[0], self.runners[2])
        result = turn_1.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Результат Усейна и Ника"] = result

    def test_andrey_and_nick(self):
        turn_2 = Tournament(90, self.runners[1], self.runners[2])
        result = turn_2.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Результат Андрея и Ника"] = result

    def test_usain_andrey_nick(self):
        turn_3 = Tournament(90, *self.runners)
        result = turn_3.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Результат общего забега"] = result



if __name__ == "__main__":
    unittest.main()