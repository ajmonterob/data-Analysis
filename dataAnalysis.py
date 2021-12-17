import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

basketball_players = pd.read_csv("basketball_players.csv")

#Part1
#1
print("Mean")
print(basketball_players.points.mean())
print("")
print("Median")
print(basketball_players.points.median())

#2
print(basketball_players[["playerID","year","points"]].sort_values("points",ascending=False).head(5))

#3
sns.boxplot(data=basketball_players[["rebounds","points","assists"]])
plt.show()

#4
nba_grouped_year = basketball_players[["points","year"]].groupby("year").median()
print(nba_grouped_year.head())
sns.scatterplot(data = nba_grouped_year, x="year",y="points")
plt.show()


#PART2

#1

basketball_master = pd.read_csv("basketball_master.csv")
eff_player = basketball_players[["playerID","points","fgAttempted","ftAttempted"]].groupby("playerID").sum()
eff_player["pointsperattemp_rate"] = eff_player["points"] / (eff_player["fgAttempted"] + eff_player["ftAttempted"])
eff_player = eff_player[(eff_player.fgAttempted > .9) & (eff_player.fgAttempted > .9)   ] 
print(eff_player[["points","fgAttempted","ftAttempted","pointsperattemp_rate"]].sort_values("points",ascending=False).head(10))



#2

multiplecategory_player = basketball_players[["playerID","points","assists","rebounds"]].groupby("playerID").sum()
multiplecategory_player["assist_plus_rebounds"] = multiplecategory_player["assists"] + multiplecategory_player["rebounds"]
print(multiplecategory_player[["points","assist_plus_rebounds"]].sort_values(["assist_plus_rebounds","points"],ascending=[False,False]).head(10))

#3

three_points_shot = basketball_players[["year","threeAttempted"]].groupby("year").sum()
three_points_shot = three_points_shot[(three_points_shot.threeAttempted > 1960 )  ] 
sns.scatterplot(data = three_points_shot, x="year",y="threeAttempted")
plt.show()



#PART3
#1

basketball_master = pd.read_csv("basketball_master.csv")
basketball_players = pd.read_csv("basketball_players.csv")
goatprev = basketball_players[["playerID","points","assists","steals","blocks"]].groupby("playerID").sum()
basketball_data = pd.merge(goatprev, basketball_master, how="left", left_on="playerID", right_on="bioID")
goat = basketball_data[["firstName","lastName","points","assists","steals","blocks"]]
goat = goat[(goat.steals > 0 )  ]

print(goat[["firstName","lastName","points","assists","steals","blocks"]].sort_values(["points","assists","steals","blocks"],ascending=[False,True,False,False]).head(20))


#2

basketball_master = pd.read_csv("basketball_master.csv")
players = basketball_master[["bioID","birthState","birthCountry"]]

USAplayers = players[players.birthCountry == "USA"]
USAplayers = USAplayers["birthState"].value_counts()
statewithmoreplayers = USAplayers.head(5)
print(statewithmoreplayers)
sns.lineplot(data = statewithmoreplayers)
plt.show()

#3

basketball_teams = pd.read_csv("basketball_teams.csv")
teams = basketball_teams[["lgID","name","homeWon"]].groupby("name").sum()
teams = teams.sort_values(["homeWon"],ascending=[False]).head(5)
print(teams)
sns.scatterplot(data = teams)
plt.show()
