import requests
import json
import pandas as pd

response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")

# if your status code starts '2' it was successful
# and if starts with '4' or '5' there was an error.

# print(response.status_code)

fpl_df = json.loads(response.text)

# print(response.json())


# JASON string Data review
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())


# TEAM DF
fpl_teams_df = pd.DataFrame(fpl_df['teams'])

fpl_teams_df_new = fpl_teams_df[["id", "name",
                                "strength_overall_home", "strength_overall_away"]]

print(fpl_teams_df_new.head())

print(fpl_teams_df.columns)

# # PHASES DF
# fpl_phases_df = pd.DataFrame(fpl_df['phases'])
# print(fpl_phases_df)
#
# print(fpl_phases_df.columns)

# # GAME WEEK DF
# fpl_game_week_df = pd.DataFrame(fpl_df['events'])
# print(fpl_game_week_df.head())
#
# print(fpl_game_week_df.columns)

# # PLAYER TYPE DF
# fpl_player_type_df = pd.DataFrame(fpl_df['element_types'])
# print(fpl_player_type_df.head())
#
# print(fpl_player_type_df.columns)

# PLAYER DF
fpl_player_df = pd.DataFrame(fpl_df['elements'])

print(fpl_player_df.columns)

fpl_player_df_new = fpl_player_df[["id", "team", "first_name", "second_name",
                                   "in_dreamteam", "now_cost", "total_points",
                                   "form", "minutes", "influence", "threat",
                                   "creativity", "ict_index", "status"]]

fpl_player_df_new['ict_index'] = pd.to_numeric(fpl_player_df_new['ict_index'], errors='coerce').fillna(0).astype(int)

fpl_player_df_new = fpl_player_df_new[fpl_player_df_new["ict_index"] > 50]

# Find a better way to combine these 4 statements together as a OR block (see example below)
# df.loc[(df.a != 1) or (df.b < 5)]

fpl_player_df_new = fpl_player_df_new[fpl_player_df_new["total_points"] != 0]

fpl_player_df_new = fpl_player_df_new[fpl_player_df_new["status"] != 'u']

fpl_player_df_new = fpl_player_df_new[fpl_player_df_new["status"] != 'i']

fpl_player_df_new = fpl_player_df_new[fpl_player_df_new["status"] != 'n']


fpl_player_df_new["ROI"] = fpl_player_df_new["now_cost"]/fpl_player_df_new["total_points"]

fpl_player_df_new = fpl_player_df_new[fpl_player_df_new["ROI"] > 1]

# fpl_player_df_new = fpl_player_df_new[fpl_player_df_new["ict_index"] > 0]



print(fpl_player_df_new.head(50))

print(len(fpl_player_df_new))












