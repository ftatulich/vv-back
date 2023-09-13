import gspread
from oauth2client.service_account import ServiceAccountCredentials

credentials = ServiceAccountCredentials.from_json_keyfile_name("services/creds.json")
gc = gspread.authorize(credentials)

spreadsheet_url = "https://docs.google.com/spreadsheets/d/1pcOTCho5qksYO7xrjtT2drW472HHzIMVbmbMM2gtq_A"
worksheet = gc.open_by_url(spreadsheet_url).sheet1

def append_table(answers: list[str]):
    worksheet.append_rows([answers])