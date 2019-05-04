title = "The Uninhabitable Earth"
author = "[[David Wallace-Wells]]"
genre = "non-fiction"
isbn = "978-0-525-57670-9"
publisher = "[[Tim Duggan Books]]"
publisher_date = "April 16, 2019"
country = "United States"
laguage = "English"
pages = "320"
date_accesssed = 'April 24, 2019'

def create_web_citation(name='', author_last='', author_first='', title='', work='', publisher='', date='', url='', date_accessed=''):
    citation = ''
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



nytimes_name = "nytimes_review"
nytimes_last ="Lanchester"
nytimes_first="John"
nytimes_title = "Two New Books Dramatically Capture the Climate Change Crisis"
nytimes_work = "[[The New York Times Book Review|Book Review]]"
nytimes_publisher = "[[The New York Times]]"
nytimes_url ="https://www.nytimes.com/2019/04/12/books/review/david-wallace-wells-uninhabitable-earth-nathaniel-rich-losing-earth.html"
nytimes_date = "April 12, 2019"
nytimes_citation = create_web_citation(name=nytimes_name, author_last=nytimes_last, author_first=nytimes_first,
                                       work=nytimes_work, publisher=nytimes_publisher, title=nytimes_title,
                                       url=nytimes_url, date=nytimes_date, date_accessed=date_accesssed)
#nytimes_citation = ''


kirkus_name = "kirkus_review"
kirkus_last =""
kirkus_first=""
kirkus_title = title
kirkus_work = ""
kirkus_publisher = "[[Kirkus Review]]"
kirkus_url ="https://www.kirkusreviews.com/book-reviews/david-wallace-wells/the-uninhabitable-earth/"
kirkus_date ="January 13, 2019"
kirkus_citation = create_web_citation(name=kirkus_name, author_last=kirkus_last, author_first=kirkus_first,
                                      work=kirkus_work, publisher=kirkus_publisher, title=kirkus_title,
                                      url=kirkus_url, date=kirkus_date, date_accessed=date_accesssed)
#kirkus_citation = ''


pw_name = "pw_review"
pw_last =""
pw_first=""
pw_title = title
pw_work = ""
pw_publisher = "[[Publishers Weekly]]"
pw_url ="https://www.publishersweekly.com/978-0-8021-4730-1"
pw_date = "January 31, 2019"
pw_citation = create_web_citation(name=pw_name, author_last=pw_last, author_first=pw_first,
                                  work=pw_work, publisher=pw_publisher, title=pw_title,
                                  url=pw_url, date=pw_date, date_accessed=date_accesssed)
pw_citation = ''

misc1_name = "npr_review"
misc1_last ="Frank"
misc1_first="Adam"
misc1_title = "New Climate Books Stress We Are Already Far Down The Road To A Different Earth"
misc1_work = ""
misc1_publisher = "[[National Public Radio]]"
misc1_url ="https://www.npr.org/2019/03/25/706499110/new-climate-books-stress-we-are-already-far-down-the-road-to-a-different-earth"
misc1_date = "March 25, 2019"
misc1_citation = create_web_citation(name=misc1_name, author_last=misc1_last, author_first=misc1_first,
                                  work=misc1_work, publisher=misc1_publisher, title=misc1_title,
                                  url=misc1_url, date=misc1_date, date_accessed=date_accesssed)
#misc1_citation = ''


misc2_name = "nytimes_single_review"
misc2_last ="Szalai"
misc2_first="Jennifer"
misc2_title = "In ‘The Uninhabitable Earth,’ Apocalypse Is Now"
misc2_work = ""
misc2_publisher = "[[The New York Times]]"
misc2_url ="https://www.nytimes.com/2019/03/06/books/review-uninhabitable-earth-life-after-warming-david-wallace-wells.html"
misc2_date = "March 6, 2019"
misc2_citation = create_web_citation(name=misc2_name, author_last=misc2_last, author_first=misc2_first,
                                  work=misc2_work, publisher=misc2_publisher, title=misc2_title,
                                  url=misc2_url, date=misc2_date, date_accessed=date_accesssed)
#misc2_citation = ''

infobox_name = "|name = " + title + "\r"
infobox_author = "|author = " + author + "\r"
infobox_language = "|language = English" + "\r"
infobox_country = "|country = United States" + "\r"
infobox_genre = "|genre = " + genre + "\r"
infobox_publisher = "|publisher = " + publisher + "\r"
infobox_pub_date = "|pub_date = " + publisher_date + "\r"
infobox_pages = "|pages = " + pages + "\r"
infobox_isbn = "|isbn = " + isbn + "\r"

infobox_text = "{{Infobox book \r" + infobox_name + "|image = \r" + infobox_author + infobox_language
infobox_text += infobox_country + infobox_genre + infobox_publisher + infobox_pub_date
infobox_text += infobox_pages + infobox_isbn + "}}"
#print(infobox_text)
main_text = "'''''" + title + "''''' is a " + publisher_date[-4:] + " book by " + author + "."



page_text = infobox_text + main_text
if nytimes_citation:
    page_text += nytimes_citation
if kirkus_citation:
    page_text += kirkus_citation
if pw_citation:
    page_text += pw_citation
if misc1_citation:
    page_text += misc1_citation
if misc2_citation:
    page_text += misc2_citation

final_text = "\r\r==References==\r{{reflist}}"
page_text += final_text
with open('page.txt', 'w') as file:
    file.write(page_text)