from flask import Flask
app= Flask(__name__)

def home():
  return "tp4 : bonjour depuis render ! votre app flask est bien en ligne "
if __name__=='__main__':
  app.run()
