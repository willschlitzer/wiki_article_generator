# key
# 0 stub
# 1 start
# 2 c
# 3 b
# 4 GA
# 5 A
# 6 FA

from astro_dict_reader import astro_dict_reader, astro_dict_builder

astronaut_class = str(14)
image_name = "Nasa-14.jpg"

astro_list = [
    ["Scott J. Horowitz", 1, True],
    ["Daniel T. Barry", 1, True],
    ["Brent W. Jett Jr.", 1, True],
    ["Kevin R. Kregel", 1, True],
    ["Kent Rominger", 3, False],
    ["Charles E. Brady Jr.", 2,True],
    ["Catherine Coleman",2, False],
    ["Michael L. Gernhardt", 1, True],
    ["John M. Grunsfeld",1, True],
    ["Wendy B. Lawrence",1,True],
    ["Jerry M. Linenger",1,True],
    ["Richard M. Linnehan",2,True],
    ["Michael López-Alegría",2,False],
    ["Scott E. Parazynski",1,True],
    ["Winston E. Scott",1,True],
    ["Steven Smith (astronaut)|Steven Smith",2, False],
    ["Joseph R. Tanner", 2, True],
    ["Andy Thomas", 1, False],
    ["Mary Ellen Weber", 1, True],
    ["Marc Garneau", 2, False],
    ["Chris Hadfield", 2, False],
    ["Maurizio Cheli", 0, False],
    ["Jean-François Clervoy", 1, False],
    ["Koichi Wakata", 1, False]
]

if __name__ == "__main__":
    astro_dict = astro_dict_builder(astro_list)
    my_list = astro_dict_reader(astro_dict)
    print(my_list)
