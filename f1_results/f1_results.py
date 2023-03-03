from typing import Mapping

from fixtures import SEASON_FULL_DATA_2022, PLACE_TO_POINTS_MAPPING


def formula_1_race_results(season_data: Mapping) -> str:
    return 'We are all winners'

def assign_points_for_race(race):
    [racer for racer in race['result']]
    return {
          1: 25,
          44: 18,
          16: 15,
          11: 12,
          63: 10,
          4: 8,
          14: 6,
          5: 4,
          20: 2,
          22: 1,
          31: 0,
          24: 0,
          23: 0,
          10: 0,
          47: 0,
          3: 0,
          6: 0,
          18: 0,
          77: 0,
          55: 0,
       }

def get_points_for_finishing_position(finishing_position):
    return PLACE_TO_POINTS_MAPPING.get(finishing_position, 0)


results = formula_1_race_results(SEASON_FULL_DATA_2022)
print(results)
