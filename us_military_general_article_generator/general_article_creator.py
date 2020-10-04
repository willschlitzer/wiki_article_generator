import DOR_list_retriever
from web_citation_creator import WebCitation
import page_text_creator
import talk_page_creator

gen_last = "Gouveia"
gen_first = "Tami"
gen_full_name = gen_first + " " + gen_last
gen_image = ""
service = " United States Air Force"
rank = 9
rank_info = Rank(rank=rank)
service_years = "2019"
successor = ""
predecessor = ""
current_command = ""
commands_held = ""
date_accesssed = "May 3, 2019"
alma_mater = "United States Air Force Academy"
# alma_mater = "United States Air Force Academy"
male = False


def gen_cat_string(alma_mater):
    cat_string = ""
    cat_list = [
        "Living people",
        "United States Air Force generals",
    ]
    if alma_mater:
        cat_list.append(alma_mater + " alumni")
    for cat in cat_list:
        cat_string += "[[Category:" + cat + "]]\n"
    return cat_string


cat_string = gen_cat_string(alma_mater)


page_text += "\n==References==\n{{reflist}}"
# page_text += template
page_text == "\n{{authority control}}"
page_text += "\n{{DEFAULTSORT: " + gen_last + ", " + gen_first + "}}\n"
page_text += cat_string
with open("page.txt", "w") as file:
    file.write(page_text)
