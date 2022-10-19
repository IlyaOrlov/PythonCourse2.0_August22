import redis

r = redis.Redis(host='localhost', port=6379, db=0)
p = r.pubsub(ignore_subscribe_messages=True)
p.subscribe('my-chat')
while True:
    msg = p.get_message()
    if msg:
        print("p.get_message(): ", msg)
        break
