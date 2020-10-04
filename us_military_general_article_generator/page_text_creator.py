short_desc = "{{short description|American Air Force general}}"

class Rank():
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


def gen_infobox(name, image="", allegiance="USA", branch="air force"):
    info_text = "{{Infobox military person"
    info_text += ("\n|name = " + name)
    return info_text


def get_pronouns(male):
    if male:
        return "he"
    else:
        return "she"

if __name__ == "__main__":
    print(gen_infobox(name="Randall Reed"))

