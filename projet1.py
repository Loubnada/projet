from flask import Flask
app= Flask(_name_)

def home():
  return "tp4 : bonjour depuis render ! votre app flask est bien en ligne "
if _name_=='_main_':
  app.run()
