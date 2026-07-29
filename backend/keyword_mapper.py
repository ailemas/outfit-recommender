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

import re


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
    "olive":            {"baseColour_Olive": 1},
    "orange":           {"baseColour_Orange": 1},
    "peach":            {"baseColour_Peach": 1},
    "pink":             {"baseColour_Pink": 1},
    "purple":           {"baseColour_Purple": 1},
    "red":              {"baseColour_Red": 1},
    "rose":             {"baseColour_Rose": 1},
    "rust":             {"baseColour_Rust": 1},
    "sea green":        {"baseColour_Sea Green": 1},
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
    "trousers":             {"subCategory_Bottomwear": 1},
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
    "saree":                {"subCategory_Saree": 1},
    "sari":                 {"subCategory_Saree": 1},
    "scarves":              {"subCategory_Scarves": 1},
    "scarf":                {"subCategory_Scarves": 1},
    "shoes":                {"subCategory_Shoes": 1},
    "footwear":             {"subCategory_Shoes": 1},
    "skin care":            {"subCategory_Skin Care": 1},
    "skincare":             {"subCategory_Skin Care": 1},
    "socks":                {"subCategory_Socks": 1},
    "stoles":               {"subCategory_Stoles": 1},
    "stole":                {"subCategory_Stoles": 1},
    "ties":                 {"subCategory_Ties": 1},
    "tie":                  {"subCategory_Ties": 1},
    "topwear":              {"subCategory_Topwear": 1},
    "top":                  {"subCategory_Topwear": 1},
    "umbrellas":            {"subCategory_Umbrellas": 1},
    "umbrella":             {"subCategory_Umbrellas": 1},
    "wallets":              {"subCategory_Wallets": 1},
    "wallet":               {"subCategory_Wallets": 1},
    "watches":              {"subCategory_Watches": 1},
    "watch":                {"subCategory_Watches": 1},
    "wristbands":           {"subCategory_Wristbands": 1},
    
    # article types
    "tshirt":               {"subCategory_Topwear": 1, "articleType_Tshirts": 1},
    "tshirts":              {"subCategory_Topwear": 1, "articleType_Tshirts": 1},
    "shirt":                {"subCategory_Topwear": 1, "articleType_Shirts": 1},
    "shirts":               {"subCategory_Topwear": 1, "articleType_Shirts": 1},
    "tops":                 {"subCategory_Topwear": 1, "articleType_Tops": 1},
    "tunics":               {"articleType_Tunics": 1},
    "tunic":                {"articleType_Tunics": 1},
    "sweater":              {"articleType_Sweaters": 1},
    "sweaters":             {"articleType_Sweaters": 1},
    "sweatshirt":           {"articleType_Sweatshirts": 1},
    "sweatshirts":          {"articleType_Sweatshirts": 1},
    "hoodie":               {"articleType_Sweatshirts": 1},
    "hoodies":              {"articleType_Sweatshirts": 1},
    "jacket":               {"articleType_Jackets": 1},
    "jackets":              {"articleType_Jackets": 1},
    "blazer":               {"articleType_Blazers": 1},
    "blazers":              {"articleType_Blazers": 1},
    "waistcoat":            {"articleType_Waistcoat": 1},
    "shrug":                {"articleType_Shrug": 1},
    "nehru jacket":         {"articleType_Nehru Jackets": 1},
    "rain jacket":          {"articleType_Rain Jacket": 1},
 
    "jeans":                {"subCategory_Bottomwear": 1, "articleType_Jeans": 1},
    "jeggings":             {"articleType_Jeggings": 1},
    "leggings":             {"articleType_Leggings": 1},
    "shorts":               {"subCategory_Bottomwear": 1, "articleType_Shorts": 1},
    "skirt":                {"subCategory_Bottomwear": 1, "articleType_Skirts": 1},
    "skirts":               {"subCategory_Bottomwear": 1, "articleType_Skirts": 1},
    "capris":               {"articleType_Capris": 1},
    "trackpants":           {"articleType_Track Pants": 1},
    "track pants":          {"articleType_Track Pants": 1},
    "tracksuit":            {"articleType_Tracksuits": 1},
    "tracksuits":           {"articleType_Tracksuits": 1},
    "tights":               {"articleType_Tights": 1},
    "jumpsuit":             {"articleType_Jumpsuit": 1},
    "rompers":              {"articleType_Rompers": 1},
 
    "sneakers":             {"subCategory_Shoes": 1, "articleType_Casual Shoes": 1},
    "casual shoes":         {"subCategory_Shoes": 1, "articleType_Casual Shoes": 1},
    "formal shoes":         {"subCategory_Shoes": 1, "articleType_Formal Shoes": 1},
    "sports shoes":         {"subCategory_Shoes": 1, "articleType_Sports Shoes": 1},
    "running shoes":        {"subCategory_Shoes": 1, "articleType_Sports Shoes": 1},
    "heels":                {"subCategory_Shoes": 1, "articleType_Heels": 1},
    "flats":                {"subCategory_Shoes": 1, "articleType_Flats": 1},
    "sandals":              {"subCategory_Sandal": 1, "articleType_Sandals": 1},
    "sports sandals":       {"subCategory_Sandal": 1, "articleType_Sports Sandals": 1},
    "flip flop":            {"subCategory_Flip Flops": 1, "articleType_Flip Flops": 1},
    "booties":              {"articleType_Booties": 1},
 
    "backpack":             {"subCategory_Bags": 1, "articleType_Backpacks": 1},
    "backpacks":            {"subCategory_Bags": 1, "articleType_Backpacks": 1},
    "handbags":             {"subCategory_Bags": 1, "articleType_Handbags": 1},
    "clutch":               {"subCategory_Bags": 1, "articleType_Clutches": 1},
    "clutches":             {"subCategory_Bags": 1, "articleType_Clutches": 1},
    "duffel bag":           {"subCategory_Bags": 1, "articleType_Duffel Bag": 1},
    "laptop bag":           {"subCategory_Bags": 1, "articleType_Laptop Bag": 1},
    "messenger bag":        {"subCategory_Bags": 1, "articleType_Messenger Bag": 1},
    "trolley bag":          {"subCategory_Bags": 1, "articleType_Trolley Bag": 1},
    "rucksack":             {"subCategory_Bags": 1, "articleType_Rucksacks": 1},
 
    "kurta":                {"articleType_Kurtas": 1},
    "kurtas":               {"articleType_Kurtas": 1},
    "kurti":                {"articleType_Kurtis": 1},
    "kurta set":            {"articleType_Kurta Sets": 1},
    "saree dress":          {"subCategory_Saree": 1, "articleType_Sarees": 1},
    "sarees":               {"subCategory_Saree": 1, "articleType_Sarees": 1},
    "lehenga":              {"articleType_Lehenga Choli": 1},
    "salwar":               {"articleType_Salwar": 1},
    "churidar":             {"articleType_Churidar": 1},
    "dupatta":              {"articleType_Dupatta": 1},
    "suit":                 {"articleType_Suits": 1},
    "suits":                {"articleType_Suits": 1},
 
    "hat":                  {"subCategory_Headwear": 1, "articleType_Hat": 1},
    "caps":                 {"subCategory_Headwear": 1, "articleType_Caps": 1},
    "headband":             {"articleType_Headband": 1},
    "necklace":             {"articleType_Necklace and Chains": 1},
    "earrings":             {"articleType_Earrings": 1},
    "bracelet":             {"articleType_Bracelet": 1},
    "bangle":               {"articleType_Bangle": 1},
    "ring":                 {"articleType_Ring": 1},
    "pendant":              {"articleType_Pendant": 1},
 
    "boxers":               {"articleType_Boxers": 1},
    "briefs":               {"articleType_Briefs": 1},
    "bra":                  {"articleType_Bra": 1},
    "camisole":             {"articleType_Camisoles": 1},
    "camisoles":            {"articleType_Camisoles": 1},
 
    "swimwear":             {"articleType_Swimwear": 1},
    "swimsuit":             {"articleType_Swimwear": 1},
    "night suit":           {"articleType_Night suits": 1},
    "nightdress":           {"articleType_Nightdress": 1},
    "robe":                 {"articleType_Robe": 1},
    "bathrobe":             {"articleType_Bath Robe": 1},
    
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


def extract_keywords(text: str) -> list[str]:
    """Extract known keywords, preserving phrases such as ``smart casual``.

    Keywords are matched from left to right, with the longest match at each
    position winning. Unknown words are skipped.
    """
    words = re.findall(r"[a-z]+(?:'[a-z]+)?", text.lower())
    keyword_words = {
        tuple(re.findall(r"[a-z]+(?:'[a-z]+)?", keyword)): keyword
        for keyword in KEYWORD_MAP
    }
    max_keyword_length = max(len(parts) for parts in keyword_words)

    matches = []
    position = 0
    while position < len(words):
        matched_keyword = None
        matched_length = 0

        for length in range(
            min(max_keyword_length, len(words) - position),
            0,
            -1,
        ):
            candidate = tuple(words[position:position + length])
            if candidate in keyword_words:
                matched_keyword = keyword_words[candidate]
                matched_length = length
                break

        if matched_keyword is None:
            position += 1
            continue

        if matched_keyword not in matches:
            matches.append(matched_keyword)
        position += matched_length

    return matches


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
