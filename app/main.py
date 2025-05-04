# This script generates a simple HTML report for the weather.
# It creates an HTML file with a title and a paragraph displaying the temperature.
from datetime import datetime

def generate_report():
    # Current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""
    <html>
    <head><title>Weather Report</title></head>
    <body>
        <h1>Wellcome to CICD Class</h1>
        <h1>Today's Weather</h1>
        <p>Temperature: 30°C</p>
        <p>Report generated at: {timestamp}</p>
    </body>
    </html>
    """

    with open("report.html", "w") as f:
        f.write(html)
    print("✅ Report generated at:", timestamp)
    return True

if __name__ == "__main__":
    generate_report()
