import nflgame

games = nflgame.games(2016, week=1)
players = nflgame.combine_game_stats(games)

## Need to work on better format
## formatted stats method is trash
for p in players.passing().sort('passing_yds').limit(5):
    stats = p.formatted_stats().split(',')
    print '%s' % p
    for s in stats:
        print '\t%s' % s
