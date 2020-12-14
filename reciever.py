import amqp
import time

with amqp.Connection('localhost', userid='bobdoom',
    password='Rabb777') as c:
    ch = c.channel()
    def on_message(message):
        print('Received message (delivery tag: {}): {}'.format(message.delivery_tag, message.body))
        ch.basic_ack(message.delivery_tag)
        time.sleep(3)
    ch.basic_consume(queue='test', callback=on_message, )
    while True:
        c.drain_events()