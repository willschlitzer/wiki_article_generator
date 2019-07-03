politcian_last = "Gouveia"
politician_first = "Tami"
state_senator = False
state = "Massachusetts"
state_abbrev = "MA"
district_no = "14th"
district_name = "Middlesex"
town_list = ["Acton", "Carlisle", "Chelmsford", "Concord"]
democrat = True
term_start = "2019"
successor = ""
predecessor = ""
alma_mater = "[[Mount Holyoke College]]"
spouse = ""
residence = "Acton"
date_accesssed = "May 3, 2019"
male = False
committee_list = [
    "Joint Committee on Children, Families and Persons with Disabilities",
    "Joint Committee on Consumer Protection and Professional Licensure",
    "Joint Committee on Export Development"
    "Joint Committee on Mental Health, Substance Use and Recovery",


]


def get_pronouns(male):
    if male:
        return "he", "his"
    else:
        return "she", "her"


def gen_committee_string(committee_list):
    committee_string = ""
    for i, committee in enumerate(committee_list):
        if i == len(committee_list) - 1 and len(committee_list) > 1:
            committee_string += "and the "
        else:
            committee_string += "the "
        committee_string += committee
        if i < len(committee_list) - 1 and len(committee_list) > 2:
            committee_string += ", "
    return committee_string


def gen_town_string(town_list, state):
    town_string = ""
    for i, town in enumerate(town_list):
        if i == len(town_list) - 1 and len(town_list) > 1:
            town_string += " and "
        town_link = "[[" + town + ", " + state + "|" + town + "]]"
        town_string += town_link
        if i < len(town_list) - 1 and len(town_list) > 2:
            town_string += ", "
    if len(town_list) > 1:
        town_plural = "towns"
    else:
        town_plural = "town"
    return town_string, town_plural


def gen_party(democrat):
    if democrat:
        return "Democrat", "[[Democratic Party (United States)|Democratic Party]]"
    else:
        return "Republican", "[[Republican Party (United States)|Republican Party]]"


def gen_office(state, state_senator):
    if state_senator:
        return (
            state + " Senate",
            "[[" + state + " Senate]]",
            "State Senator",
            "[[State Senator]]",
        )
    else:
        return (
            state + " House of Representatives",
            "[[" + state + " House of Representatives]]",
            "State Representative",
            "[[State Representative]]",
        )


residence_link = "[[" + residence + ", " + state + "|" + residence + "]]"
if alma_mater:
    alma_mater_link = "[[" + alma_mater + "]]"
else:
    alma_mater_link = ""
full_name = politician_first + " " + politcian_last
bold_full_name = "'''" + full_name + "'''"
pronoun, pos_pronoun = get_pronouns(male)
town_string, town_plural = gen_town_string(town_list, state)
party, party_link = gen_party(democrat)

district = district_no + " " + district_name + " District"
district_link = "[[" + district + "]]"
office, office_link, title, title_link = gen_office(state, state_senator)
short_desc = "{{short description|" + state + " politician}}\r"
template = "\r{{" + office + "|state=collapsed}}\r"
committee_string = gen_committee_string(committee_list)
infobox_name = "|name = " + politician_first + " " + politcian_last + "\r"
infobox_office = (
    "|office = " + "Member of the " + office_link + " from the " + district + "\r"
)
infobox_party = "|party = " + party_link + "\r"
infobox_term_start = "|termstart = " + term_start + "\r"
infobox_residence = "|residence = " + residence_link + "\r"
infobox_spouse = "|spouse = " + spouse + "\r"
infobox_alma_mater = "|alma_mater = " + alma_mater_link + "\r"
infobox_successor = "|successor = " + successor + "\r"
infobox_predecessor = "|predecessor = " + predecessor + "\r"

pol_infobox = (
    "{{Politician infobox"
    + infobox_name
    + infobox_office
    + infobox_party
    + infobox_term_start
    + infobox_residence
    + infobox_spouse
    + infobox_alma_mater
    + infobox_predecessor
    + infobox_successor
    + "}}"
)
main_text = (
    bold_full_name
    + " is a "
    + title_link
    + " who represents the "
    + district
    + " in the "
    + office_link
    + ". "
)

main_text += (
    pronoun.title() + " represents the " + town_plural + " of " + town_string + ". "
)
main_text += politcian_last + " serves on " + committee_string + "."


def gen_cat_string(state, party, office, residence, alma_mater):
    cat_string = ""
    cat_list = ["Living people","21st-century politicians", "21st-century American politicians"]
    cat_list.append(state + " politicians")
    cat_list.append(state + " " + party + "s")
    cat_list.append("Members of the " + office)
    if alma_mater:
        cat_list.append(alma_mater + " alumni")
    if residence:
        cat_list.append("People from " + residence + ", " + state)
    for cat in cat_list:
        cat_string += "[[Category:" + cat + "]]\r"
    return cat_string


cat_string = gen_cat_string(state, party, office, residence, alma_mater)


def create_web_citation(
    name="",
    author_last="",
    author_first="",
    title="",
    work="",
    publisher="",
    date="",
    url="",
    date_accessed="",
):
    citation = ""
    citation += "<ref name="
    citation += name
    citation += ">{{cite web\r"
    if author_last:
        citation += "|last = "
        citation += author_last
        citation += "\r"
    if author_first:
        citation += "|first = "
        citation += author_first
        citation += "\r"
    citation += "|title ="
    citation += title
    citation += "\r"
    if work:
        citation += "|work = "
        citation += work
        citation += "\r"
    if publisher:
        citation += "|publisher = "
        citation += publisher
        citation += "\r"
    citation += "|date = "
    citation += date
    citation += "\r"
    citation += " |url = "
    citation += url
    citation += "\r"
    citation += " |accessdate = "
    citation += date_accessed
    citation += "\r"
    citation += "}}</ref>"
    return citation


ref1_name = "about_tami"
ref1_last = ""
ref1_first = ""
ref1_title = "About Tami"
ref1_work = ""
ref1_publisher = "State Representative Tami Gouveia"
ref1_url = "https://www.tamigouveia.com/about-tami"
ref1_date = "2018"
ref1_citation = create_web_citation(
    name=ref1_name,
    author_last=ref1_last,
    author_first=ref1_first,
    work=ref1_work,
    publisher=ref1_publisher,
    title=ref1_title,
    url=ref1_url,
    date=ref1_date,
    date_accessed=date_accesssed,
)
# ref1_citation = ''


ref2_name = "gouveia_committees"
ref2_last = ""
ref2_first = ""
ref2_title = "Tami L. Gouveia: Committees"
ref2_work = ""
ref2_publisher = "The Commonwealth of Massachusetts"
ref2_url = "https://malegislature.gov/Legislators/Profile/TLG1/Committees"
ref2_date = "2019"
ref2_citation = create_web_citation(
    name=ref2_name,
    author_last=ref2_last,
    author_first=ref2_first,
    work=ref2_work,
    publisher=ref2_publisher,
    title=ref2_title,
    url=ref2_url,
    date=ref2_date,
    date_accessed=date_accesssed,
)
# ref2_citation = ''


ref3_name = "gouveia_district"
ref3_last = ""
ref3_first = ""
ref3_title = "Tami L. Gouveia: District"
ref3_work = ""
ref3_publisher = "The Commonwealth of Massachusetts"
ref3_url = "https://malegislature.gov/Legislators/Profile/TLG1/District"
ref3_date = "2019"
ref3_citation = create_web_citation(
    name=ref3_name,
    author_last=ref3_last,
    author_first=ref3_first,
    work=ref3_work,
    publisher=ref3_publisher,
    title=ref3_title,
    url=ref3_url,
    date=ref3_date,
    date_accessed=date_accesssed,
)
# ref3_citation = ""

ref4_name = "wicked_local"
ref4_last = "Razzaq"
ref4_first = "Zane"
ref4_title = "In 6th Middlesex, Maria Gouveia becomes first Korean-American in Mass. House"
ref4_work = ""
ref4_publisher = "[[Wicked Local]]"
ref4_url = "https://www.wickedlocal.com/news/20181106/in-6th-middlesex-maria-Gouveia-becomes-first-korean-american-in-mass-house"
ref4_date = "November 7, 2018"
ref4_citation = create_web_citation(
    name=ref4_name,
    author_last=ref4_last,
    author_first=ref4_first,
    work=ref4_work,
    publisher=ref4_publisher,
    title=ref4_title,
    url=ref4_url,
    date=ref4_date,
    date_accessed=date_accesssed,
)
ref4_citation = ""

page_text = short_desc + pol_infobox + main_text
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
page_text += "\r{{DEFAULTSORT: " + politcian_last + ", " + politician_first + "}}\r"
page_text += cat_string
# For Massachusetts use only
page_text += "\r{{Massachusetts-MARepresentative-stub}}"
with open("page.txt", "w") as file:
    file.write(page_text)

talk_text = (
    "{{talkheader|search=yes}}\r{{WikiProject Biography|living=yes|class=stub|auto=yes|listas="
    + politcian_last
    + ", "
    + politician_first
    + "}}\r{{WikiProject United States|class=Stub|importance=Low|"
    + state_abbrev
    + "=Yes|"
    + state_abbrev
    + "-importance=Low}}\r"
    + "{{User:MiszaBot/config | algo = old(30d) | archive = {{SUBST:FULLPAGENAME}}/Archive %(counter)d | counter = 1 | maxarchivesize = 150K | archiveheader = {{Automatic archive navigator}} | minthreadstoarchive = 1 | minthreadsleft = 4 }}"
)
with open("talk.txt", "w") as file:
file.write(talk_text)