def astro_dict_reader(astro_dict):
    astro_keys = []
    for key in astro_dict.keys():
        astro_keys.append(key)
    astro_keys.sort()
    name_rating_alpha = []
    for key in astro_keys:
        rating_num = astro_dict[key]
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
        astro_tuple = (key, rating)
        name_rating_alpha.append(astro_tuple)
    return name_rating_alpha