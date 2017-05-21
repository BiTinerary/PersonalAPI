require 'gmail'
credentials = []

File.readlines('./loginCreds.txt').each do |line|
    credentials << line
end

username = credentials[0]
password = credentials[1]
phoneNumber = credentials[2]
bodyText = 'what to say'
withKeyword = 'Jfjcbbd'

def sendEmail(bodyText, phoneNumber, username, password)
    Gmail.connect(username, password) do |gmail|
  
        gmail.deliver do
            to phoneNumber
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
    end
    puts 'Email Sent! Message: #{bodyText} To: #{phoneNumber}'
end

sendEmail(bodyText, phoneNumber, username, password)

def deleteMessage(keyword, username, password)
    
    Gmail.connect(username, password) do |gmail|
        gmail.inbox.emails(:unread, gm: keyword).each do |email| 
            #puts email.body
            email.read!
            email.delete!
        end
    end
    puts "deleted unread with keyword: #{keyword}"
end

deleteMessage(withKeyword, username, password)
