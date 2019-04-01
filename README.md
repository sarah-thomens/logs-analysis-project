# Logs Analysis Project
##### By: Sarah Thomens

## How to Install and Run Project
1. This project should be run using a virtual box, we'll use VirtualBox and Vagrant.
	* To download VirtualBox click [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and install the platform package for your operating system.
	* To download Vagrant, which configures the VM, click [here](https://www.vagrantup.com/downloads.html) and install the version for your operating system.
2. Next configure the Virtual Machine by downloading [this](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) and moving to your preferred directory.
	* Open your terminal and cd into this directory
	* cd into the vagrant directory
	* Start the virtual machine: `vagrant up`
	* Log into your virtual machine: `vagrant ssh`
3. Make sure you have the news database before running this project.
	* This is provided by the Udacity team [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
	* Unzip and move this file to the vagrant directory
	* To load the data, cd into the vagrant directory while your VM is running and use this command: `psql -d news -f newsdata.sql`
2. Make sure you have created all views used by this code to do so use this command: `psql -d news -f createviews.sql` 
3. Run `python loganalysis.py` to run the project.

## Project Description
This program accesses the news database provided by Udacity to answer three questions:
	1. What are the most popular three articles?
	2. Who are the most popular article authors?
	3. On which days did more than 1% of requests lead to errors?

The program uses SQL commands to access the news database and javascript to create the readable output that answers the above three questions.
