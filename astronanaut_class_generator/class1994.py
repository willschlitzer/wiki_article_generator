#key
# 0 stub
# 1 start
# 2 c
# 3 b
# 4 GA
# 5 A
# 6 FA

from astro_dict_reader import astro_dict_reader


astro_dict = {
    "Scott J. Horowitz":1, "Daniel T. Barry": 1
}

if __name__ == "__main__":
    my_list = astro_dict_reader(astro_dict)
    print(my_list)