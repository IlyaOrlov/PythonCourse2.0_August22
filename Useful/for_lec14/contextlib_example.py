import contextlib


@contextlib.contextmanager
def set_obj_attrs(obj, attrs):
    bkp_attrs = {}
    try:
        for p_name, p_value in attrs.items():
            if hasattr(obj, p_name):
                bkp_attrs[p_name] = getattr(obj, p_name)
                setattr(obj, p_name, p_value)
        yield obj
    finally:
        for p_name, p_value in bkp_attrs.items():
            setattr(obj, p_name, p_value)


class MyConf:
    pass

m = MyConf()
m.server_addr = '192.168.1.1'
m.server_port = 1212

new_conf = {'server_addr': '192.168.1.11', 'server_port': 2121}
with set_obj_attrs(m, new_conf):
    # doing test
    print(m.server_addr)
    print(m.server_port)
print("======================")
print(m.server_addr)  # '192.168.1.1'
print(m.server_port)  # 1212














