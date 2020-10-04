class WebCitation():
    def __init__(self, ref_name, title, url, date_accessed, author_last = "", author_first = "", work = "", publisher = "", date = ""):
        self.ref_name = ref_name
        self.title = " |title = " + title
        self.author_last = " |last = " + author_last
        self.author_first = " |first = " + author_first
        self.work = " |work = " + work
        self.publisher = " |publisher = " + publisher
        self.date = " |date = " + date
        self.url = " |url = " + url
        self.date_accessed = " |date_accessed = " + date_accessed
        self.create_citation()

    def create_citation(self):
        cite_info = str(self.title + self.author_last + self.author_first + self.work + self.publisher + self.date + self.url + self.date_accessed)
        self.citation = "<ref name=" + self.ref_name + ">{{cite web" + cite_info.replace("  ", " ") + "}}</ref>"
        self.named_citation = "<ref name=" + self.ref_name + "/>"