from typing import Mapping

from f1_results.fixtures import SEASON_FULL_DATA_2022


def formula_1_race_results(season_data: Mapping) -> str:
    return 'We are all winners'


results = formula_1_race_results(SEASON_FULL_DATA_2022)
print(results)
