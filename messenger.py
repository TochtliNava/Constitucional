import pywhatkit as kit

phone_number = "+523122014135"

def send_message(message):
    kit.sendwhatmsg_instantly(phone_number, message)

send_message("holi")