require 'gmail'

keyValuePairs = './keyValuePairs.txt' # Keys: Keywords, Values: Commands
loginCreds = './loginCreds.txt' #Gmail Login credentials

def getCredentials(loginCreds) #Allow this to utilize Oauth2
    credentials = []
    File.readlines(loginCreds).each do |line| # append each line to array
        credentials << line
    end
    username, password, phoneNumber = credentials # assign variable to each index
    return [username, password, phoneNumber] # return new array
end

def loginUsing(loginCreds) # login using credentials pulled from credentials file
    arrayCreds = getCredentials(loginCreds)
    gmailSesh = Gmail.connect(arrayCreds[0], arrayCreds[1])
    return gmailSesh # Create one login session.
end

def sendEmail(recipient, bodyText, gmailSesh)
        gmailSesh.deliver do
            to recipient
            #subject messageSubject

            text_part do
                body bodyText
            end

            html_part do
                content_type 'text/html; charset=UTF-8'
                body bodyText #'<p>Text of <em>html</em> message.</p>''
            end
            #add_file '\path\to\image.png'
        end
    puts "\nEmail Sent!\nMessage: '#{bodyText}'\nTo: #{recipient}" #debug
end

# use passed arguments to continue session, find message and send respective response.
def deleteMessage(keyword, command, gmailSesh, recipient) 
        gmailSesh.inbox.emails(gm: "from: #{recipient} in:unread '#{keyword}'").each do |email|
            #puts email.body

            if email.body != nil
                email.delete! #then delete
                command = %x(#{command}).chomp
                sendEmail(recipient, "#{command}", gmailSesh) #send command output to recipient using gmail session.
                puts "Found Keyword: #{keyword}" #debug
                puts "Issuing command: #{command}" #debug
                return true # move on to next keyword
            end
        end
    puts "keyword not found!"
    return false
end

def searchAndTrigger(keyValuePairs, loginCreds) #single login session!
	gmailSesh = loginUsing(loginCreds) # Open single session, then search for all keywords/triggers.
 	recipient = getCredentials(loginCreds)[2]

    x = Hash[*File.read(keyValuePairs).split(/, |\n/)]
    x.each do |key, value|
    	deleteMessage(key, value, gmailSesh, recipient) # pass necessary variables to discern what trigger to send/delete
    end
end

while true
	searchAndTrigger(keyValuePairs, loginCreds)
	puts "\nSleeping...".chomp
	sleep 5
end
