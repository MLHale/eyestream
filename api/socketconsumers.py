
def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    message.reply_channel.send({
        "text": message.content['text'],
    })

    i=0
    while (i<50):
        i=i+1
        message.reply_channel.send({
            "text": 'test'+str(i),
        })
