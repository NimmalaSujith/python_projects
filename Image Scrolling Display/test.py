import time

from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin
credPath = {
  "type": "service_account",
  "project_id": "ece-news-photo-frame",
  "private_key_id": "85e3ce1f053ad96264f11f89bb383fa4aaf768ef",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC1uFUqYGsN74U3\nsfFRZkgtu0m9rpAtHomnXZKei5vEogXA36qYFObHFpiItbsyEsjC4vG/jY+8ydMG\noT1HgjXLl7ZTTaHSI3OUBLAvcEqBovbq2KOShqNsX9vNUMgKJHLhPQ77t/aGGz5u\nKQCWFl862hgpwpHxOyso6w5rxEHeT474mXXNx8SFyVchUC1onY/PVNtE7ndpeYhk\nbjePDe+MGhtAG6US0cgaecdvINzPhJFI0pQlccmZK0DohqJYPc0Znot7j6Mw2YQe\nHhLNZAyKrI4wNc2Ol7r8nOyRQ2ba8GnqRrbU7bmBoz5f6SzHJ4Gzo5jtJ//PDrxy\nTV97qq2hAgMBAAECggEAAfbqsMkXDzECMy5wyez9pcTrEKpk85/rZAxOa/ldZzxL\nLKEeYoODVS6o2n2AdxOd6QF0FJqOrb9O0TkIBRBizX8n4PGraK6qbrS4ROMFYy5k\nVfiemBRtitvkb+1KJFXtigLTeSQtfZiozZ8S2wyF3giCj10Dn+SAXHJiFwcpoSId\nVGMHp9k/OfIZ8FNluaNwiHDCKmFuGslwftFQ3OQ5WNLuwlA8jWCyz97Q6FAvFFiI\nfShIg17VtumLv4H8VIIyq5TZKzf3ghfPqpVnlGYjRuKxTKASK4MDafUcLKjvr7Zf\n7cKJKqi34FA/Wm01qCP5v4by0OrNmW+nHJ22gEf+gQKBgQD8dsyuthM7hQBRrx6J\n+80k/t41UWOlsYEktHlHwJP+EuZw/egzI27ylFAPQDUbPSMcHpxh47poTvjItj2s\n0RpIT9yfeq7toPI5w8FtbIsDTUPM9BT0v2qN5Z0dZZFVygXjs7k8KxhfM5S/2NpQ\nu+s1tHqk2rIhCg8yl3/HCGhXcQKBgQC4Q+IUpB2ndy6YiEtGMJf9A6qkGC6vrO8S\n1oGbuSBtwKS6+KwtPeJQWaxrWsoCx9D8l/TqTBGuWAOeqIj49mrQ7VdrtU+8OZyV\nL4Tf+/WEcaHHFPiiCdNpzaQqTuKKPMuUb9XzozDBc8VD7gNylzOqTVDvyOMqYYrQ\nCR3EiMKBMQKBgQCbxtno+6PGV/yoajuXvG0KZNDLaVrpBCvBcDJdWbB3V0YldiXu\nV/C/cVAs+NtL4V9mnGS16gQ9FG1hu0E2/xcOg2iIZvTE30hW6DjTwePMt8IcFodP\ntUSUJZfaaa9RlgQoSd8EBztUksk3zyB2LF2nl6MNUXwT8tcJyn0nXEK1oQKBgFTu\nPQNkjaKFpX16vK9ScIuXKAzQdJxWai9VnZGoJ5FOzN69Bacosep1Gqq0ww27CdGT\nPLjNbQzd1nVHmzKdaah47OVhQaoxJ8H/kBApMwXj1jxLpzoQq1hGB5fUmkg7M15s\nmcHdgvh3owHnb8FefdrOHjMXddUv9mpi+Ux/+J7RAoGAIiLNyoUDIP4f8WXgMCpQ\nft5hyRKdZCejz/lBkeaad1tHZSJQTV8O/55zsy7wqQpLKstmDc/v+S9QNAxWoX1m\nryhzwjy8KGXLq3hEBBEb7FVm6kxLyrACBd6FlZ3zfoJ1jD3m+PW9pUwUoZB8l8L/\n6rjYPhAJBd0QCiK1ZPf+gcc=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-sb107@ece-news-photo-frame.iam.gserviceaccount.com",
  "client_id": "117052635523003854004",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-sb107%40ece-news-photo-frame.iam.gserviceaccount.com"
}

login = credentials.Certificate(credPath)
firebase_admin.initialize_app(login)
db = firestore.client()
while True:
    collection = db.collection("photos").stream()
    List = []
    for x in collection:
        List.append(x.to_dict()["link"])
    print(List)
    time.sleep(1)