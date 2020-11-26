from bs4 import BeautifulSoup
import requests
import time
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_API_URL = os.getenv("BASE_API_URL")

valueUpdated = False

def sendMesg(msg):
  requests.get("https://api.telegram.org/bot"+TOKEN+"/sendMessage?chat_id=156669906&text="
    +msg
  )

def getValue():
  r = requests.get(BASE_API_URL)
  soup = BeautifulSoup(r.text, 'lxml')
  value = float(soup.findAll('td')[14].getText()[3:])
  return value

def shouldIBuy():
  global valueUpdated
  euNow = getValue()
  if euNow < 6.63:
    if not valueUpdated:
      valueUpdated = True
      msg = "Compre\nValor = " + str(euNow)
      sendMesg(msg)
  else:
    if valueUpdated:
      msg = "Valor muito elevado\nEsqueça"
      sendMesg(msg)
      valueUpdated = False
    else:
      pass

def main():
  while True:
    shouldIBuy()
    time.sleep(60*5)

if __name__ == '__main__':
  print("Rodando")
  main()
