import base64
import pythonjsonlogger



msg = "hello"
encoded = base64.b64encode(msg.encode())
print(encoded)