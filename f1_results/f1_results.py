from typing import Mapping

from f1_results.fixtures import SEASON_FULL_DATA_2022, PLACE_TO_POINTS_MAPPING


def formula_1_race_results(season_data: Mapping) -> str:
    return 'We are all winners'

def assign_points_for_race(race):
    results = {}
    for i, driver in enumerate(race['result']):
        results[driver] = get_points_for_finishing_position(i)
    return results

def get_points_for_finishing_position(finishing_position):
    return PLACE_TO_POINTS_MAPPING.get(finishing_position, 0)


results = formula_1_race_results(SEASON_FULL_DATA_2022)
print(results)
