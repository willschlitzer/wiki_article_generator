def template_return(template_start):
    file = "DOR_list.txt"
    with open(file, "r") as f:
        raw_list = f.read().split("\n")
    date_list = remove_ranks(raw_list)
    #return date_list
    template = template_start
    for date in date_list:
        template += "|"
        template += date
    template += "}}"
    return template


def remove_ranks(raw_list):
    ranks = [
        "Second Lieutenant ",
        "First Lieutenant ",
        "Captain ",
        "Major ",
        "Lieutenant Colonel ",
        "Colonel ",
        "Brigadier General ",
        "Major General ",
        "Lieutenant General ",
        "General ",
    ]
    date_list = []
    for i, date_rank in enumerate(raw_list):
        date_list.append(date_rank.replace(ranks[i], ""))
    return date_list


if __name__ == "__main__":
    main()
