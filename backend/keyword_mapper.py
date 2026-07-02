"""
- keyword_mapper.py maps English keywords that users type to the one-hot feature columns made by preprocess.py
- can add more entries
- entries follow the format: {FEATURE_COLUMN}_{Value}
- ex. season_Summer, usage_Casual

- columns verified from dataset using df[col].unique()

- exact usage values: Casual, Ethnic, Formal, Home, Party, Smart Casual, Sports, Travel
- exact season values: Fall, Spring, Summer, Winter
- exact gender values: Boys, Girls, Men, Unisex, Women

"""

KEYWORD_MAP: dict[str, dict[str, float]] = {
    
    # seasons
    "summer":       {"season_Summer": 1},
    "winter":       {"season_Winter": 1},
    "spring":       {"season_Spring": 1},
    "fall":         {"season_Fall": 1},
    "autumn":       {"season_Fall": 1},
    
    # usage/occasion
    "casual":       {"usage_Casual": 1},
    "formal":       {"usage_Formal": 1},
    "work":         {"usage_Formal": 1},
    "office":       {"usage_Formal": 1},
    "sports":       {"usage_Sports": 1},
    "sport":        {"usage_Sports": 1},
    "athletic":     {"usage_Sports": 1},
    "gym":          {"usage_Sports": 1},
    "ethnic":       {"usage_Ethnic": 1},
    "traditional":  {"usage_Ethnic": 1},
    "cultural":     {"usage_Ethnic": 1},
    "party":        {"usage_Party": 1},
    "smart casual": {"usage_Smart Casual": 1},
    "travel":       {"usage_Travel": 1},
    "home":         {"usage_Home": 1},
    "lounge":       {"usage_Home": 1},
    "sleep":        {"usage_Home": 1},
    "sleepwear":    {"usage_Home": 1},
    
    # gender
    "women":        {"gender_Women": 1},
    "woman":        {"gender_Women": 1},
    "female":       {"gender_Women": 1},
    "men":          {"gender_Men": 1},
    "man":          {"gender_Men": 1},
    "male":         {"gender_Men": 1},
    "boys":         {"gender_Boys": 1},
    "boy":          {"gender_Boys": 1},
    "girls":        {"gender_Girls": 1},
    "girl":         {"gender_Girls": 1},
    "unisex":       {"gender_Unisex": 1},
    
    
    # colours
    "black":            {"baseColour_Black": 1},
    "beige":            {"baseColour_Beige": 1},
    "blue":             {"baseColour_Blue": 1},
    "bronze":           {"baseColour_Bronze": 1},
    "brown":            {"baseColour_Brown": 1},
    "burgundy":         {"baseColour_Burgundy": 1},
    "charcoal":         {"baseColour_Charcoal": 1},
    "coffee brown":     {"baseColour_Coffee Brown": 1},
    "coffee":           {"baseColour_Coffee Brown": 1},
    "copper":           {"baseColour_Copper": 1},
    "cream":            {"baseColour_Cream": 1},
    "fluorescent":      {"baseColour_Fluorescent Green": 1},
    "neon green":       {"baseColour_Fluorescent Green": 1},
    "gold":             {"baseColour_Gold": 1},
    "green":            {"baseColour_Green": 1},
    "grey":             {"baseColour_Grey": 1},
    "gray":             {"baseColour_Grey": 1},
    "grey melange":     {"baseColour_Grey Melange": 1},
    "khaki":            {"baseColour_Khaki": 1},
    "lavender":         {"baseColour_Lavender": 1},
    "lime":             {"baseColour_Lime Green": 1},
    "lime green":       {"baseColour_Lime Green": 1},
    "magenta":          {"baseColour_Magenta": 1},
    "maroon":           {"baseColour_Maroon": 1},
    "mauve":            {"baseColour_Mauve": 1},
    "metallic":         {"baseColour_Metallic": 1},
    "multi":            {"baseColour_Multi": 1},
    "multicolour":      {"baseColour_Multi": 1},
    "multicolor":       {"baseColour_Multi": 1},
    "mushroom":         {"baseColour_Mushroom Brown": 1},
    "mustard":          {"baseColour_Mustard": 1},
    "navy":             {"baseColour_Navy Blue": 1},
    "navy blue":        {"baseColour_Navy Blue": 1},
    "nude":             {"baseColour_Nude": 1},
    "off white":        {"baseColour_Off White": 1},
    "olive":            {"baseColour_Olive Green": 1},
    "orange":           {"baseColour_Orange": 1},
    "peach":            {"baseColour_Peach": 1},
    "pink":             {"baseColour_Pink": 1},
    "purple":           {"baseColour_Purple": 1},
    "red":              {"baseColour_Red": 1},
    "rose":             {"baseColour_Rose": 1},
    "rust":             {"baseColour_Rust": 1},
    "Sea green":        {"baseColour_Sea Green": 1},
    "silver":           {"baseColour_Silver": 1},
    "steel":            {"baseColour_Steel": 1},
    "tan":              {"baseColour_Tan": 1},
    "taupe":            {"baseColour_Taupe": 1},
    "teal":             {"baseColour_Teal": 1},
    "turquoise":        {"baseColour_Turquoise Blue": 1},
    "turquoise blue":   {"baseColour_Turquoise Blue": 1},
    "white":            {"baseColour_White": 1},
    "yellow":           {"baseColour_Yellow": 1},

    # sub-categories
    "accessories":          {"subCategory_Accessories": 1},
    "apparel set":          {"subCategory_Apparel Set": 1},
    "set":                  {"subCategory_Apparel Set": 1},
    "bags":                 {"subCategory_Bags": 1},
    "bag":                  {"subCategory_Bags": 1},
    "handbag":              {"subCategory_Bags": 1},
    "bath":                 {"subCategory_Bath and Body": 1},
    "body care":            {"subCategory_Bath and Body": 1},
    "beauty":               {"subCategory_Beauty Accessories": 1},
    "belts":                {"subCategory_Belts": 1},
    "belt":                 {"subCategory_Belts": 1},
    "bottomwear":           {"subCategory_Bottomwear": 1},
    "bottom":               {"subCategory_Bottomwear": 1},
    "pants":                {"subCategory_Bottomwear": 1},
    "jeans":                {"subCategory_Bottomwear": 1},
    "trousers":             {"subCategory_Bottomwear": 1},
    "shorts":               {"subCategory_Bottomwear": 1},
    "skirt":                {"subCategory_Bottomwear": 1},
    "cufflinks":            {"subCategory_Cufflinks": 1},
    "dress":                {"subCategory_Dress": 1},
    "dresses":              {"subCategory_Dress": 1},
    "eyewear":              {"subCategory_Eyewear": 1},
    "sunglasses":           {"subCategory_Eyewear": 1},
    "glasses":              {"subCategory_Eyewear": 1},
    "flip flops":           {"subCategory_Flip Flops": 1},
    "flipflops":            {"subCategory_Flip Flops": 1},
    "slippers":             {"subCategory_Flip Flops": 1},
    "fragrance":            {"subCategory_Fragrance": 1},
    "perfume":              {"subCategory_Perfumes": 1},
    "gloves":               {"subCategory_Gloves": 1},
    "hair":                 {"subCategory_Hair": 1},
    "headwear":             {"subCategory_Headwear": 1},
    "cap":                  {"subCategory_Headwear": 1},
    "hat":                  {"subCategory_Headwear": 1},
    "innerwear":            {"subCategory_Innerwear": 1},
    "underwear":            {"subCategory_Innerwear": 1},
    "jewellery":            {"subCategory_Jewellery": 1},
    "jewelry":              {"subCategory_Jewellery": 1},
    "lips":                 {"subCategory_Lips": 1},
    "lipstick":             {"subCategory_Lips": 1},
    "loungewear":           {"subCategory_Loungewear and Nightwear": 1},
    "nightwear":            {"subCategory_Loungewear and Nightwear": 1},
    "pyjamas":              {"subCategory_Loungewear and Nightwear": 1},
    "makeup":               {"subCategory_Makeup": 1},
    "mufflers":             {"subCategory_Mufflers": 1},
    "muffler":              {"subCategory_Mufflers": 1},
    "nails":                {"subCategory_Nails": 1},
    "nail polish":          {"subCategory_Nails": 1},
    "sandal":               {"subCategory_Sandal": 1},
    "sandals":              {"subCategory_Sandal": 1},
    "saree":                {"subCategory_Saree": 1},
    "sari":                 {"subCategory_Saree": 1},
    "scarves":              {"subCategory_Scarves": 1},
    "scarf":                {"subCategory_Scarves": 1},
    "shoes":                {"subCategory_Shoes": 1},
    "sneakers":             {"subCategory_Shoes": 1},
    "footwear":             {"subCategory_Shoes": 1},
    "skin care":            {"subCategory_Skin Care": 1},
    "skincare":             {"subCategory_Skin Care": 1},
    "socks":                {"subCategory_Socks": 1},
    "stoles":               {"subCategory_Stoles": 1},
    "stole":                {"subCategory_Stoles": 1},
    "ties":                 {"subCategory_Ties": 1},
    "tie":                  {"subCategory_Ties": 1},
    "topwear":              {"subCategory_Topwear": 1},
    "tops":                 {"subCategory_Topwear": 1},
    "top":                  {"subCategory_Topwear": 1},
    "shirt":                {"subCategory_Topwear": 1},
    "tshirt":               {"subCategory_Topwear": 1},
    "umbrellas":            {"subCategory_Umbrellas": 1},
    "umbrella":             {"subCategory_Umbrellas": 1},
    "wallets":              {"subCategory_Wallets": 1},
    "wallet":               {"subCategory_Wallets": 1},
    "watches":              {"subCategory_Watches": 1},
    "watch":                {"subCategory_Watches": 1},
    "wristbands":           {"subCategory_Wristbands": 1},
    
    # style vibes (composite mappings)
    "cute":             {"usage_Casual": 1,       "season_Summer": 1},
    "minimalist":       {"usage_Smart Casual": 1, "baseColour_White": 1},
    "minimalistic":     {"usage_Smart Casual": 1, "baseColour_White": 1},
    "glam":             {"usage_Party": 1,        "baseColour_Gold": 1},
    "chic":             {"usage_Smart Casual": 1},
    "cozy":             {"usage_Home": 1,         "season_Winter": 1},
    "boho":             {"usage_Casual": 1,       "season_Spring": 1},
    "edgy":             {"usage_Casual": 1,       "baseColour_Black": 1},
    "athleisure":       {"usage_Sports": 1,       "season_Summer": 1},
    "preppy":           {"usage_Smart Casual": 1, "season_Summer": 1},
    "streetwear":       {"usage_Casual": 1,       "baseColour_Black": 1},
    "vacation":         {"usage_Travel": 1,       "season_Summer": 1},
    
}

# converts a list of keyword strings into a numeric feature vector aligned with feature_columns
# unknown keywords are ignored (vector value remains 0)
# if no keyword matches, raise ValueError
def keywords_to_vector(keywords: list[str], feature_columns: list[str]) -> list[float]:
    vector: dict[str, float] = {col: 0.0 for col in feature_columns}
    matched_any = False
    
    for kw in keywords:
        key = kw.lower().strip()
        if key in KEYWORD_MAP:
            matched_any = True
            for col, val in KEYWORD_MAP[key].items():
                if col in vector:
                    vector[col] = val

    if not matched_any:
        raise ValueError(f"None of the keywords {keywords!r} were recognized."
                         "Try: summer, casual, formal, women, white, dress, etc.")

    return [vector[col] for col in feature_columns]

