"""
- keyword_mapper.py maps English keywords that users type to the one-hot feature columns made by preprocess.py
- can add more entries
- entries follow the format: {FEATURE_COLUMN}_{Value}
- ex. season_Summer, usage_Casual

"""

KEYWORD_MAP: dict[str, dict[str, float]] = {
    
    # seasons
    "summer":    {"season_Summer": 1},
    "winter":    {"season_Winter": 1},
    "spring":    {"season_Spring": 1},
    "fall":      {"season_Fall": 1},
    "autumn":    {"season_Fall": 1},
    
    # usage/occasion
    "casual":    {"usage_Casual": 1},
    
    # gender
    "women":     {"gender_Women": 1},
    "woman":     {"gender_Women": 1},
    "female":    {"gender_Women": 1},
    "men":       {"gender_Men": 1},
    "man":       {"gender_Men": 1},
    "male":      {"gender_Men": 1},
    "boys":      {"gender_Boys": 1},
    "boy":       {"gender_Boys": 1},
    "girls":     {"gender_Girls": 1},
    "girl":      {"gender_Girls": 1},
    "unisex":    {"gender_Unisex": 1},
    
    
    # colours
    "black":     {"baseColour_Black": 1},
    
    # sub-categories
    "tops":     {"subCategory_Topwear": 1},
    
    # style vibes (composite mappings)
    "cute":     {"usage_Casual": 1,    "season_Summer": 1},
    
    
}

# converts a list of keyword strings into a numeric feature vector aligned with feature_columns
# unknown keywords are ignored (vector value remains 0)
# if no keyword matches, raise ValueError
def keywords_to_vector(keywords: list[str], feaure_columns: list[str]) -> list[float]:
    # implement
    return

