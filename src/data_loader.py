import pandas as pd

def load_excel(files):
    dfs=[pd.read_excel(f) for f in files]
    return pd.concat(dfs, ignore_index=True)

def load_google_sheet(sheet):
    import gspread
    import pandas as pd
    gc = gspread.service_account(filename="config/service_account.json")
    sh = gc.open(sheet).sheet1
    data = sh.get_all_records()
    return pd.DataFrame(data)
