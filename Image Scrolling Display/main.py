import firebase_admin
import pygame
import pyrebase
from firebase_admin import firestore
from firebase_admin import credentials
import urllib.request
from time import sleep
import os

import requests
from pygame.locals import *

url = "http://www.kite.com"
timeout = 5

credPath = {
    "type": "service_account",
    "project_id": "",
    "private_key_id": "",
    "private_key": "",
    "client_email": "",
    "client_id": "",
    "auth_uri": "",
    "token_uri": "",
    "auth_provider_x509_cert_url": "",
    "client_x509_cert_url": ""
}

login = credentials.Certificate(credPath)
firebase_admin.initialize_app(login)
db = firestore.client()

pygame.init()
pygame.display.set_caption("Scrolling Text")
WIDTH = 1280
HEIGHT = 1080
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
# pygame.FULLSCREEN
list = [""]
count = 0
isTrue = True

config = {
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": "",
    "databaseURL": "",

}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

isTrue = True
mode = "1"


def isWifi():
    try:
        request = requests.get(url, timeout=timeout)
        print("Connected to the Internet")
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")
        return False




def updateImages():
    collection = db.collection("photos").stream()
    List_file = []
    List_collection = {}
    OfflineLinks = ""
    for x in collection:
        List_collection.update({x.to_dict()['photoName']: x.to_dict()["link"]})
    print(List_collection)
    with open("file.txt", "r") as f:
        List_file.append(f.read().split(","))
    for x_file in List_file[0][1:]:
        if x_file not in List_collection:
            try:
                os.remove(x_file)
            except:
                print("error while deleting or file is already deleted")
        else:
            OfflineLinks = OfflineLinks + "," + x_file

    for x_file in List_collection:
        if x_file not in List_file:
            try:
                urllib.request.urlretrieve(List_collection[x_file], f"{x_file}")
                OfflineLinks = OfflineLinks +","+ x_file
            except:
                print("error while Adding")
    with open("file.txt", "w") as f:
        f.write(OfflineLinks)

updateImages()
while False:
    wifiOut = isWifi()
    if not wifiOut:
        List_file = []
        with open("file.txt", "r") as f:
            List_file.append(f.read().split(","))
        while isTrue:
            for x in List_file[0][1:]:
                img = pygame.image.load(x)
                windowSurface.blit(img, (0, 0))
                pygame.display.flip()
                sleep(1)
                isTrue != isWifi()
    else:
        mode = database.child("mode").get().val()
        updateImages()
        List_file = []
        with open("file.txt", "r") as f:
            List_file.append(f.read().split(","))
        while isTrue:
            isTrue = database.child("isRepeat").get().val()
            if database.child("mode").get().val() != "1":
                break
            out1 = database.child("delay").get().val()
            for x in List_file[0][1:]:
                print(x)
                img = pygame.image.load(x)
                windowSurface.blit(img, (0, 0))
                pygame.display.flip()
                sleep(out1)
        isTrue = database.child("isRepeat").get().val()
        sleep(1)
    sleep(1)
