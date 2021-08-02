CYB333 End of Course Project
"Website monitoring tool"

The point of this project is to develop a python tool to monitor
a website on an Apache2 webserver to ensure it is running as it should.
This is accomplished through utilizing python to access the website 
and perform it's monitoring task of checking the connection.  If a 
request code is received that indicates an interruption in service, 
an email will be sent to the site administrator.  This tool will 
ensure that the site administrator will always be aware if there is
a loss in connectivity to the website. This tool can be automated 
to run as often as you want through either "chron" on Linux 
distrubutions or through "Task Scheduler" in a Windows environment.
