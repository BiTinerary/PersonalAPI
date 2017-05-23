require 'gmail'

filename = './loginCreds.txt'
bodyText = 'what to say'
keyword = 'ipman'

# Get credentials from each line of file
# Port this lazy/bad storing of credentials to YAML/Token/API, etc...
def getCredentials(filename)
	credentials = []
	File.readlines(filename).each do |line| # append each line to array
	    credentials << line
	end
	username, password, phoneNumber = credentials # assign variable to each index
	return [username, password, phoneNumber] # return new array
end

# Login using previous credetials. Port this to YAML/Token/OAUTH, etc...
def loginUsing(filename) # login using credentials pulled from credentials file
	arrayCreds = getCredentials(filename)
    gmail = Gmail.connect(arrayCreds[0], arrayCreds[1])
    return gmail
end

# Send email.
# Recipient = email address or email address of phone number.
# Body text = content of message, can uncomment lines below to attach local files, provide subject, etc...
# Filename = pass credentials as argument to previous functions.
def sendEmail(recipient, bodyText, filename)
    gmail = loginUsing(filename) # assign variable to login session/connection passed in previous function.
        gmail.deliver do
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
    puts "Email Sent!\nMessage: '#{bodyText}'\nTo: #{recipient}" #Debug, did message get sent? and what?
end

# delete unread message from inbox, which contains specific keyword/s.
# !!! Dangerous, as this will delete unread emails with the keyword anywhere in the message !!!
# This is something that needs to be fixed, else keywords/trigger word defined in later array...
# must be weird, totally random phrases to avoid deleting important emails. (this would be not ideal technique)
# Otherwise, use disposable email address (that i use for spam)
# Otherwise flag to something else and move to **not** inbox.

# ie: I text my own email, this scans for keywords/commands and then triggers local commands, returns API calls or w/e
# then deletes the email containing the keyword, as to not falsely trigger later on.
def deleteMessage(keyword, filename) 
    gmail = loginUsing(filename) # seperate login session.
        gmail.inbox.emails(:unread, gm: 'from:#{getCredentials[2]} #{keyword}).each do |email| # search 'inbox' for every 'unread' keyword ## Probably doesn't need to search for every instance?
            puts email.body

            if email.body != nil
                email.read! #then mark as read ##this can probably be omitted
                #email.delete! #then delete
                return true
            end
            #inbox = gmail.inbox
            #email.body.parts.each do |part|
            #    puts part.decoded
            #end

        end
    #puts "Deleted unread emails with keyword: #{keyword}"
    return false
end

#while True:
#    if deleteMessage == true:
print deleteMessage(keyword, filename)
#sendEmail(getCredentials(filename)[2], bodyText, filename)

################
#Security Notes#
################

#anyone can email you these key words, do not hard code. Store in dictionary, off script.
#limit triggering to sender address/es. Default personal, allow others/friends? Ask for permission, then add/write to 3rd txt file?
#Do not do crazy things, ie: dead man switch, nuke HDD's computers, etc... or do? Then see how long it takes for the world to kill machine?
