import urllib.request

def getHtml(url):
    sock = urllib.request.urlopen(url)
    htmlSource = sock.read()
    sock.close()
    return htmlSource

#mailto: 
def findEmails(string,match="mailto:"):
    emails = []
    for x in range(len(string)-len(match)-1):
        if string[x:x+len(match)] == match:
            testString = string[x:]
            testString = testString[len(match):testString.find("\"")]
            emails += [testString]
    return emails

def fileWrite(emails,fileName):
    file = open(fileName, "w")
    for x in emails:
        file.write(x)
        file.write("\n")
    file.close()

def main():
    # SAMPLE EMAILS: http://floridapolytechnic.org/staff/salah-eddin/ #http://www.siots.biz/contact
    html = str(getHtml(input("Please enter an URL to take emails from: ")))
    fileName = input("What do you wish the file name to be : ")
    if fileName[-4:] != ".txt":
        fileName +=".txt"
    if html.find("mailto") < 0:
        print("There is no email addresses present on this page")
    else:
        emails = findEmails(html)
    fileWrite(emails,fileName)
        

main() 
    
