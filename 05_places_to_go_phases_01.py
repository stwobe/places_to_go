# 05_places_to_go_phases_01.py

'''
PHASES:
	1. INITIAL WEBPAGE - Create the webpage with a list in it
	2. Improve HTML + CSS - make responsive
	3. DJANGO - Convert site to Django
	4. PHOTOS
		Find photos already taken of places
		Organize photos already taken of places
	5. PHOTOS 2 - Add photos to webpages
	6. DYNAMIC - Add dynamic functionality - categories - choose distance - First page will be "Places, Distance"
	7. DYNAMIC 2 - Add other dynamic functionalities - activities, shops etc
'''

# PHASE 1
# Create a list
'''
DISCOVERY:
	Build list..
	Add places to list (in Documents2)..
	Find paper list.. (could not find)

REQUIREMENTS:
	Create a list in Sublime Text
	Create local Git repo
	Create Github repo
	Clone repo from Github to the VPS

SOLUTION:
	Basic HTML file set up with BlueGriffon on LMDE/Laptop - further edits to HTML file to be done in Blue Griffon too
	Created local repo in ~/..../02_places
	Created https://github.com/stwobe/places_to_go
	Pushed code to Github
	Cloned in VPS from Github in ~/p..._01
	Create a softlink to html file - actual file is in ~ - link is in /var/www/

TIMELINE:
	Sunday 16th April 2017
	9:30am - 1:00pm 

	10:00 Create list in Sublime..
	10:30 Create local Git repo..
	12:40 Create Github repo..
	12:50 Push local to remote..
	5:00 Create repo in VPS - https://git-scm.com/book/en/v1/Git-on-the-Server-The-Protocols - search "pull from github to server"
	5:30 Pull from Github to VPS
	8:10 Remove people's names
'''

'''
CODE SNIPPET
#
git remote add origin https://github.com/stwobe/places_to_go.git
git push -u origin master
'''














# PHASE 2
# Add CSS + improve HTML
'''
DISCOVERY:
Using  site on phone - not responsive and it's white - not good

REQUIREMENTS:
Responsive + mobile friendly
Tasteful green colour scheme

SOLUTION:
Get CSS from D Adams page - rsync it from server
Get Bootstrap code from Adams page - rsync it from server
Re-do HTML from scratch - use <ul><li> etc - in Blue Griffon

TIMELINE:
Monday May 8th 2017 - Sunday 14th MAy 2017

















'''
# PHASE 3
# DJANGO - Convert site to Django
'''
REQUIREMENTS:
	Hyperlinked/nested categories - e.g. first page - says "Places"
	Click on Places and you see Cwmbran, newport , Pontypool etc - the top level
	Click on Cwmbran and you see Cwmbran Mountain, canal, Birches etc.
	Click on Birches and you see Forest, Stream, Mine, football
	Click on Stream - takes you to the Stream page

DISCOVERY:

SOLUTION:

TIMELINE:
Saturday 22nd April 2017 til Sunday night 23rd April 2017
'''