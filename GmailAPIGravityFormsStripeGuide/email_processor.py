"""
@company: Pericror
Description:
    Demo code for https://www.pericror.com/software/using-python-gmail-api-and-gravity-forms-stripe
"""
import gmail_wrapper
import requests
import time

if __name__ == '__main__':
    wrapper = gmail_wrapper.GmailWrapper()
    while True:
        # Ensure our auth credentials are still valid
        wrapper.refresh_credentials()
        
        # Get an unread (unprocessed) email
        unread_msg_id = wrapper.get_unread_message_id()
        if unread_msg_id:
            # Process the email
            msg_data = wrapper.get_message_data(unread_msg_id)
            msg_body = msg_data['body'].split('\n')
            msg_body = [elem.rstrip('\r') for elem in msg_body]
            
            # Check if the email matches the expected format
            if (len(msg_body) >= 2 and "link:" in msg_body[0]
                and "email:" in msg_body[1]):
                link = msg_body[0][len("link:"):]
                email = msg_body[1][len("email:"):]
                print "Processing email! [Link]: {} [Email]: {}".format(
                    link, email)
                    
                # Check Link
                try:
                    resp = requests.get(link)
                except Exception:
                    error_msg = "Error requesting link! Could not check."
                    print error_msg
                    message = wrapper.create_message(email, "Link Results",
                                                     error_msg, error_msg)
                    wrapper.send_message(message)
                    wrapper.mark_as_read(unread_msg_id)
                    continue
                try:
                    resp.raise_for_status()
                    color = "#00FF7F"
                    result = "Passed!"
                except requests.exceptions.HTTPError as e:
                    color = "#FF6347"
                    result = "Failed!"
                    
                # Craft result text/html
                plain = "Link: {}\nResult: {}\nResponse Code: {}\n Reason: " \
                    "{}".format(link, result, resp.status_code, resp.reason)
                html = "Link: {}<br>Result: <span style='background-color:{};'>" \
                    "<b>{}</b></span><br>".format(link, color, result)
                html += "Response Code: <b>{}</b><br>".format(resp.status_code)
                html += "Reason: <b>{}</b>".format(resp.reason)
                
                # Send an email response the contains the original email
                message = wrapper.create_message(email, "Link Results", plain, html)
                wrapper.send_message(message)
                print "Sent results to {}!".format(email)
                
            # Mark the message as read so we don't process it again
            wrapper.mark_as_read(unread_msg_id)
            
        print "Sleeping 5 minutes before checking again..."
        time.sleep(300) # sleep 5 minutes before checking again
