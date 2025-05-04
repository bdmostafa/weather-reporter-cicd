# This script generates a simple HTML report for the weather.
# It creates an HTML file with a title and a paragraph displaying the temperature.
def generate_report():
    html = """
    <html>
    <head><title>Weather Report</title></head>
    <body>
        <h1>Today's Weather</h1>
        <p>Temperature: 30°C</p>
    </body>
    </html>
    """
    with open("report.html", "w") as f:
        f.write(html)
    return True

if __name__ == "__main__":
    generate_report()
