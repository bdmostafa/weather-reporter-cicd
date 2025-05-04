# This script generates a simple HTML report for the weather.
# It creates an HTML file with a title and a paragraph displaying the temperature.
from datetime import datetime

def generate_report():
    html = """
    <html>
    <head><title>Weather Report</title></head>
    <body>
        <h1>Today's Weather</h1>
        <p>Temperature: 30°C</p>
        <p>Report generated at: {{timestamp}}</p>
    </body>
    </html>
    """
    with open("report.html", "w") as f:
        f.write(html)
    return True

# Current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# HTML file read and add timestamp
with open("report.html", "r") as file:
    html_content = file.read()

html_content = html_content.replace("{{timestamp}}", timestamp)

with open("report.html", "w") as file:
    file.write(html_content)

if __name__ == "__main__":
    generate_report()
