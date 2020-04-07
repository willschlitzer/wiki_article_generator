# key
# 0 stub
# 1 start
# 2 c
# 3 b
# 4 GA
# 5 A
# 6 FA

from astro_dict_reader import astro_dict_reader, astro_dict_builder

astronaut_class = str(15)
image_name = "NASA Astronaut Group 15.jpg"

astro_list = [
    ["Scott Altman", 1, False],
    ["Jeffrey Ashby", 2, False],
    ["Michael J. Bloomfield", 0, True],
    ["Joe F. Edwards Jr.", 2, True],
    ["Dominic L. Pudwill Gorie", 1, True],
    ["Rick Husband", 1, False],
    ["Steven Lindsey", 1, False],
    ["Pamela Melroy", 1, False],
    ["Susan Kilrain", 2, False],
    ["Frederick W. Sturckow", 1, True],
    ["Michael P. Anderson", 1, True],
    ["Kalpana Chawla", 2, False],
    ["Robert Curbeam", 1, False],
    ["Kathryn P. Hire", 2, True],
    ["Janet L. Kavandi", 1, True],
    ["Ed Lu",1, False],
    ["Carlos I. Noriega", 1, True],
    ["James F. Reilly", 2, True],
    ["Stephen Robinson",1, False],
    ["Jean-Loup Chrétien", 1, False],
    ["Takao Doi", 1, False],
    ["Michel Tognini", 1, False],
    ["Dafydd Williams", 1, False]

]

if __name__ == "__main__":
    astro_dict = astro_dict_builder(astro_list)
    my_list = astro_dict_reader(astro_dict)
    print(my_list)
