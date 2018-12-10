import nflgame

games = nflgame.games(2016)
players = nflgame.combine_game_stats(games)

print 'Passing Yard Leaders for 2016'

for p in players.passing().sort('passing_yds').limit(5):
    msg = '\t%s %d completions for %d yards, %d touchdowns and %d interceptions'
    print msg % (p, p.passing_cmp, p.passing_yds, p.passing_tds, p.passing_ints)

print 'Rushing Yard Leaders for 2016'

for p in players.rushing().sort('rushing_yds').limit(5):
    msg = '\t%s %d carries for %d yards and %d TDs'
    print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)

print 'Receiving Yard Leaders for 2016'

for p in players.receiving().sort('receiving_yds').limit(5):
    msg = '\t%s with %d receptions for %d receiving yards and %d TDs'
    print msg % (p, p.receiving_rec, p.receiving_yds, p.receiving_tds)
