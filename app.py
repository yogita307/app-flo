#!C:\Users\malth\AppData\Local\Programs\Python\Python310\python.exe
# Importing the 'cgi' module
from calendar import calendar, month
import datetime
from datetime import date
import cgi

print("Content-Type: text/html")
print('')
print("<html><body style='text-align: center;background: rgba( 242, 206, 218, 0.3 );box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );backdrop-filter: blur( 6.5px );border-radius: 1000px;'>")
print("<br>")
print("<h1 style='text-decoration:underline'> Your Report </h1>")
form = cgi.FieldStorage()


periods = form.getvalue("periods")
print("<br>")
print("<br>")
print("<p>Your periods are " + periods + "</p><br />")


############################################
length = form.getvalue("length")
length = int(length)
if length > 1 and length <= 7:
    print("<p>Your period length is normal</p><br />")
elif length == 1 or length > 7:
    print("<p>Your period is not normal</p><br />")
###################################3##
pp = form.getvalue("pp")
day = pp[8:]
mont = pp[5:7]
year = pp[0:4]


t1 = date.today()
t2 = date(year=int(year), month=int(mont), day=int(day))
t3 = t1 - t2
gap = t3.days
print("<p>A normal menstrual cycle typically lasts between 21 days to 35 days</p><br />")

gap = int(gap)
if gap == 0 or gap == 1:
    print("<p>you have just completed your period")
elif gap < 21 and gap > 1:
    print("<p>Your period has completed a few days back i.e." +
          str(gap) + "days</p><br />")
elif gap > 21 and gap < 35:
    print("<p>You may get your period soon. Do not worry!!</p><br />")
elif gap < 0:
    print("Entered wrong")
# elif gap > 35:
#     print("Your period has completed " + str(gap) +
#           " days ago and you haven't got it yet.")

############################################
birth = form.getvalue("birth")
sym = form.getvalue("sym")

if sym and gap > 35:
    if birth == "Yes":
        print(
            f"<p>Your periods has completed {gap} days ago.<br /> As you are using Birth control pills to get rid of {sym}, You may get period <br />soon or else refer to your Doctor for other solution </p><br /> ")
    else:
        print(
            "<p>As you have " + str(sym) + " Periods  delayed with " + str(gap) + " days. So, please refer to your doctor</p><br /> ")
if sym and gap < 35 and gap > 0:
    print(
        f"<p>As you mentioned that you are having {sym}, Its okay as of now because the gap between your previous period and now is {gap} days</p><br />")

print("</body></html>")
print("<style>")

print("")
#

print("</style>")
