from web_citation_creator import WebCitation

gen_last = "Gouveia"
gen_first = "Tami"
service = " United States Air Force"
rank = 9
years_of_service = "2019"
successor = ""
predecessor = ""
current_command = ""
commands_held = ""
date_accesssed = "May 3, 2019"
alma_mater = "United States Air Force Academy"
#alma_mater = "United States Air Force Academy"





def gen_cat_string(state, party, office, residence, alma_mater):
    cat_string = ""
    cat_list = ["Living people","United States Air Force generals",]
    if alma_mater:
        cat_list.append(alma_mater + " alumni")
    if residence:
        cat_list.append("People from " + residence + ", " + state)
    for cat in cat_list:
        cat_string += "[[Category:" + cat + "]]\r"
    return cat_string


cat_string = gen_cat_string(state, party, office, residence, alma_mater)


page_text = short_desc + gen_infobox + main_text
if ref1_citation:
    page_text += ref1_citation
if ref2_citation:
    page_text += ref2_citation
if ref3_citation:
    page_text += ref3_citation
if ref4_citation:
    page_text += ref4_citation

page_text += "\r==References==\r{{reflist}}"
page_text += template
page_text += "\r{{DEFAULTSORT: " + politcian_last + ", " + gen_first + "}}\r"
page_text += cat_string
# For Massachusetts use only
page_text += "\r{{Massachusetts-MARepresentative-stub}}"
with open("page.txt", "w") as file:
    file.write(page_text)

talk_text = (
    "{{talkheader|search=yes}}\r{{WikiProject Biography|living=yes|class=stub|auto=yes|listas="
    + politcian_last
    + ", "
    + gen_first
    + "}}\r{{WikiProject United States|class=Stub|importance=Low|"
    + state_abbrev
    + "=Yes|"
    + state_abbrev
    + "-importance=Low}}\r"
    + "{{User:MiszaBot/config | algo = old(30d) | archive = {{SUBST:FULLPAGENAME}}/Archive %(counter)d | counter = 1 | maxarchivesize = 150K | archiveheader = {{Automatic archive navigator}} | minthreadstoarchive = 1 | minthreadsleft = 4 }}"
)
with open("talk.txt", "w") as file:
file.write(talk_text)