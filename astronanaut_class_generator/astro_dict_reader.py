def astro_dict_reader(astro_dict):
    astro_keys = []
    for key in astro_dict.keys():
        astro_keys.append(key)
    astro_keys.sort()
    name_rating_alpha = []
    for key in astro_keys:
        name = astro_dict[key][0]
        rating_num = astro_dict[key][1]
        if rating_num == 0:
            rating = "stub"
        elif rating_num == 1:
            rating = "start"
        elif rating_num == 2:
            rating = "C"
        elif rating_num == 3:
            rating = "B"
        elif rating_num == 4:
            rating = "GA"
        elif rating_num == 5:
            rating = "A"
        elif rating_num == 6:
            rating = "FA"
        astro_tuple = (name, rating)
        name_rating_alpha.append(astro_tuple)
    return name_rating_alpha

def astro_dict_builder(astro_list):
    """Takes a list of astronaut names, the article rating, and weather or not to use the middle name, and returns a dictionary of the last name keys"""
    astro_dict = {}
    for astronaut in astro_list:
        if astronaut[2] == True:
            last = astronaut[0].split()[2]
        else:
            last = astronaut[0].split()[1]
        first = astronaut[0].split()[0]
        astro_key = last + ", " + first
        astro_dict[astro_key] = astronaut[0:2]
    return astro_dict

