import amqp

for i in range(10): 
    with amqp.Connection(
        'localhost', exchange='test_exchange',
        userid='bobdoom',
        password='Rabb777',
        confirm_publish=True) as c:       # , virtual_host='test_vhost'
        ch = c.channel()
        ch.basic_publish(amqp.Message(f'Hello World {i}'), routing_key='test')


# with amqp.Connection('localhost', exchange='test_exchange',
#         userid='bobdoom',
#         password='Rabb777') as c:
#     ch = c.channel()
#     ch.basic_publish(amqp.Message('Hello World'), routing_key='test')


for i in range(10): 
    with amqp.Connection(
        'localhost', exchange='test_exchange',
        userid='bobdoom',
        password='Rabb777',
        confirm_publish=False) as c:       # , virtual_host='test_vhost'
        ch = c.channel()
        ch.basic_publish(amqp.Message(f'World Hello {i}'), routing_key='test_test')
