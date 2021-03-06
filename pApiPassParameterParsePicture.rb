require 'gmail'
#exit if defined?(Ocra)
#^Ocra is used to make exe's, this allows script to exit infinite loop when checkin dependencies.^

keyValuePairs = File.join(Dir.pwd, 'keyValuePairs.txt') # Keys: Keywords, Values: Commands
loginCreds = File.join(Dir.pwd, 'loginCreds.txt') #Gmail Login credentials

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

def sendEmail(gmailSesh, recipient, bodyText)
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
def searchMessage(gmailSesh, keyword, command, recipient)
    gmailSesh.inbox.emails(gm: "from: #{recipient} in:unread '#{keyword}'").each do |email|
        #puts email.body
        if email.body != nil
            if keyword.include? "()" # if () keyword is found, run custom command.
                email.message.attachments.each do |attachment| # turn every attachment into variable
                    if attachment.filename.end_with? ".txt" # find only the attachment that is a text file.
                        attachmentContent = attachment.read() # read contents (custom argument) from attachment

                        splitOnParen = attachmentContent.split(/\(([^\)]+)\)/)
                        
                        beforeParens = splitOnParen[0].downcase
                        betweenParens = splitOnParen[1]#.downcase

                        puts "#{command} #{beforeParens} #{betweenParens}"
                        command = "#{command} #{betweenParens}"
                    end

                    if attachment.filename.end_with? ".jpg"
                    	print attachment.filename

                    	File.write(File.join(Dir.pwd, "/customScripts/babyHTML/images/feet.jpg"), attachment.body.decoded)
                    end
                end
            end
            email.delete! # delete email so for loop doesn't repeate previous commands
            command = %x(#{command}).chomp
            sendEmail(gmailSesh, recipient, "#{command}") # send command output to recipient using gmail session.
            puts "Found Keyword: #{keyword}" #debug
            puts "Command output: #{command}" #debug
            return true # move on to next keyword
        end
    end
    puts "Keyword not found!"
    return false
end

def searchAndTrigger(gmailSesh, keyValuePairs, loginCreds) # single login session!
    recipient = getCredentials(loginCreds)[2]

    x = Hash[*File.read(keyValuePairs).split(/, |\n/)]
    x.each do |key, value|
        searchMessage(gmailSesh, key, value, recipient) # pass necessary variables to discern what trigger to send/delete
    end
end

x = 0
gmailSesh = loginUsing(loginCreds) # Open single session, then search for all keywords/triggers.

while true
    x += 1
    begin
        searchAndTrigger(gmailSesh, keyValuePairs, loginCreds)
        puts "\n"
    rescue
        puts "Login Failed! Trying again..."
        gmailSesh = loginUsing(loginCreds) # Login session failed previously. Try again.
    #ensure
        #puts "Sleeping... Loop: #{x}\n\n"
        #sleep 5
    end
end
