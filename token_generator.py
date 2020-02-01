from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
path = "D:\\Python\Projekty\\15. calendar\\tests\\client_secret.json"

scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file(path, scopes=scopes)
credentials = flow.run_console()
pickle.dump(credentials, open("token.pkl", "wb"))


