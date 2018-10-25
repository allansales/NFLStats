from bs4 import BeautifulSoup
import requests
from dateFormat import monthToNum, dayFormat

base_url = "https://www.pro-football-reference.com"

page = requests.get(base_url+"/boxscores/game-scores.htm")
soup = BeautifulSoup(page.content, 'html.parser')

scores_urls = [url.find("a").get("href") for url in soup.find_all('td', {'data-stat' : "all_games"})]

def date_format(date):

	month, day, year = date.replace(",","").split(" ")
	month = monthToNum(month)
	day = dayFormat(day)

	newdate = year+"-"+month+"-"+day
	return newdate

f = open('scores.csv', 'w')
f.write("week,day_of_week,date,win_team,location,lose_team,pts_win,pts_lose,yards_win,turnovers_win,yards_lose,turnovers_lose"+"\n")
for scores_url in scores_urls:
	game_score_page = requests.get(base_url+scores_url) 
	game_score_page_tree = BeautifulSoup(game_score_page.content, 'html.parser')

	week = [week.get_text() for week in game_score_page_tree.find_all('td', {'data-stat' : "week_num"})]
	day_of_week = [day_of_week.get_text() for day_of_week in game_score_page_tree.find_all('td', {'data-stat' : "game_day_of_week"})]
	date = [date.get_text() for date in game_score_page_tree.find_all('td', {'data-stat' : "game_date"})]
	
	win_team = [win_team.get_text() for win_team in game_score_page_tree.find_all('td', {'data-stat' : "winner"})]
	location = [location.get_text() for location in game_score_page_tree.find_all('td', {'data-stat' : "game_location"})]
	lose_team = [loser.get_text() for loser in game_score_page_tree.find_all('td', {'data-stat' : "loser"})]
	
	pts_win = [pts_win.get_text() for pts_win in game_score_page_tree.find_all('td', {'data-stat' : "pts_win"})]
	pts_lose = [pts_lose.get_text() for pts_lose in game_score_page_tree.find_all('td', {'data-stat' : "pts_lose"})]
	yards_win = [yards_win.get_text() for yards_win in game_score_page_tree.find_all('td', {'data-stat' : "yards_win"})]
	to_win = [to_win.get_text() for to_win in game_score_page_tree.find_all('td', {'data-stat' : "to_win"})]
	yards_lose = [yards_lose.get_text() for yards_lose in game_score_page_tree.find_all('td', {'data-stat' : "yards_lose"})]
	to_lose = [to_lose.get_text() for to_lose in game_score_page_tree.find_all('td', {'data-stat' : "to_lose"})]
	
	for w, dow, d, win, loc, lose, pt_win, pt_lose, y_win, to_w, y_lose, to_l in zip(week, day_of_week, date, win_team, location, lose_team, pts_win, pts_lose, yards_win, to_win, yards_lose, to_lose):
		line = w + "," + dow + "," + date_format(d) + "," + win + "," + loc + "," + lose + "," + pt_win + "," + pt_lose + "," + y_win + "," + to_w + "," + y_lose + "," + to_l + "\n"
		f.write(line)
f.close()