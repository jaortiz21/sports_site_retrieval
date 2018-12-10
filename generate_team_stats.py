import nflgame

games = nflgame.games(2016, home='CHI',away='CHI')

for g in games:
    print g
