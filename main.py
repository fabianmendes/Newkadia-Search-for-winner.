import  requests 
from bs4 import BeautifulSoup

class Person():
	def __init__(self, name, location, mail):
		self.name = name
		self.city = location
		self.email= mail
		self.days = []
	
	#def setDate(day):
	#	self.days.append(day)

#word = input("Enter a word: ")#take use input and store
#YOUR_NAME = ...and maybe their email! Probably to invite them to Projectboard
r = requests.get("https://www.newkadia.com/?Comic_pag=Comic-Books-Collecting-Ideas")
#	Line 4: you ente any website you want to scrape. So up there i have Merriam-Webster site and ".format(word)" is basically telling programm to search the link and at the add word variable.
#	{} mean that where we are going to paste our word variable

soup = BeautifulSoup(r.content, "html.parser")
#storing bs4 into soup and telling what to do.
#"html.parser tells which parser we are using..."
web  = soup.find("span", attrs={"style":"line-height: 120%; font-size:11pt; "})
mean = web.text
# thanks to "snippsat" extracted from, https://python-forum.io/Thread-Read-input-file-and-print-hyperlinks?pid=3312#pid3312
"""
	#soup, where bs4 is saved
	#"span" tell which section in html to look for...you did have body, div, etc...instead of span
	#attrs....being more specific to where to look for
	#"class":"dtText"...tells program to go inside span tag and find class with name dtText
	#you can find class, span, div and pther info in html. by highlighting the text...then right-mouse click and then click inspect
	#.text is just going to print text without html tags..."""

def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0]
	# credits to Greeksforgeeks
	# extracted from "https://www.geeksforgeeks.org/python-replace-substring-in-list-of-strings/"

winners = mean.split('----@----.com')
del winners[-1] # it deletes the note at the end of the list.
for i in range(len(winners)):
	winners[i] = winners[i].split("\xa0\xa0\xa0\xa0")
	winners[i][0] = list(winners[i][0].split("\xa0"))

	if len(winners[i][0]) % 2 != 0:
		coma = True

	for j in range(int(len(winners[i][0])/2)):
		if coma == True and j == 1:
			semicolon = ", "
		else:
			semicolon = " "

		winners[i][0][j] = winners[i][0][j] + semicolon + winners[i][0].pop(j + 1)
		if j == 1 and (len(winners[i][0])) > j + 1:
			lista_aux = list(winners[i][0][j])
			semicolon = lista_aux.pop(winners[i][0][j].index(","))
			aux = ["",]
			for _ in range(len(lista_aux)):
				aux[0] = aux[0] + lista_aux.pop()
				
			
			winners[i][0][j] = reverse(str(aux[0]))
			winners[i][0][j] = winners[i][0][j] + semicolon + " " + winners[i][0].pop(j + 1)			
 
print("The definition of is: " + mean)
print(type(mean))
print(winners)
#print mean....it will print any word definition that is stored in word variable.

winners_of_date= []
for w in range(len(winners)):
	who_is= winners[w][0][0]
	where = winners[w][0][1]
	fourl = winners[w][1]
	winners_of_date.append(Person(who_is, where, fourl))
	#winners_of_date[w].setDate() # The date of looking.
print("\nName: \t\tPlace: \t\temail:")
for ganador in range(len(winners_of_date)):
	winner_data = winners_of_date[ganador]
	print(winner_data.name + "\t|" + winner_data.city + "\t|" +  winner_data.email)
#print("You can see them in the Newkadia today winners page: " + web.get('href')) 