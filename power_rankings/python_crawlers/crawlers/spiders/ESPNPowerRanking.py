# -*- coding: utf-8 -*-
import scrapy
import re

class ESPNPowerRankingSpider(scrapy.Spider):
    name = 'powerRankingCrawler'

    start_urls = []

    teams = ["nyg","nyj","lar","lac","ari","atl","bal","buf","car","chi","cin","cle","dal","den","det","gb","hou","ind","jax","kc","mia","min","ne","no","oak","phi","pit","sf","sea","tb","ten","wsh"]
    years = ["2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016"]

    BASE_URL = "http://www.espn.com/nfl/team/rankings/_/name/TEAM_NAME/year/SEASON_YEAR"

    for team in teams:
        for year in years:
            team_url = BASE_URL.replace("TEAM_NAME", team)
            team_season_url = team_url.replace("SEASON_YEAR", year)
            start_urls.append(team_season_url)

    def win_loss_tie_of_record(self, record):
        split_record = record.split("-")

        if(len(split_record)==3):
            win, loss, tie = split_record
        else:
            win, loss = split_record
            tie = "0"

        return(win, loss, tie)

    def format_game_week(self, week):
        if("Week" in week):
            week_str, week_number = week.split()
            week_number = int(week_number) - 1
            return week_number
        return(week)

    def parse(self, response):

                weeks = response.xpath("//tr[@class='oddrow' or @class='evenrow']/td[1]/a/text()").extract()
                records = response.xpath("//tr[@class='oddrow' or @class='evenrow']/td[@align='center'][last()-1]/text()").extract()
                ranks = response.xpath("//tr[@class='oddrow' or @class='evenrow']/td[@align='center'][last()]/text()").extract()
                team = response.xpath("//a[@class='sub-brand-title']/b/text()").extract()
                year = response.xpath("//option[@selected='selected']/text()").extract()

                for week, record, rank in zip(weeks, records, ranks):

                    win, loss, tie = self.win_loss_tie_of_record(record)

                    yield{"week": self.format_game_week(week),
                          "record": record,
                          "rank": rank,
                          "team": team,
                          "year": year,
                          "n_wins": win,
                          "n_loses":loss,
                          "n_ties": tie,
                    }