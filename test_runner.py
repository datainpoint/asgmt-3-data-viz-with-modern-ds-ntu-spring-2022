import unittest
import sqlite3
import numpy as np
import ipynb.fs.full.exercises as ex

connection = sqlite3.connect('nba.db')
class TestAssignmentThree(unittest.TestCase):
    def test_01_retrieve_table_list_from_nbadb(self):
        table_list_from_nbadb = ex.function_retrieve_table_list_from_nbadb(connection)
        self.assertEqual(table_list_from_nbadb.shape, (3, 2))
        types = table_list_from_nbadb.iloc[:, 0].values
        names = table_list_from_nbadb.iloc[:, 1].values
        self.assertIn("table", types)
        self.assertIn("career_summaries", names)
        self.assertIn("players", names)
        self.assertIn("teams", names)
    def test_02_retrieve_table_info_from_nbadb(self):
        table_info_from_nbadb = ex.function_retrieve_table_info_from_nbadb(connection)
        self.assertEqual(table_info_from_nbadb.shape, (3, 3))
        names = table_info_from_nbadb.iloc[:, 0].values
        self.assertIn("career_summaries", names)
        self.assertIn("players", names)
        self.assertIn("teams", names)
        number_of_rows = table_info_from_nbadb.iloc[:, 1].values
        self.assertIn(502, number_of_rows)
        self.assertIn(30, number_of_rows)
        number_of_columns = table_info_from_nbadb.iloc[:, 2].values
        self.assertIn(31, number_of_columns)
        self.assertIn(18, number_of_columns)
        self.assertIn(12, number_of_columns)
    def test_03_count_players_from_each_country(self):
        players_from_each_country = ex.function_count_players_from_each_country(connection)
        self.assertEqual(players_from_each_country.shape, (42, 2))
        countries = players_from_each_country.iloc[:, 0].values
        self.assertIn("USA", countries)
        self.assertIn("Canada", countries)
        self.assertIn("France", countries)
        self.assertIn("Ukraine", countries)
        self.assertIn("Portugal", countries)
        number_of_players = players_from_each_country.iloc[:, 1].values
        self.assertEqual(number_of_players.sum(), 502)
    def test_04_count_players_from_usa_or_not(self):
        players_from_usa_or_not = ex.function_count_players_from_usa_or_not(connection)
        self.assertEqual(players_from_usa_or_not.shape, (2, 2))
        from_usa_or_not = players_from_usa_or_not.iloc[:, 0].values
        self.assertEqual(np.unique(from_usa_or_not).size, 2)
        number_of_players = players_from_usa_or_not.iloc[:, 1].values
        self.assertEqual(number_of_players.sum(), 502)
    def test_05_count_players_for_each_position(self):
        players_for_each_position = ex.function_count_players_for_each_position(connection)
        self.assertEqual(players_for_each_position.shape, (7, 2))
        positions = players_for_each_position.iloc[:, 0].values
        self.assertIn("G", positions)
        self.assertIn("F", positions)
        self.assertIn("G-F", positions)
        self.assertIn("F-C", positions)
        self.assertIn("C", positions)
        self.assertIn("C-F", positions)
        self.assertIn("F-G", positions)
        number_of_players = players_for_each_position.iloc[:, 1].values
        self.assertEqual(number_of_players.sum(), 502)
    def test_06_count_players_for_each_new_position(self):
        players_for_each_new_position = ex.function_count_players_for_each_new_position(connection)
        self.assertEqual(players_for_each_new_position.shape, (3, 2))
        positions = players_for_each_new_position.iloc[:, 0].values
        self.assertIn("G", positions)
        self.assertIn("F", positions)
        self.assertIn("C", positions)
        number_of_players = players_for_each_new_position.iloc[:, 1].values
        self.assertEqual(number_of_players.sum(), 502)
    def test_07_calculate_proportion_for_each_position(self):
        proportion_for_each_position = ex.function_calculate_proportion_for_each_position(connection)
        self.assertEqual(proportion_for_each_position.shape, (7, 2))
        positions = proportion_for_each_position.iloc[:, 0].values
        self.assertIn("G", positions)
        self.assertIn("F", positions)
        self.assertIn("G-F", positions)
        self.assertIn("F-C", positions)
        self.assertIn("C", positions)
        self.assertIn("C-F", positions)
        self.assertIn("F-G", positions)
    def test_08_find_roster_of_phx_suns(self):
        roster_of_phx_suns = ex.function_find_roster_of_phx_suns(connection)
        self.assertEqual(roster_of_phx_suns.shape, (17, 4))
        team_names = roster_of_phx_suns.iloc[:, 0].values
        self.assertIn("Phoenix Suns", team_names)
        positions = roster_of_phx_suns.iloc[:, 1].values
        self.assertIn("C", positions)
        self.assertIn("C-F", positions)
        self.assertIn("F", positions)
        self.assertIn("F-C", positions)
        self.assertIn("G", positions)
        last_names = roster_of_phx_suns.iloc[:, 3].values
        self.assertIn("Ayton", last_names)
        self.assertIn("Crowder", last_names)
        self.assertIn("Bridges", last_names)
        self.assertIn("Paul", last_names)
        self.assertIn("Booker", last_names)
    def test_09_find_the_top_ten_scorers(self):
        the_top_ten_scorers = ex.function_find_the_top_ten_scorers(connection)
        self.assertEqual(the_top_ten_scorers.shape, (10, 3))
        first_names = the_top_ten_scorers.iloc[:, 0].values
        self.assertIn("LeBron", first_names)
        self.assertIn("Carmelo", first_names)
        self.assertIn("Kevin", first_names)
        last_names = the_top_ten_scorers.iloc[:, 1].values
        self.assertIn("James", last_names)
        self.assertIn("Anthony", last_names)
        self.assertIn("Durant", last_names)
    def test_10_find_the_top_players(self):
        the_top_players = ex.function_find_the_top_players(connection)
        self.assertEqual(the_top_players.shape, (5, 4))
        first_names = the_top_players.iloc[:, 0].values
        self.assertIn("Andre", first_names)
        self.assertIn("Anthony", first_names)
        self.assertIn("Chris", first_names)
        self.assertIn("LeBron", first_names)
        last_names = the_top_players.iloc[:, 1].values
        self.assertIn("Drummond", last_names)
        self.assertIn("Davis", last_names)
        self.assertIn("Paul", last_names)
        self.assertIn("James", last_names)
        keys = the_top_players.iloc[:, 2].values
        self.assertIn("rpg", keys)
        self.assertIn("bpg", keys)
        self.assertIn("apg", keys)
        self.assertIn("spg", keys)
        self.assertIn("ppg", keys)
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentThree)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))