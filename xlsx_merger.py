import pandas as pd
from os import listdir

datapath = "data/"
xlsx_file_names = listdir(datapath)

print(f"{len(xlsx_file_names)} files found:\n" + "\n".join(xlsx_file_names))
print("importing...")
dfs = [pd.read_excel(datapath + fn) for fn in xlsx_file_names]

print(f"{len(dfs)} files imported!")

if len(xlsx_file_names) != len(dfs):
    print("Imported files:")
    print(dfs)
    print("Not all files could be imported! Exiting...")
    exit()

row_count = 0
standard_col = dfs[0].columns.tolist()
for n, df in enumerate(dfs):
    if len(df.columns) != 35:
        print(xlsx_file_names[n] + " File does not contain all columns! Should be 35 is " + str(len(df.columns)))
    else:
        row_count += df.shape[0]
    df_cols = df.columns.tolist()
    if df_cols != standard_col:
        print(xlsx_file_names[n])
        for dfc, org in zip(df_cols, standard_col):
            if dfc != org:
                print("\t", org, "<-->", dfc)

print(f"{row_count} rows counted!")

df = pd.concat(dfs)
print(df.shape)
df = df.rename(columns={'Wenn du bei Frage 4 "Sonstige" angekreuzt hast, gib an, was du dabei gemeint hast.':'Wenn du bei Frage 14 "Sonstige" angekreuzt hast, gib an, was du dabei gemeint hast.'})

df = df.reset_index()
print(df.columns)

df.drop(["index", "Name", "E-Mail", "Schule", "Klasse"], axis=1).to_csv("Motivation im Onlineunterricht.csv")
df.drop(["index", "Name", "E-Mail", "Klasse"]).to_csv("motivation.csv")
