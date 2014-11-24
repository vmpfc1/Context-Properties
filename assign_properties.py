import random

"""
This file takes a number of properties and then assigns them to either the context independent (CI) or context dependent (CD) categories.
(Two properties for each condition were taken from Barsalou (1982). These properties are noted below in their respective lists.)
Using these properties, sentences were constructed where the property is central to a given subject word (CI) or peeripheral (CD) to its meaning.
Barsalou (1982) has 15 properties in each condition. Context sentences (3 per property) were then constructed around these properties.
 
Barsalou (1982) conducted a norming study to confirm the assured relations between subject nouns and properties and between predicates and properties.
Nine (instead of three) property sentences are constructed for each property in Smith & Srinivasan (2015). Sentences with the most appropriate relations
are included in the analysis, and less appropriate sentences are thrown away.
"""

# The properties listed in Table 1 (Barsalou, 1982)
ciList = ["has a smell", "can contain money"]
cdList = ["can be walked upon", "where cooking can occur"]

# The 26 remaining properties
props = ["can be colorful", "can be old", "can be tall", "where art can be", "where animals live", "can have feathers", "can be sugary", "can contain water",
	"can fit in a hand", "can be spherical", "can contain books", "can start a fire", "can contain food", "can be money", "can be made from plastic", 
	"can be dangerous", "can be heavy", "can be painful", "can be unhealthy", "where food is eaten", "where people sleep", "where old people are", 
	"can be eaten", "can be expensive", "where children can be", "where people relax"] # add extra properties

shuffled = sorted(props, key=lambda k: random.random())

# Add to lists, which will be written to a text file
int = 0
while int < 13:
	ciList.append(shuffled[int])
	int +=1
while int < 26:
	if int == 26:
		break
	cdList.append(shuffled[int])
	int+=1

# Write everything to a text file
f = open("sentences.txt", 'w')
f.write("CI items: " + "\n")
for item in ciList:
	f.write(item + ", \n")
f.write("\n" + "CD items: " + "\n")
for item in cdList:
	f.write(item + ", \n")
f.close()
