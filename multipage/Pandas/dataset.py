import pandas as pd


df = pd.read_json('multipage/vehicle_data.json', encoding = 'ISO-8859-1')

print(df.info)

nan_value = float("NaN")

df.replace("", nan_value, inplace=True)

df.dropna(subset = ["reason_1"], inplace=True)
df.dropna(subset = ["reason_2"], inplace=True)
df.dropna(subset = ["reason_3"], inplace=True)

del df['rejection_percentage']

html = df.to_html()

print(df.sample)

text_file = open("templates/junk/cleaned.html", "w")
text_file.write(html)
text_file.close()
