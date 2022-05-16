import pandas as pd

data = pd.read_json('multipage/vehicle_data.json', encoding = 'ISO-8859-1')

df = pd.DataFrame(data)
    
html = df.to_html()

text_file = open("templates/junk/data.html", "w")
text_file.write(html)
text_file.close()

        
    


 