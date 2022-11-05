import time
import redis

# Создаем подключение
r = redis.Redis(host='localhost', port=6379, db=0)

# Добавляем элемент - пару ключ-значение
r.set('name', 'John')
# Получаем значение по ключу
print("r.get('name'): ", r.get('name'))
# Определяем тип значения по ключу
print("r.type('name'): ", r.type('name'))
# Удаляем элемент по ключу
r.delete('name')
print("r.get('name'): ", r.get('name'))

# set всегда добавляет значение строкового типа
r.set('my_int', 2)
print("r.get('my_int'): ", r.get('my_int'))
print("r.type('my_int'): ", r.type('my_int'))
# Инкрементируем значение по ключу, которое для данной
# операции интерпретируется как 64-битное знаковое целое
print("r.incr('my_int'): ", r.incr('my_int'))
# Проверяем существование значения по ключу
print("r.exists('my_int'): ", r.exists('my_int'))
r.set('temp_value', 'value')
# Задаем время жизни ключа (в секундах), по истечении
# которого он будет автоматически удален с сервера
r.expire('temp_value', 5)
# Узнаем оставшееся время жизни ключа
print("r.ttl('temp_value'): ", r.ttl('temp_value'))
print("r.get('temp_value'): ", r.get('temp_value'))

time.sleep(6)
print("After 6 seconds...")

print("r.ttl('temp_value'): ", r.ttl('temp_value'))
print("r.get('temp_value'): ", r.get('temp_value'))
print("r.exists('temp_value'): ", r.exists('temp_value'))

# hashset - хэшсет
# Добавляем пару ключ-значение в хэшсет user:1
r.hset('user:1', 'name', 'John')
# Добавляем еще одну пару ключ-значение в хэшсет user:1
r.hset('user:1', 'email', 'john@gmail.com')
print("r.hget('user:1', 'name'): ", r.hget('user:1', 'name'))
print("r.hkeys('user:1'): ", r.hkeys('user:1'))
print("r.hgetall('user:1'): ", r.hgetall('user:1'))
# list - список # Добавляем элементы в список
r.rpush('my_list', 'elem1')
r.rpush('my_list', 'elem2')
r.rpush('my_list', 'elem3')
r.rpush('my_list', 'elem4')
print("r.llen('my_list'): ", r.llen('my_list'))
print("r.lindex('my_list', 0): ", r.lindex('my_list', 0))
print("r.lrange('my_list', 1, 3): ", r.lrange('my_list', 1, 3))

# Реализация паттерна издатель-подписчик
p = r.pubsub(ignore_subscribe_messages=True)
p.subscribe('my-chat')
print("p.get_message(): ", p.get_message())
r.publish('my-chat', 'user: Hello!')
while True:
    msg = p.get_message()
    if msg:
        print("p.get_message(): ", msg)
        break
