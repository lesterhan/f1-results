
# F1 Results

## Epic: Post season summary
 At the end of the season, I want to be able to print out a summary that says, for example the 2022 season:

```
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
10. (United Kingdom) Williams-Mercedes: 8 Points
```
### Stories:
#### Assign points based on standings at end of race
At the end of each race, points are given out based on the following rule

| Place| Points |
|-|-|
| 1 | 25|
| 2 | 18 |
| 3 | 15 |
| 4 | 12 |
| 5 | 10 |
| 6 | 8 |
| 7 | 6 |
| 8 | 4 |
| 9 | 2 |
| 10 | 1 |
| 11-20 | 0 |

More: https://en.wikipedia.org/wiki/2022_Formula_One_World_Championship#Scoring_system

#### Support fastest lap
Give 1 point to the driver with the fastest lap, if they are in the top 10. If they are not in the top 10, they get no points.

#### Support sprint qualifying points
At the end of sprint qualifying, points are given out based on the following rule

| Place| Points |
|-|-|
| 1 | 8|
| 2 | 7 |
| 3 | 6 |
| 4 | 5 |
| 5 | 4 |
| 6 | 3 |
| 7 | 2 |
| 8 | 1 |
| 9-20 | 0 |

#### Points total at the end of season
Get points total for all drivers and teams

#### Summarize the top 3 driver's champions
Print out summary for driver's championship

#### Summarize the top 3 constructor's champions
Print out summary for constructor's championship

## Epic: Mid season summary
