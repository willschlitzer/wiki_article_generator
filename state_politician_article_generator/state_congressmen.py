politcian_last = "Olsen"
politician_first = "Jim"
state_senator = False
state = "Oklahoma"
state_abbrev = "OK"
named_districts = False
district_no = "2"
district_name = ""
town_list = ["Sequoyah County"]
democrat = False
term_start = "2019"
successor = ""
predecessor = "[[John R. Bennett]]"
alma_mater = "State University of New York, Albany"
spouse = ""
residence = ""
date_accesssed = "June 29, 2019"
male = True
official_portrait = True
committee_in_name = False
committee_list = [
    "Administrative Rules",
    "A&B Public Safety",
    "Judiciary",
    "Public Safety",
]


def get_pronouns(male):
    if male:
        return "he", "his"
    else:
        return "she", "her"


def gen_committee_string(committee_list, committee_in_name):
    committee_string = ""
    for i, committee in enumerate(committee_list):
        if i == len(committee_list) - 1 and len(committee_list) > 1:
            committee_string += "and the "
        else:
            committee_string += "the "
        committee_string += committee
        if not committee_in_name:
            committee_string += " Committee"
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


if residence:
    residence_link = "[[" + residence + ", " + state + "|" + residence + "]]"
else:
    residence_link = ""
if alma_mater:
    alma_mater_link = "[[" + alma_mater + "]]"
else:
    alma_mater_link = ""
full_name = politician_first + " " + politcian_last
bold_full_name = "'''" + full_name + "'''"
pronoun, pos_pronoun = get_pronouns(male)
town_string, town_plural = gen_town_string(town_list, state)
party, party_link = gen_party(democrat)


if named_districts:
    district = district_no + " " + district_name + " District"
else:
    district = "District " + district_no
district_link = "[[" + district + "]]"
office, office_link, title, title_link = gen_office(state, state_senator)
short_desc = "{{short description|" + state + " politician}}\r"
template = "\r{{" + office + "|state=collapsed}}\r"
committee_string = gen_committee_string(committee_list, committee_in_name)

if official_portrait:
    file_name = politician_first + "_" + politcian_last + "_official_portrait.jpg"
    file_caption = (
        politician_first
        + " "
        + politcian_last
        + "'s official portrait from the "
        + office
        + "."
    )
    pic_info = "filename\r\r"
    pic_info += file_name
    pic_info += "\r\r"
    pic_info += "caption\r\r"
    pic_info += file_caption
    # following is for Oklahoma congressmen
    pic_info += "author\r\rOklahoma Legislative Service Bureau"
    pic_info += "template\r\r{{PD-OK-LSBPD}}"
    with open("pic_info.txt", "w") as file:
        file.write(pic_info)

infobox_name = "|name = " + politician_first + " " + politcian_last + "\r"
infobox_image = "|image ="
if official_portrait:
    infobox_image += file_name
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
    + infobox_image
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
    cat_list = [
        "Living people",
        "21st-century politicians",
        "21st-century American politicians",
    ]
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


ref1_name = "swtimes"
ref1_last = ""
ref1_first = ""
ref1_title = "Sallisaw businessman files for Oklahoma House seat"
ref1_work = ""
ref1_publisher = "Times Record"
ref1_url = "https://www.swtimes.com/news/20180425/sallisaw-businessman-files-for-oklahoma-house-seat"
ref1_date = "April 25, 2018"
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


ref2_name = "muskogee_politico"
ref2_last = "Faught"
ref2_first = "Jamison"
ref2_title = "Jim Olsen running for State House District 2"
ref2_work = ""
ref2_publisher = "Muskogee Politico"
ref2_url = (
    "https://www.muskogeepolitico.com/2018/04/jim-olsen-running-for-state-house.html"
)
ref2_date = "April 25, 2018"
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


ref3_name = "rep_page"
ref3_last = ""
ref3_first = ""
ref3_title = "Representative Jim Olsen District 2 - Republican"
ref3_work = ""
ref3_publisher = "Oklahoma State Legislature"
ref3_url = "https://www.okhouse.gov/Members/District.aspx?District=2"
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

ref4_name = "laboeuf_bio"
ref4_last = ""
ref4_first = ""
ref4_title = "David Henry Argosky Laboeuf: Biography"
ref4_work = ""
ref4_publisher = "The Commonwealth of Massachusetts"
ref4_url = "https://malegislature.gov/Legislators/Profile/DAL1/Biography"
ref4_date = "2019"
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

ref5_name = "meet_david"
ref5_last = ""
ref5_first = ""
ref5_title = "Meet David"
ref5_work = ""
ref5_publisher = "Laboeuf Democrat for State Rep"
ref5_url = "https://www.davidleboeuf.org/about"
ref5_date = "2019"
ref5_citation = create_web_citation(
    name=ref5_name,
    author_last=ref5_last,
    author_first=ref5_first,
    work=ref5_work,
    publisher=ref5_publisher,
    title=ref5_title,
    url=ref5_url,
    date=ref5_date,
    date_accessed=date_accesssed,
)
ref5_citation = ""

page_text = short_desc + pol_infobox + main_text
if ref1_citation:
    page_text += ref1_citation
if ref2_citation:
    page_text += ref2_citation
if ref3_citation:
    page_text += ref3_citation
if ref4_citation:
    page_text += ref4_citation
if ref5_citation:
    page_text += ref5_citation
page_text += "\r==References==\r{{reflist}}"
page_text += template
page_text += "\r{{DEFAULTSORT: " + politcian_last + ", " + politician_first + "}}\r"
page_text += cat_string
# For Massachusetts use only
# page_text += "\r{{Massachusetts-MARepresentative-stub}}"
with open("page.txt", "w") as file:
    file.write(page_text)

talk_text = (
    "{{talkheader|search=no}}\r{{WikiProject Biography|living=yes|class=stub|auto=yes|listas="
    + politcian_last
    + ", "
    + politician_first
    + "}}\r{{WikiProject United States|class=Stub|importance=Low}}\r"
    # Used only if state has a WikiProject under WP United States
    #    + "}}\r{{WikiProject United States|class=Stub|importance=Low|"
    #    + state_abbrev
    #    + "=Yes|"
    #    + state_abbrev
    #    + "-importance=Low}}\r"
    + "{{User:MiszaBot/config | algo = old(30d) | archive = {{SUBST:FULLPAGENAME}}/Archive %(counter)d | counter = 1 | maxarchivesize = 150K | archiveheader = {{Automatic archive navigator}} | minthreadstoarchive = 1 | minthreadsleft = 4 }}"
)
with open("talk.txt", "w") as file:
    file.write(talk_text)
