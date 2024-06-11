from random import randint

def pick_random_word():
    word_list=["tokyo", "london", "paris", "new york", "sydney", "berlin", "rome", "madrid", "beijing", "moscow", "dubai", "singapore", "hong kong", "los angeles", "chicago", "toronto", "vancouver", "mexico city", "rio de janeiro", "buenos aires", "cape town", "cairo", "istanbul", "bangkok", "seoul", "kuala lumpur", "delhi", "mumbai", "jakarta", "manila", "lima", "bogota", "caracas", "havana", "athens", "vienna", "prague", "budapest", "warsaw", "oslo", "stockholm", "helsinki", "copenhagen", "brussels", "amsterdam", "zurich", "geneva", "barcelona", "lisbon", "santiago"]


    selected_index= randint(0,len(word_list)-1)
    return word_list[selected_index]


