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
    
    
    # colours
    
    
    # sub-categories
    
    
    # style vibes (composite mappings)
    "cute":    {"usage_Casual": 1,    "season_Summer": 1},
    
    
}