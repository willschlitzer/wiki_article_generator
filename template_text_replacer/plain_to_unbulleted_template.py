import re
import pyperclip
import time

pretext = "{{Unbulleted list|"
posttext = "}}"

#text = """[[John O. Creighton]]<br/>[[John H. Casper]]<br/>[[Pierre J. Thuot]]<br/>[[David C. Hilmers]]<br/>[[Richard M. Mullane]]"""
text = input("Astronauts: ")
#print(text[-3:])
new_text = text.replace("<br />", "<br/>").replace("<br>", "<br/>")
wiki_names = new_text.split("<br/>")
name_string = "|".join(wiki_names)
final_string = pretext + name_string + posttext
if (text[:3] == "[[[") or (text[0:2] != "[[") or (text[-3:] == "]]]") or (text[-2:] != "]]"):
    print("Check punctuation at the beginning/end")
    pyperclip.copy(text)
else:
    print(final_string)
    print()
    about_msg = "modifying crew list to use unbulleted list template; standardizing spaceflight articles for HTML list elements"
    print(about_msg)
    pyperclip.copy(about_msg)
    time.sleep(3)
    pyperclip.copy(final_string)


##
#or (text[-3:] == "]]]") or (text[-2:] != "]]")