short_desc = "{{short description|American Air Force general}}"


class Rank:
    def __init__(self, rank):
        self.rank = rank
        self.insignia = "[[File:US-O" + str(self.rank) + " insignia.svg|30px]]"
        self.dor_template = "{{USAF DOR O-" + str(self.rank)
        self.get_rank_text(rank=self.rank)

    def get_rank_text(self, rank):
        if rank == 10:
            self.rank_word = "General"
            self.rank_link = "[[General (United States)|General]]"
        elif rank == 9:
            self.rank_word = "Lieutenant General]"
            self.rank_link = "[[Lieutenant general (United States)|Lieutenant General]]"
        elif rank == 8:
            self.rank_word = "Major General"
            self.rank_link = "[[Major general (United States)|Major General]]"
        elif rank == 7:
            self.rank_word = "Brigadier General"
            self.rank_link = "[[Brigadier general (United States)|Brigadier General]]"


def gen_infobox(
    name,
    image="",
    allegiance="USA",
    branch="air force",
    service_years="",
    rank_insignia="",
    rank_link="",
    current_command="",
    commands_held="",
    awards="",
):
    info_text = "{{Infobox military person"
    info_text += "\n|name         =" + name
    info_text += "\n|image        = " + image
    info_text += (
        "\n|birth_date   = \n|birth_place  =\n|death_date   = \n|death_place  = "
    )
    info_text += "\n|allegiance   = {{" + allegiance + "}}"
    info_text += "\n|branch       = {{" + branch + "|" + allegiance + "}}"
    info_text += "\n|serviceyears = " + service_years
    info_text += "\n|rank         = " + rank_insignia + " " + rank_link
    commands = current_command
    for i in commands_held:
        if commands:
            commands += "|"
        commands += i
    info_text += "\n|commands     ={{Unbulleted list|" + commands + "}}"
    info_text += "\n|awards       =" + awards
    info_text += "\n}}"
    return info_text


def get_pronouns(male):
    if male:
        return "he"
    else:
        return "she"


def gen_lead(male, command, rank_link, full_name):
    bold_full_name = "'''" + full_name.title() + "'''"
    lower_rank_link = rank_link.lower()
    pronoun = get_pronouns(male=male)
    lead_text = (
        bold_full_name
        + " is a "
        + lower_rank_link
        + "in the [[United States Air Force]]. "
        + pronoun.title()
        + " is the current commander of the "
        + command
        + "."
    )
    return lead_text


if __name__ == "__main__":
    print(gen_infobox(name="Randall Reed"))
    # print(gen_lead(False, "69 Squad", "Maj Gen", "Schlitz"))
