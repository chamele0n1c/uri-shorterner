#!/usr/bin/env python

from django.http import HttpRequest
import random
import time
import string
import cgi
import re
import os
import requests
import sys
print "Content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()

url = data.getvalue("url")

cs = data.getvalue("cs")

resp = data.getvalue('g-recaptcha-response')

skey = "" #Your secret Key for reCAPCTHA

user_agent = os.environ["HTTP_USER_AGENT"]

ip = os.environ["REMOTE_ADDR"]

preq = {'secret':skey, 'response':resp, 'remoteip':ip}

parse = requests.post("https://www.google.com/recaptcha/api/siteverify", preq)

response = parse.json()

if response['success'] is False:
    print """
    <html>
    <head>
    <title>Sigh</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
    <script type="text/javascript" src="js/main.js"></script>
    </head>
    <body style="text-align: center;">
    <div id="ngh"></div>
    <div id="main">
    <h1>Either a bot, or cant do a recaptcha </h1>
    <img src="http://vignette2.wikia.nocookie.net/disneycreate/images/7/7a/Sigh.gif/revision/latest?cb=20140105221224" style="align: center;" />
    <h1> I cri ery tiem</h1>
    </div>
    </body>
    </html> """ 
    sys.exit()




# taken from StackOverflow


def ranid(size=3, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

check = re.compile("^https?://")

if check.match(url):
    pass
else:
    print """
    <html>
    <head>
    <title>Really dude?</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
    <script type="text/javascript" src="js/main.js"></script>
    </head>
    <body style="text-align: center;">
    <div id="ngh"></div>
    <div id="main">
    <h1>Not a valid URL. Really? C'mon </h1>
    <img src="https://67.media.tumblr.com/71de193f71eeb27584e82e5ed85c3649/tumblr_nikh3kvuPD1s3h43ko1_r1_500.gif" style="align: center;" />
    <h1> I await your real URL </h1>
    </div>
    </body>
    </html> """ 
    sys.exit()

if cs != "" and cs is not None :
    if len(cs) < 13:
        if not os.path.exists("c/" + cs + ".html"):
 	    cs = cs.translate(None, " . \/%$^&*()~`")
# end

if cs == "" or cs is None or len(cs) > 12:
    cs = ranid()

    

index_content = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Redirecting</title>
<style>
body {
	background: #000;
	color: darkred;

}

#main {
	margin: 50px;
	text-align: center;
	padding: 10px;
	border-radius: 50px;
	border-color: red;
	border-style: solid;
	border-width: 6px;
}
</style>
</head>
<body>

<div id="main">

<h1> Redirecting you to your page... </h1>

</div>

<script type="text/javascript">
function redir() {
    window.location.href = "%s";;
}
setTimeout(redir, 300);
</script>
</body>
</html>
''' % (url,)

filen = "c/" +  cs + ".html"

if os.path.exists(filen):
    os.remove(filen)
text_file = open(filen, "w")
text_file.write(index_content)
text_file.close()

log0 = {ip, user_agent, time.strftime("%a, %d %b %Y %H:%M:%S")}
logloc = "c/" + cs + ".log"
log = ' '.join(log0)
logfile = open(logloc, "wb")
logfile.write(log)
logfile.close()


print '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Page Ready!</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
<script type="text/javascript" src="/js/main.js"></script>
<style>
a:visited {
	color: #fff;
	text-decoration: none;
}
a:link {
	text-decoration: none;
	color: gray;
}
</style>
</head>
<body>
<div id="ngh"> </div>
<div id="main">

<h1>Your URL is <a href="%s">%s</a></h1>

</div>

</body>
</html>
''' % ("https://smfree.cf/c/%s" % cs, "https://smfree.cf/c/%s" % cs) #Use your website here instead






