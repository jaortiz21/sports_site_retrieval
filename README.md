# sports_site_retrieval
Project for Information Retrieval and Visualization that focused on scraping the NFL website for statistics on players and teams.

# Project Information #
This project uses [nflgame](https://github.com/BurntSushi/nflgame/blob/master/README.md) API to generate statistics for any number of players and teams starting from the 2010 season up until the 2017 season. In this repository will be several python files used to generate statistics necessary for our project in effectively trying to predict statistics for players in any given season.

# Additional Info #
Code that will not show up in this repository is directly related to being running straight from the terminal. These pieces of code were ran as such because all they did was creat excel files necessary for us to gather all data from every single player in a particular season and place it inside of a single file.<br />
Example:<br />
`nflgame.combine(nflgame.games(2010)).csv('season2010.csv')`<br />
The above example allowed us to generate the stats for every player in the 2010 season, and was performed for every season through the 2016 season.
