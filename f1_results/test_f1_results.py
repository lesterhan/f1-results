from unittest import TestCase

from f1_results.f1_results import (
    formula_1_race_results,
    assign_points_for_race,
    get_points_for_finishing_position
)
from f1_results.fixtures import SEASON_FULL_DATA_2022, UNITED_STATES_2022


class TestF1Results(TestCase):

    def test_full_summary(self):
        self.assertEqual(
            formula_1_race_results(SEASON_FULL_DATA_2022),
            ("""
            In 2022, after 22 races, the Red Bull driver Max Verstappen won the Formula One World Driver's Championship with 454 points.
            Ferrari driver Charles LeClerc came in second with 308 points. And Red Bull driver Sergio Pérez took home 3rd with 305 points.

            Red Bull won the World Constructor's Championship with a total of 759 from both drivers.
            Ferrari was second with 554 points and Mercedes was third with 515 points.

            Here's a detailed summary of the Driver's Championship:
            1. (Netherlands) Max Verstappen: 454 Points
            2. (Monaco) Charles Leclerc: 308 Points
            3. (Mexico) Sergio Pérez: 305 Points
            4. (United) Kingdom George Russell: 275 Points
            5. (Spain) Carlos Sainz Jr.: 246 Points
            6. (United Kingdom) 🇬🇧 Lewis Hamilton: 240 Points
            7. (United Kingdom) Lando Norris: 122 Points
            8. (France) Esteban Ocon: 92 Points
            9. (Spain) Fernando Alonso: 81 Points
            10. (Finland) Valtteri Bottas: 49 Points
            11. (Australia) Daniel Ricciardo: 37 Points
            12. (Germany) Sebastian Vettel: 37 Points
            13. (Denmark) Kevin Magnussen: 25 Points
            14. (France) Pierre Gasly: 23 Points
            15. (Canada) Lance Stroll: 18 Points
            16. (Germany) Mick Schumacher: 12 Points
            17. (Japan) Yuki Tsunoda: 12 Points
            18. (China) Zhou Guanyu: 6 Points
            19. (Thailand) Alexander Albon: 4 Points
            20. (Canada) Nicholas Latifi: 2 Points
            21. (Netherlands) Nyck de Vries: 2 Points
            22. (Germany) Nico Hülkenberg: 0 Points

            Here's a detailed summary of the Constructor's Championship:
            1. (Austria) Red Bull Racing: 759 Points
            2. (Italy) Ferrari: 554 Points
            3. (Germany) Mercedes: 515 Points
            4. (France) Alpine: 173 Points
            5. (United Kingdom) McLaren-Mercedes: 159 Points
            6. (Switzerland) Alfa Romeo-Ferrari: 55 Points
            7. (United Kingdom) Aston Martin Aramco-Mercedes: 55 Points
            8. (United States) Haas-Ferrari: 37 Points
            9. (Italy) AlphaTauri-RBPT: 35 Points
            10. (United Kingdom) Williams-Mercedes: 8 Points""")
        )


class TestAssignPointsForRace(TestCase):

    def test_assign_points_for_race(self):
       points_for_race = assign_points_for_race(UNITED_STATES_2022)
       self.assertEqual(points_for_race, {})

class TestGetPointsForFinishingPosition(TestCase):

    def test_get_points_for_top_ten(self):
        self.assertEqual(get_points_for_finishing_position(1), 18)

    def test_get_points_for_outside_top_ten(self):
        self.assertEqual(get_points_for_finishing_position(11), 0)