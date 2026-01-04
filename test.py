import base64



msg = "hello"
encoded = base64.b64encode(msg.encode())
print(encoded)