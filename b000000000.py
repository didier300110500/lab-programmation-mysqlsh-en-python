# -*- coding: utf-8 -*-
"""

@author: 300110500
"""

import json

def charge(fichier):
   with open(fichier) as f:
      return json.load(f)

import mysqlx
session = mysqlx.get_session({
    "host": "localhost",
    "port": 33060,
    "user": "root",
    "password": "password"
})

db = session.get_schema("world_x")

def main():
  print(charge('b000000000.json'))

# Ne pas oublier de remercier le gestionnaire de BD
  session.close

if __name__== "__main__":
    main()
