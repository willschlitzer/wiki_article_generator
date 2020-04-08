# key
# 0 stub
# 1 start
# 2 c
# 3 b
# 4 GA
# 5 A
# 6 FA

from astro_dict_reader import astro_dict_reader, astro_dict_builder

astronaut_class = str(16)
image_name = "Nasa astronaut class of 1996.jpg"

astro_list = [
    ["Duane G. Carey", 1, True],
    ["Stephen Frick",1, False],
    ["Charles O. Hobaugh",1, True],
    ["James M. Kelly (astronaut)|James M. Kelly", 1, True],
    ["Mark Kelly", 4, False],
    ["Scott Kelly (astronaut)|Scott Kelly", 4, False],
    ["Paul Lockhart", 0, False],
    ["Christopher Loria", 2, False],
    ["William C. McCool", 1, True],
    ["Mark L. Polansky", 1, True],
    ["David M. Brown", 1, True],
    ["Daniel C. Burbank",1, True],
    ["Yvonne Cagle", 1, False],
    ["Fernando Caldeiro", 0, False],
    ["Charles Camarda", 1, False],
    ["Laurel Clark", 2, False],
    ["Michael Fincke|E. Michael Fincke", 1, False],
    ["Patrick G. Forrester", 1, True],
    ["John Herrington", 1, False],
    ["Joan Higginbotham", 2, False],
    ["Sandra Magnus", 1, False],
    ["Mike Massimino", 1, False],
    ["Richard Mastracchio",1, False],
    ["Lee Morin", 1, False],
    ["Lisa Nowak", 3, False],
    ["Donald Pettit", 1, False],
    ["John L. Phillips", 1, True],
    ["Paul W. Richards", 1, True],
    ["Piers Seller",1, False],
    ["Heidemarie Stefanyshyn-Piper", 2, False],
    ["Daniel M. Tani", 2, True],
    ["Rex J. Walheim", 1, True],
    ["Peggy Whitson", 2, False],
    ["Jeffrey Williams (astronaut)|Jeffrey Williams", 1, False],
    ["Stephanie Wilson", 1, False],
    ["Pedro Duque", 1, False],
    ["Christer Fuglesang", 2, False],
    ["Umberto Guidoni", 1, False],
    ["Steve MacLean (astronaut)|Steve MacLean", 1, False],
    ["Mamoru Mohri", 0, False],
    ["Soichi Noguchi", 1, False],
    ["Julie Payette", 2, False],
    ["Philippe Perrin", 1, False],
    ["Gerhard Thiele", 0, False]
]

if __name__ == "__main__":
    astro_dict = astro_dict_builder(astro_list)
    my_list = astro_dict_reader(astro_dict)
    print(my_list)
