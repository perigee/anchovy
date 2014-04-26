# Meteor Notes
[**Meteor**](http://www.meteor.com) is an opensource javascript web app platform based on [Node.js](http://nodejs.org), thanks to its rich third party packages system [Atmoshpere](http://atmospherejs.com), it becomes popular recently. By default, Meteor uses MongoDB as its backend database. 

## Installation

1. Install the Node.js (npm included), download it from [nodejs.org](http://nodejs.org/download/)

2. Install the **Meteorite** (additional packages manager)

	```
	$ sudo -H npm install -g meteorite 
	```

3. Install the meteor

	```
	$ curl https://install.meteor.com | sh
	```

## Preparation 

### Project initialization 
Workflow of a particular web app with Meteor


> figure out what to do.


1. Initialize the project

	```
	$ meteor myproject
	```
	or 
	
	```
	$ mrt myproject
	```
	which will create a directory called _myproject_ and some files
2. Install the packages
3. Launch the site, when it is running, it will dynamcially upate your modifications

	```
	$ cd myproject
	$ meteor
	```
	or you can just deploy your site on Internet ;-D
	
	```
	$ meteor deploy myproject.meteor.com
	```
	and check your site on **http://myproject.meteor.com**
	
4. Publication with **Meteor Up**
	1. Install the Meteor up
	
		```
		$ npm install -g mup
		```	
	
## Achitecture of a web app

### Templates
Template is an essential element in webapp. 
Meteor uses [handlebars](http://handlebarsjs.com/) as its template system. 