facts_txt = open("facts.txt","r")
lines = facts_txt.readlines()


generated_facts = ""
for line in lines:
    fact_template = open("facts/fact_template.txt","r")

    line_split = line.split("|")
    fact_num = line_split[0]
    fact_title = line_split[1]
    fact_date = line_split[2]
    fact_itself = line_split[3]

    generated_facts += f"<li><a href=\"facts/{fact_num}.html\">fact about {fact_title} - {fact_date}</a></li>"
    
    new_file = open(f"facts/{fact_num}.html", "a")
    with open(f"facts/{fact_num}.html", 'w') as f:
        new_file.write(fact_template.read().format(fact_num, fact_title, fact_itself))
        new_file.close()

with open("index_template.txt", "r") as f:
    index_file = open("index.html", "w")
    index_file.write(f.read().format(generated_facts))