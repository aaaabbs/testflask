from flask import Flask, redirect, request, make_response
from datetime import datetime
import uuid
import os

app = Flask(__name__)

visitor_data = []

plastic = 0
can = 0

def choosewaste(typeofwaste,wasteemoji):
    visitor_id = request.cookies.get('visitor_id')

    if not visitor_id:
        visitor_id = str(uuid.uuid4())

    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    user_agent = request.user_agent.string
    access_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    visitor_data.append({'ip': ip, 'user_agent': user_agent, 'access_time': access_time, 'type': typeofwaste, 'visitor_id': visitor_id})

    response = make_response(f"""
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{typeofwaste} Waste Contribution</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f4f7;
                margin: 0;
                padding: 0;
                color: #333;
                text-align: center;
            }}
            h1 {{
                color: #007BFF;
                font-size: 2em;
                margin-top: 50px;
            }}
            .message {{
                font-size: 3em;
                font-weight: bold;
                color: #007BFF;
                margin-top: 30px;
                padding: 20px;
                background-color: #ffffff;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
                display: inline-block;
                margin-bottom: 50px;
            }}
            .container {{
                width: 90%;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
            p {{
                font-size: 1.2em;
                color: #444;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Thank you for your participation!</h1>
            <div class="message">
                You have put <b>{typeofwaste} waste</b> {wasteemoji} into the bin!
            </div>
        </div>
    </body>
    </html>
    """)

    response.set_cookie('visitor_id', visitor_id, max_age=60*60*24*365)
    return response


@app.route('/')
def home():
    return "Welcome! Use /track to track clicks or /stats to view click statistics."


@app.route('/Plastic')
def Plastic():
    global plastic
    plastic += 1
    return choosewaste('Plastic', '🥤')

@app.route('/Can')
def Can():
    global can
    can += 1
    return choosewaste('Can', '🥫')

@app.route('/stats')
def stats():
    # HTML for table header
    table_header = """
    <table style="width: 100%; border-collapse: collapse; background-color: #ffffff; color: #333;">
        <thead style="background-color: #007BFF; color: white;">
            <tr>
                <th style="padding: 10px; text-align: left;">IP Address</th>
                <th style="padding: 10px; text-align: left;">User Agent</th>
                <th style="padding: 10px; text-align: left;">Access Time</th>
                <th style="padding: 10px; text-align: left;">Type of Waste</th>
                <th style="padding: 10px; text-align: left;">Visitor ID</th>
            </tr>
        </thead>
        <tbody>
    """

    # HTML for table rows
    table_rows = ""
    for visitor in visitor_data:
        table_rows += f"""
        <tr style="border-bottom: 1px solid #ddd;">
            <td style="padding: 8px;">{visitor['ip']}</td>
            <td style="padding: 8px;">{visitor['user_agent']}</td>
            <td style="padding: 8px;">{visitor['access_time']}</td>
            <td style="padding: 8px;">{visitor['type']}</td>
            <td style="padding: 8px;">{visitor['visitor_id']}</td>
        </tr>
        """

    # HTML for table footer
    table_footer = """
        </tbody>
    </table>
    """

    # Combine the table parts
    table_html = table_header + table_rows + table_footer

    # Combine table with summary info
    response_html = f"""
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Visitor Stats</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f4f7;
                margin: 0;
                padding: 0;
                color: #333;
            }}
            h1 {{
                color: #007BFF;
                text-align: center;
                padding: 20px;
                font-size: 2.5em;
            }}
            p {{
                font-size: 1.2em;
                color: #444;
                text-align: center;
                margin: 10px 0;
            }}
            h2 {{
                text-align: center;
                color: #007BFF;
                font-size: 1.8em;
                margin-top: 30px;
            }}
            .container {{
                width: 90%;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background-color: white;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
            }}
            .table-wrapper {{
                margin-top: 30px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Website Visitor Stats</h1>
            <p><b>Total Plastic Clicks:</b> {plastic}</p>
            <p><b>Total Can Clicks:</b> {can}</p>
            <p><b>Total Unique Visitors:</b> {len(set(visitor['visitor_id'] for visitor in visitor_data))}</p>
            <div class="table-wrapper">
                <h2>Visitor Data</h2>
                {table_html}
            </div>
        </div>
    </body>
    </html>
    """

    return response_html

@app.route('/reset')
def reset():
    visitor_data = []
    return f'{visitor_data}\n\nDelete data done!\n\n{visitor_data}'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
