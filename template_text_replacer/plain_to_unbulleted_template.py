import re

pretext = "{{Unbulleted list|"
posttext = "}}"

text = """[[Eileen Collins|Eileen M. Collins]]<br/>[[Jeffrey Ashby|Jeffrey S. Ashby]]<br/>[[Michel Tognini]]<br/>[[Steven Hawley|Steven A. Hawley]]<br/>[[Catherine Coleman|Catherine G. Coleman]]"""

#print(text[-3:])
new_text = text.replace("<br />", "<br/>").replace("<br>", "<br/>")
wiki_names = new_text.split("<br/>")
name_string = "|".join(wiki_names)
final_string = pretext + name_string + posttext
if (text[:3] == "[[[") or (text[0:2] != "[[") or (text[-3:] == "]]]") or (text[-2:] != "]]"):
    print("Check punctuation at the beginning/end")
else:
    print(final_string)
    print()
    print("modifying crew list to use unbulleted list template; standardizing spaceflight articles for HTML list elements")

##
#or (text[-3:] == "]]]") or (text[-2:] != "]]")