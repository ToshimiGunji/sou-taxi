import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime

# SCOPES = ['https://spreadsheets.google.com/feeds',
#           'https://www.googleapis.com/auth/drive']
# SERVICE_ACCOUNT_FILE = "sou-taxi-project-d2a843809101.json"
# credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)
# gc = gspread.authorize(credentials)
# SPREADSHEET_KEY = "16OD2Rv51rAMy-UPChHTsuoQQADm-huMt-9QTSKaDHy0"
#
# workbook = gc.open_by_key(SPREADSHEET_KEY)
# worksheet = workbook.worksheet("シート1")
# # worksheet_list = workbook.worksheets()
# # worksheet = gs.open_by_key(SPREADSHEET_KEY).worksheet("シート1")
# worksheet.update_acell("A3", str(datetime.now()))

while True:
    start = input("乗車")
    if start == "乗車":
        get_on_time = datetime.now()
        print(get_on_time)
        while True:
            finish = input("降車")
            if finish == "降車":
                get_off_time = datetime.now()
                print(get_off_time)
                print(get_off_time - get_on_time)
            else:
                print("有効なコマンドではありません")
                continue
    else:
        print("有効なコマンドではありません")
        continue
