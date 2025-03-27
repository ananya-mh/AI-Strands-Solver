import requests
import datetime
import pandas as pd

# Start and end dates
start_date = datetime.date(2024, 3, 4)
end_date = datetime.date.today()

all_data = []

current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime('%Y-%m-%d')
    url = f"https://www.nytimes.com/svc/strands/v2/{date_str}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        print(f"Retrieved data for {date_str}")

        all_data.append({
            "date": date_str,
            "id": data.get("id"),
            "themeWords": ', '.join(data.get("themeWords", [])),
            "editor": data.get("editor"),
            "constructors": data.get("constructors"),
            "spangram": data.get("spangram"),
            "clue": data.get("clue"),
            "startingBoard": ' '.join(data.get("startingBoard", [])),
            "solutions": ', '.join(data.get("solutions", []))
        })

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data for {date_str}: {e}")

    current_date += datetime.timedelta(days=1)

# Convert to DataFrame and save as CSV
df = pd.DataFrame(all_data)
df.to_csv("strands_data.csv", index=False)

print("Finished scraping and saved to strands_data.csv.")
