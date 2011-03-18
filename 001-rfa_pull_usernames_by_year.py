#this file pulls the yearly list of successful and unsuccessful rfa's usernames, dates, and vote counts
import re, urllib, time, os, ConfigParser

config = ConfigParser.ConfigParser()
config.read('.wpadmin-scrape.cfg')
data_dir=config.get('DataDirectories','data_dir', 1)

print data_dir

if not os.path.exists(data_dir):
    os.mkdir(data_dir)

if not os.path.exists(data_dir+"successyears"):
    os.mkdir(data_dir+"successyears")

if not os.path.exists(data_dir+"unsuccessyears"):
    os.mkdir(data_dir+"unsuccessyears")

success_outdir = data_dir + "successyears/"
unsuccess_outdir = data_dir + "unsuccessyears/"

print "output to directory" + success_outdir 
print "output to directory" + unsuccess_outdir 

yearcounter = 2004
while yearcounter <= 2011:
    print yearcounter
    #candidate = candidate.replace(" ","_")  # Get rid of spaces if any (otherwise ?action=raw does not work)
    url = 'http://en.wikipedia.org/wiki/Wikipedia:Successful_requests_for_adminship/%s?action=raw' % str(yearcounter)
    print url
    try: infileTextb = urllib.urlopen(url).read()
    except: print "Error S year " + str(yearcounter)
    infileText = str(infileTextb)
    print infileText 
    outfile = open("%s%s.txt" % (success_outdir, str(yearcounter)),'w')
    outfile.write(infileText)
    outfile.close()

    url = 'http://en.wikipedia.org/wiki/Wikipedia:Unsuccessful_adminship_candidacies_(Chronological)/%s?action=raw' % str(yearcounter)
    print url
    try: infileTextb = urllib.urlopen(url).read()
    except: print "Error U year " + str(yearcounter)
    infileText = str(infileTextb)
    print infileText 
    outfile = open("%s%s.txt" % (unsuccess_outdir, str(yearcounter)),'w')
    outfile.write(infileText)
    outfile.close()
    
    yearcounter += 1
    #if counter % 100 == 0: print "(%d/%d)" % (counter, len(candidates))
    time.sleep(1) # Give the server a little break

print "Complete"



