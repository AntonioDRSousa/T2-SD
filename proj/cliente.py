import xmlrpc.client
import sys
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

print("Teste WebService")
response = proxy.service(input("Mensagem: "))

print(response)
