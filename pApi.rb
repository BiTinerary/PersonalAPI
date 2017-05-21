require 'gmail'

username = 'email@gmail.com'
password = 'password'
targetAddress = 'phonenumber@mymetropcs.com'
messageSubject = 'what to say'

def sendEmail(bodyText, targetAddress, username, password)
  Gmail.connect(username, password) do |gmail|
  
    gmail.deliver do
      to targetAddress
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
end

sendEmail('hiyahiya', targetAddress, username, password)


def deleteMessage(keyword, username, password)
    
    Gmail.connect(username, password) do |gmail|
        gmail.inbox.emails(:unread, gm: keyword).each do |email| 
        puts email.body
        email.read!
        email.delete!
        end
	end
end

deleteMessage('Lolliez', username, password)