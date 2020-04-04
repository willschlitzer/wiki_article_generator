from astro_dict_reader import astro_dict_reader
from class1994 import astro_dict

astronaut_class = str(14)
image_name = "1994 NASA Astronaut Group.jpg"
astro_info = ""

astro_data = astro_dict_reader(astro_dict)
print(astro_data)
for astronaut in astro_data:
    astro_string = ""
    astro_string = "\n:{{icon|"
    astro_string += astronaut[1]
    astro_string += "}} [["
    astro_string += astronaut[0]
    astro_string += "]]"
    astro_info += astro_string



template_text = (
    "====NASA Astronaut Group 13====\n{{Good topic box\n|title=NASA Astronaut Group "
    + astronaut_class
    + "\n|lead= {{icon|list}} [[NASA Astronaut Group "
    + astronaut_class
    + "]] |bookname= \n|count=23\n|image="
    + image_name
    + "\n|imagesize=120px\n|column1=" + astro_info + "\n}}"
)

print(template_text)
