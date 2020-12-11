import amqp

for i in range(10): 
    with amqp.Connection(
        'localhost', exchange='test_exchange',
        userid='bobdoom',
        password='Rabb777',
        confirm_publish=True) as c:       # , virtual_host='test_vhost'
        ch = c.channel()
        ch.basic_publish(amqp.Message(f'Hello World {i}'), routing_key='test')
