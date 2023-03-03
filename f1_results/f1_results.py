from typing import Mapping

from f1_results.fixtures import SEASON_FULL_DATA_2022, PLACE_TO_POINTS_MAPPING, TEAMS_2022


def formula_1_race_results(season_data: Mapping) -> str:
    return 'We are all winners'


def assign_points_for_race(race, driver_dict):
    for i, driver in enumerate(race['result']):
        driver_dict[driver] = get_points_for_finishing_position(i)
    return driver_dict


def get_points_for_finishing_position(finishing_position):
    return PLACE_TO_POINTS_MAPPING.get(finishing_position, 0)


def create_driver_dict(teams):
    dict = {}
    for team in teams:
        for driver in team['drivers']:
            dict[driver['number']] = 0
    return dict


def assign_season_results(season_data):
    races = season_data['race_results']
    driver_dict = create_driver_dict(TEAMS_2022)
    for race in races:
        assign_points_for_race(race, driver_dict)
    return driver_dict


results = formula_1_race_results(SEASON_FULL_DATA_2022)
print(results)
