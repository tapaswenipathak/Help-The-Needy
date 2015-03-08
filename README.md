# Help-The-Needy

We want to help you so that you can easily help the needy.

This will give you all nearby NGOs with a map, given a address by a user.


## Setup Instructions

* Clone the source

	```
	git clone git@github.com:tapasweni-pathak/Help-The-Needy.git
	```
* Install requirements

	```
	pip install -r /path/to/requirements.txt
	```
* Install Bootstrap

	```
	sudo apt-get update
	sudo apt-get install -y python-software-properties python g++ make
	sudo add-apt-repository ppa:chris-lea/node.js
	sudo apt-get update
	sudo apt-get install nodejs
	sudo npm install bootstrap
	```
* Generate Google Places API Key (You can use our to test things)

	1. Visit the [Google APIs Console](https://code.google.com/apis/console/b/0/?noredirect) and log in with your Google account.

	2. A default project called API Project is created for you when you first log in to the APIs Console. You can use the project, 		or create a new one by clicking the API Project button at the top of the window and selecting Create. Maps API for Business 		customers must use the API project created for them as part of their Places for Business purchase.

	3. Click the Services link in the left-hand navigation panel.

	4. Click the status switch (the on/off button) next to the Places API entry. The switch slides to ON.

	5. Click API Access in the left-hand navigation panel.

	6. Click Create new Server key. Enter one or more server IP addresses if you wish to restrict the servers that can send API requests.

	7. Click Create. Your API key appears under the heading Key for server apps (with IP locking).

* Some More Changes

	In settings.py

	```

	 STATICFILES_DIRS =  (
    			('assets', '/path/to/Help-The-Needy/help_the_needy/static'),
    			)
	```


## To Run

```
cd Help-The-Needy/help_the_needy/

python manage.py runserver
```

**Some Errors?**

Make sure you have db.sqlite file. If you do not have it, run

```
./manage.py syncdb
```

If it asks

```
You just installed Django's auth system, which means you don't have any superusers defined.
Would you like to create one now? (yes/no):
```

Say no. 



## Features
### Currently Implemented

* Enter your address -> get nearby NGOs.
* Click on the see map -> get the map.
* Click on the NGO name -> get more information about the NGO.



### TODO

* Allow user to search for NGO category wise.
* Allow the user to change the nearby radius.
* Login System.
* Profile Page for every user, that shows their helping history.
* NGO page.



## Contributing

* You can send patches for above todos.
* Send us a issue.
* Find some bugs.



## Need some help?

* Contact [Tapasweni Pathak] (https://github.com/tapasweni-pathak)
* Contact [Shaifali Aggarwal] (https://github.com/exploreshaifali)



##### Thanks for creating the following things!

* Django
* Freelancer Bootstrap Theme
* Google Places API
* Django Easy Map
* Python Google Places





This is started when we decided to participate in [this Women Hackathon] ('https://www.hackerearth.com/women-hackathon-2015/').

