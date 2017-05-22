require 'gmail'

filename = './loginCreds.txt'
bodyText = 'what to say'
keyword = 'ipman'

def getCredentials(filename)
	credentials = []
	File.readlines(filename).each do |line|
	    credentials << line
	end
	username, password, phoneNumber = credentials
	return [username, password, phoneNumber]
end

def loginUsing(filename)
	arrayCreds = getCredentials(filename)
    gmail = Gmail.connect(arrayCreds[0], arrayCreds[1])
    return gmail
end

def sendEmail(recipient, bodyText, filename)
    gmail = loginUsing(filename)
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
    puts "Email Sent!\nMessage: '#{bodyText}'\nTo: #{recipient}"
end

sendEmail(getCredentials(filename)[2], bodyText, filename)
