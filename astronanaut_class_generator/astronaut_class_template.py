from astro_dict_reader import astro_dict_reader, astro_dict_builder
from class1994 import astro_list, astronaut_class, image_name


astro_info = ""

astro_dict = astro_dict_builder(astro_list)
astro_data = astro_dict_reader(astro_dict)
print(astro_data)
class_size = len(astro_dict)


def create_astro_string(astronaut):
    astro_string = "\n:{{icon|"
    astro_string += astronaut[1]
    astro_string += "}} [["
    astro_string += astronaut[0]
    astro_string += "]]"
    # astro_info += astro_string
    return astro_string


def column_splitter(astro_data=astro_data, class_size=class_size):
    col_num = 3
    col_size = int(class_size / col_num)
    neg_col_size = -1 * col_size
    if (class_size % col_num) != 0:
        col_size += 1
    astro_info = "\n|column1="
    for astronaut in astro_data[:col_size]:
        astro_info += create_astro_string(astronaut=astronaut)
    astro_info += "\n|column2="
    for astronaut in astro_data[col_size:neg_col_size]:
        astro_info += create_astro_string(astronaut=astronaut)
    astro_info += "\n|column3="
    for astronaut in astro_data[neg_col_size:]:
        astro_info += create_astro_string(astronaut=astronaut)
    return astro_info


astro_info = column_splitter(astro_data=astro_data, class_size=class_size)

template_text = (
    "====NASA Astronaut Group "
    + astronaut_class
    + "====\n{{Good topic box\n|title=NASA Astronaut Group "
    + astronaut_class
    + "\n|lead= {{icon|list}} [[NASA Astronaut Group "
    + astronaut_class
    + "]] |bookname= \n|count="+ str(class_size) + "\n|image="
    + image_name
    + "\n|imagesize=120px"
    + astro_info
    + "\n}}"
)

print(template_text)
