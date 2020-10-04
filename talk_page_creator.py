def talk_page(gen_last, gen_first):
    talk_text = (
            "{{talkheader|search=yes}}\r{{WikiProject Biography|living=yes|class=stub|auto=yes|listas="
            + gen_last
            + ", "
            + gen_first
            + "|military-work-group=y|military-priority=}}"
              "\n{{WikiProject Military history|class=stub"
              "\n<!-- B-Class 5-criteria checklist -->"
              "\n|b1 <!-- Referencing and citations --> ="
              "\n|b2 <!-- Coverage and accuracy --> ="
              "\n|b3 <!-- Structure --> ="
              "\n|b4 <!-- Grammar and style --> ="
              "\n|b5 <!-- Supporting materials --> ="
              "\n|Aviation=n|Biography=y|US=y|Cold-War=|Post-Cold-War=}}"
              "\n{{WikiProject United States|class=stub|importance=|USMIL=y}}"
              "\n}}"
            + "\n{{User:MiszaBot/config | algo = old(30d) | archive = {{SUBST:FULLPAGENAME}}/Archive %(counter)d | counter = 1 | maxarchivesize = 150K | archiveheader = {{Automatic archive navigator}} | minthreadstoarchive = 1 | minthreadsleft = 4 }}"
    )
    with open("talk.txt", "w") as file:
        file.write(talk_text)

if __name__ == "__main__":
    main(gen_last="Schlitzer", gen_first="Will")