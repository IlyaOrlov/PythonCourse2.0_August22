import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
print(f"3 is even: {proxy.is_even(3)}")
print(f"100 is even: {proxy.is_even(100)}")
