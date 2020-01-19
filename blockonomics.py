import configloader
import requests

# Define all the database tables using the sqlalchemy declarative base
class Blockonomics:
    def fetch_new_btc_price():
        url = 'https://www.blockonomics.co/api/price'
        params = {'currency':configloader.config["Payments"]["currency"]}
        r = requests.get(url,params)
        if r.status_code == 200:
          price = r.json()['price']
          return price
        else:
          print(r.status_code, r.text)

    def new_address(reset=False):
        api_key = configloader.config["Bitcoin"]["api_key"]
        url = 'https://www.blockonomics.co/api/new_address'
        if reset == True:
          url += '?reset=1'
        headers = {'Authorization': "Bearer " + api_key}
        r = requests.post(url, headers=headers)
        if r.status_code == 200:
          return r
        else:
          print(r.status_code, r.text)
          return r

    def get_balance(address):
        api_key = configloader.config["Bitcoin"]["api_key"]
        url = 'https://www.blockonomics.co/api/balance'
        data = {'addr':address}
        r = requests.post(url, json = data)
        if r.status_code == 200:
          return r
        else:
          print(r.status_code, r.text)