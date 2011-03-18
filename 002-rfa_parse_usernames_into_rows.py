import re, urllib, time, os, ConfigParser

def parseLine(outfile, filestring,success):
    isRFARow = filestring.find("|{{Rfarow|")
    if isRFARow > -1:
        endpoint = filestring.find("||", 10)
        attemptnum = "1"

        if endpoint == -1: #not the first attempt
            endpoint = filestring.find("|", 10)
            attemptnum = filestring[endpoint+1:endpoint+2]
            attemptdate = filestring[endpoint+3:filestring.find("|",endpoint+3)]
            attemptstring = "_" + attemptnum
        else:
            attemptstring = ""
            attemptdate = filestring[endpoint+2:filestring.find("|",endpoint+2)]

        username = filestring[10:endpoint]
        username_reformat = username.replace(" ","_")  # Get rid of spaces if any
        user_url = username_reformat + attemptstring

        outfile.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (username, username_reformat,user_url, attemptnum, attemptdate,success))

def parseDirectory(yeardirectory, outfile,success):
    yearcounter = 2004
    while yearcounter <= 2011:
        print (yeardirectory + str(yearcounter))
        infile = open("%s%s.txt" % (yeardirectory, yearcounter), "r")
        infiletext = infile.read()
        infileLines = infiletext.splitlines()
        
        for infileLine in infileLines:
            parseLine(outfile, infileLine,success)

        yearcounter += 1 

    infile.close()
    
config = ConfigParser.ConfigParser()
config.read('.wpadmin-scrape.cfg')
data_dir=config.get('DataDirectories','data_dir', 1)

successyear_dir = data_dir + 'successyears/'
unsuccessyear_dir = data_dir + 'unsuccessyears/'


outfile = open(data_dir + 'rfa_candidate_names.txt','w')
outfile.write("%s\t%s\t%s\t%s\t%s\t%s\n" % ("username", "username_reformat","user_url", "attemptnum", "attemptdate","success"))
parseDirectory(successyear_dir, outfile,1)
parseDirectory(unsuccessyear_dir, outfile,0)

outfile.close()
