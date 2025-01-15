from flask import Flask, request, make_response
from datetime import datetime
import uuid
from pyairtable import Api
import threading

app = Flask(__name__)

API_KEY = "patfVbNtFooligV4r.ad5866b4b280ec7b6d41ebdd7759f0ff1babb6a61b2575900dd3c0d487960af3"
BASE_ID = "appGAffUHZ28wrxIK"

api = Api(API_KEY)
table = api.base(BASE_ID).table("Table 1")
table_cookie = api.base(BASE_ID).table("Cookies")

@app.route('/delete_all_cookiesaofdhgpoewhtr')
def delete_all_cookies():
    # Create a response object
    from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/delete_cookies')
def delete_all_cookies():
    # Create a response object
    response = make_response("All cookies have been deleted.")

    # Log the initial cookies from the request
    print("Cookies in request:", request.cookies)

    # Loop through all cookies in the request and set their expiration to the past
    for cookie in request.cookies:
        print(f"Deleting cookie: {cookie}")
        response.set_cookie(cookie, '', expires=0)

    # Log the Set-Cookie headers in the response
    print("Response Set-Cookie headers:", response.headers.getlist('Set-Cookie'))

    return response


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Get visitor_id from cookies or generate a new one
        visitor_id = request.cookies.get('visitor_id')
        print(visitor_id)
        if not visitor_id:
            visitor_id = str(uuid.uuid4())
        else:
            response = make_response(
                '''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Submission Successful</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            background-color: #f0f4f7;
                            margin: 0;
                            padding: 0;
                            color: #333;
                            text-align: center;
                        }
                        .container {
                            width: 90%;
                            max-width: 600px;
                            margin: 0 auto;
                            padding: 20px;
                        }
                        h1 {
                            color: #007BFF;
                            font-size: 2.5em;
                            margin-top: 50px;
                        }
                        .message {
                            font-size: 1.5em;
                            font-weight: bold;
                            color: #444;
                            margin-top: 30px;
                            padding: 20px;
                            background-color: #ffffff;
                            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                            border-radius: 10px;
                            display: inline-block;
                        }
                        p {
                            font-size: 1.2em;
                            color: #666;
                        }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Sorry.</h1>
                        <div class="message">
                            You have already submit this form.
                        </div>
                        <p>Thatchawit 669, Thitipat 670, Vorapon 705</p>
                    </div>
                </body>
                </html>
                '''
            )
            return response

        # Get form data
        name = request.form.get('name')
        grade = request.form.get('grade')

        # Save to Airtable
        table_cookie.create({
            'Cookie': visitor_id,
            'Name': name,
            'Grade': grade,
            'Last time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })

        # Redirect to the submitted page with a cookie
        response = make_response(
            '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Submission Successful</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f0f4f7;
                        margin: 0;
                        padding: 0;
                        color: #333;
                        text-align: center;
                    }
                    .container {
                        width: 90%;
                        max-width: 600px;
                        margin: 0 auto;
                        padding: 20px;
                    }
                    h1 {
                        color: #007BFF;
                        font-size: 2.5em;
                        margin-top: 50px;
                    }
                    .message {
                        font-size: 1.5em;
                        font-weight: bold;
                        color: #444;
                        margin-top: 30px;
                        padding: 20px;
                        background-color: #ffffff;
                        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                        border-radius: 10px;
                        display: inline-block;
                    }
                    p {
                        font-size: 1.2em;
                        color: #666;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Thank You!</h1>
                    <div class="message">
                        Your form has been successfully submitted.
                    </div>
                    <p>Thatchawit 669, Thitipat 670, Vorapon 705</p>
                </div>
            </body>
            </html>
            '''
        )
        response.set_cookie('visitor_id', visitor_id, max_age=60*60*24*365)
        return response

    # Render the form for GET requests
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Form Submission</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f4f7;
                margin: 0;
                padding: 0;
                color: #333;
                text-align: center;
            }
            .container {
                width: 90%;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }
            h1 {
                color: #007BFF;
                margin-top: 50px;
                font-size: 2em;
            }
            form {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }
            label {
                font-size: 1.2em;
                color: #444;
            }
            input, select, button {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                font-size: 1em;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            button {
                background-color: #007BFF;
                color: white;
                font-size: 1.2em;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Submit Your Information</h1>
            <form method="POST" action="/form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" placeholder="Ex: Thitipat Jirataweewong" style="background-color: transparent;" required>
                <br>
                <label for="nickname">Nickname:</label>
                <input type="text" id="nickname" name="nickname" placeholder="Ex: Khaopan" style="background-color: transparent;" required>
                <br>
                <label for="grade">Select Grade:</label>
                <select id="grade" name="grade" required>
                    <option value="M4">M4</option>
                    <option value="M5">M5</option>
                    <option value="M6">M6</option>
                </select>
                <br>
                <button type="submit">Submit</button>
            </form>
            <p>Thatchawit 669, Thitipat 670, Vorapon 705</p>
        </div>
    </body>
    </html>
    '''



def choosewaste(typeofwaste, wasteemoji, location):
    visitor_id = request.cookies.get('visitor_id')

    if not visitor_id:
        response = make_response(
            '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Submission Successful</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f0f4f7;
                        margin: 0;
                        padding: 0;
                        color: #333;
                        text-align: center;
                    }
                    .container {
                        width: 90%;
                        max-width: 600px;
                        margin: 0 auto;
                        padding: 20px;
                    }
                    h1 {
                        color: #007BFF;
                        font-size: 2.5em;
                        margin-top: 50px;
                    }
                    .message {
                        font-size: 1.5em;
                        font-weight: bold;
                        color: #444;
                        margin-top: 30px;
                        padding: 20px;
                        background-color: #ffffff;
                        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                        border-radius: 10px;
                        display: inline-block;
                    }
                    p {
                        font-size: 1.2em;
                        color: #666;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Sorry.</h1>
                    <div class="message">
                        You are not choosen for this statistic project.
                    </div>
                    <p>Thatchawit 669, Thitipat 670, Vorapon 705</p>
                </div>
            </body>
            </html>
            '''
        )
        return response

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.user_agent.string
    access_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Function to handle table.create in a separate thread
    def log_waste_to_table():
        table.create({
            "IP address": ip,
            "User Agent": user_agent,
            "Access time": access_time,
            "Type of waste": typeofwaste,
            "Visitor ID": visitor_id,
            "Location": location
        })

    # Start the logging in a separate thread
    threading.Thread(target=log_waste_to_table).start()

    # Generate and return the response immediately
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
                You have put <b>{typeofwaste} waste</b> {wasteemoji} into the bin at {location}!
            </div>
        </div>
    </body>
    </html>
    """)

    return response


@app.route('/')
def home():
    return "Hello! Nothing's here!"


















@app.route('/PlasticAtFloor1Wing1')
def PlasticAtFloor1Wing1():
    return choosewaste('Plastic', '🥤','Floor1Wing1')

@app.route('/MetalAtFloor1Wing1')
def MetalAtFloor1Wing1():
    return choosewaste('Metal', '⚙️','Floor1Wing1')

@app.route('/PaperAtFloor1Wing1')
def PaperAtFloor1Wing1():
    return choosewaste('Paper/Cardboard', '📝/📦','Floor1Wing1')

@app.route('/GlassAtFloor1Wing1')
def GlassAtFloor1Wing1():
    return choosewaste('Glass', '🫙','Floor1Wing1')

@app.route('/OtherRecyclableAtFloor1Wing1')
def OtherRecyclableAtFloor1Wing1():
    return choosewaste('Other type of recyclable', '♻️','Floor1Wing1')

@app.route('/NonRecyclableAtFloor1Wing1')
def OtherNonRecyclableAtFloor1Wing1():
    return choosewaste('Non-recyclable', '🚫','Floor1Wing1')



@app.route('/PlasticAtFloor1Wing2')
def PlasticAtFloor1Wing2():
    return choosewaste('Plastic', '🥤','Floor1Wing2')

@app.route('/MetalAtFloor1Wing2')
def MetalAtFloor1Wing2():
    return choosewaste('Metal', '⚙️','Floor1Wing2')

@app.route('/PaperAtFloor1Wing2')
def PaperAtFloor1Wing2():
    return choosewaste('Paper/Cardboard', '📝/📦','Floor1Wing2')

@app.route('/GlassAtFloor1Wing2')
def GlassAtFloor1Wing2():
    return choosewaste('Glass', '🫙','Floor1Wing2')

@app.route('/OtherRecyclableAtFloor1Wing2')
def OtherRecyclableAtFloor1Wing2():
    return choosewaste('Other type of recyclable', '♻️','Floor1Wing2')

@app.route('/NonRecyclableAtFloor1Wing2')
def OtherNonRecyclableAtFloor1Wing2():
    return choosewaste('Non-recyclable', '🚫','Floor1Wing2')



@app.route('/PlasticAtFloor1Wing3')
def PlasticAtFloor1Wing3():
    return choosewaste('Plastic', '🥤','Floor1Wing3')

@app.route('/MetalAtFloor1Wing3')
def MetalAtFloor1Wing3():
    return choosewaste('Metal', '⚙️','Floor1Wing3')

@app.route('/PaperAtFloor1Wing3')
def PaperAtFloor1Wing3():
    return choosewaste('Paper/Cardboard', '📝/📦','Floor1Wing3')

@app.route('/GlassAtFloor1Wing3')
def GlassAtFloor1Wing3():
    return choosewaste('Glass', '🫙','Floor1Wing3')

@app.route('/OtherRecyclableAtFloor1Wing3')
def OtherRecyclableAtFloor1Wing3():
    return choosewaste('Other type of recyclable', '♻️','Floor1Wing3')

@app.route('/NonRecyclableAtFloor1Wing3')
def OtherNonRecyclableAtFloor1Wing3():
    return choosewaste('Non-recyclable', '🚫','Floor1Wing3')



@app.route('/PlasticAtFloor1Wing4')
def PlasticAtFloor1Wing4():
    return choosewaste('Plastic', '🥤','Floor1Wing4')

@app.route('/MetalAtFloor1Wing4')
def MetalAtFloor1Wing4():
    return choosewaste('Metal', '⚙️','Floor1Wing4')

@app.route('/PaperAtFloor1Wing4')
def PaperAtFloor1Wing4():
    return choosewaste('Paper/Cardboard', '📝/📦','Floor1Wing4')

@app.route('/GlassAtFloor1Wing4')
def GlassAtFloor1Wing4():
    return choosewaste('Glass', '🫙','Floor1Wing4')

@app.route('/OtherRecyclableAtFloor1Wing4')
def OtherRecyclableAtFloor1Wing4():
    return choosewaste('Other type of recyclable', '♻️','Floor1Wing4')

@app.route('/NonRecyclableAtFloor1Wing4')
def OtherNonRecyclableAtFloor1Wing4():
    return choosewaste('Non-recyclable', '🚫','Floor1Wing4')



@app.route('/PlasticAtFloor2Wing1')
def PlasticAtFloor2Wing1():
    return choosewaste('Plastic', '🥤','Floor2Wing1')

@app.route('/MetalAtFloor2Wing1')
def MetalAtFloor2Wing1():
    return choosewaste('Metal', '⚙️','Floor2Wing1')

@app.route('/PaperAtFloor2Wing1')
def PaperAtFloor2Wing1():
    return choosewaste('Paper/Cardboard', '📝/📦','Floor2Wing1')

@app.route('/GlassAtFloor2Wing1')
def GlassAtFloor2Wing1():
    return choosewaste('Glass', '🫙','Floor2Wing1')

@app.route('/OtherRecyclableAtFloor2Wing1')
def OtherRecyclableAtFloor2Wing1():
    return choosewaste('Other type of recyclable', '♻️','Floor2Wing1')

@app.route('/NonRecyclableAtFloor2Wing1')
def OtherNonRecyclableAtFloor2Wing1():
    return choosewaste('Non-recyclable', '🚫','Floor2Wing1')



@app.route('/PlasticAtFloor2Wing2')
def PlasticAtFloor2Wing2():
    return choosewaste('Plastic', '🥤','Floor2Wing2')

@app.route('/MetalAtFloor2Wing2')
def MetalAtFloor2Wing2():
    return choosewaste('Metal', '⚙️','Floor2Wing2')

@app.route('/PaperAtFloor2Wing2')
def PaperAtFloor2Wing2():
    return choosewaste('Paper/Cardboard', '📝/📦','Floor2Wing2')

@app.route('/GlassAtFloor2Wing2')
def GlassAtFloor2Wing2():
    return choosewaste('Glass', '🫙','Floor2Wing2')

@app.route('/OtherRecyclableAtFloor2Wing2')
def OtherRecyclableAtFloor2Wing2():
    return choosewaste('Other type of recyclable', '♻️','Floor2Wing2')

@app.route('/NonRecyclableAtFloor2Wing2')
def OtherNonRecyclableAtFloor2Wing2():
    return choosewaste('Non-recyclable', '🚫','Floor2Wing2')



@app.route('/PlasticAtFloor2Wing3')
def PlasticAtFloor2Wing3():
    return choosewaste('Plastic', '🥤','Floor2Wing3')

@app.route('/MetalAtFloor2Wing3')
def MetalAtFloor2Wing3():
    return choosewaste('Metal', '⚙️','Floor2Wing3')

@app.route('/PaperAtFloor2Wing3')
def PaperAtFloor2Wing3():
    return choosewaste('Paper/Cardboard', '📝/📦','Floor2Wing3')

@app.route('/GlassAtFloor2Wing3')
def GlassAtFloor2Wing3():
    return choosewaste('Glass', '🫙','Floor2Wing3')

@app.route('/OtherRecyclableAtFloor2Wing3')
def OtherRecyclableAtFloor2Wing3():
    return choosewaste('Other type of recyclable', '♻️','Floor2Wing3')

@app.route('/NonRecyclableAtFloor2Wing3')
def OtherNonRecyclableAtFloor2Wing3():
    return choosewaste('Non-recyclable', '🚫','Floor2Wing3')



@app.route('/PlasticAtFloor2Wing4')
def PlasticAtFloor2Wing4():
    return choosewaste('Plastic', '🥤','Floor2Wing4')

@app.route('/MetalAtFloor2Wing4')
def MetalAtFloor2Wing4():
    return choosewaste('Metal', '⚙️','Floor2Wing4')

@app.route('/PaperAtFloor2Wing4')
def PaperAtFloor2Wing4():
    return choosewaste('Paper/Cardboard', '📝/📦','Floor2Wing4')

@app.route('/GlassAtFloor2Wing4')
def GlassAtFloor2Wing4():
    return choosewaste('Glass', '🫙','Floor2Wing4')

@app.route('/OtherRecyclableAtFloor2Wing4')
def OtherRecyclableAtFloor2Wing4():
    return choosewaste('Other type of recyclable', '♻️','Floor2Wing4')

@app.route('/NonRecyclableAtFloor2Wing4')
def OtherNonRecyclableAtFloor2Wing4():
    return choosewaste('Non-recyclable', '🚫','Floor2Wing4')



@app.route('/PlasticAtFloor3Wing1')
def PlasticAtFloor3Wing1():
    return choosewaste('Plastic', '🥤','Floor3Wing1')

@app.route('/MetalAtFloor3Wing1')
def MetalAtFloor3Wing1():
    return choosewaste('Metal', '⚙️','Floor3Wing1')

@app.route('/PaperAtFloor3Wing1')
def PaperAtFloor3Wing1():
    return choosewaste('Paper/Cardboard', '📝/📦','Floor3Wing1')

@app.route('/GlassAtFloor3Wing1')
def GlassAtFloor3Wing1():
    return choosewaste('Glass', '🫙','Floor3Wing1')

@app.route('/OtherRecyclableAtFloor3Wing1')
def OtherRecyclableAtFloor3Wing1():
    return choosewaste('Other type of recyclable', '♻️','Floor3Wing1')

@app.route('/NonRecyclableAtFloor3Wing1')
def OtherNonRecyclableAtFloor3Wing1():
    return choosewaste('Non-recyclable', '🚫','Floor3Wing1')



@app.route('/PlasticAtFloor3Wing2')
def PlasticAtFloor3Wing2():
    return choosewaste('Plastic', '🥤','Floor3Wing2')

@app.route('/MetalAtFloor3Wing2')
def MetalAtFloor3Wing2():
    return choosewaste('Metal', '⚙️','Floor3Wing2')

@app.route('/PaperAtFloor3Wing2')
def PaperAtFloor3Wing2():
    return choosewaste('Paper/Cardboard', '📝/📦','Floor3Wing2')

@app.route('/GlassAtFloor3Wing2')
def GlassAtFloor3Wing2():
    return choosewaste('Glass', '🫙','Floor3Wing2')

@app.route('/OtherRecyclableAtFloor3Wing2')
def OtherRecyclableAtFloor3Wing2():
    return choosewaste('Other type of recyclable', '♻️','Floor3Wing2')

@app.route('/NonRecyclableAtFloor3Wing2')
def OtherNonRecyclableAtFloor3Wing2():
    return choosewaste('Non-recyclable', '🚫','Floor3Wing2')



@app.route('/PlasticAtFloor3Wing3')
def PlasticAtFloor3Wing3():
    return choosewaste('Plastic', '🥤','Floor3Wing3')

@app.route('/MetalAtFloor3Wing3')
def MetalAtFloor3Wing3():
    return choosewaste('Metal', '⚙️','Floor3Wing3')

@app.route('/PaperAtFloor3Wing3')
def PaperAtFloor3Wing3():
    return choosewaste('Paper/Cardboard', '📝/📦','Floor3Wing3')

@app.route('/GlassAtFloor3Wing3')
def GlassAtFloor3Wing3():
    return choosewaste('Glass', '🫙','Floor3Wing3')

@app.route('/OtherRecyclableAtFloor3Wing3')
def OtherRecyclableAtFloor3Wing3():
    return choosewaste('Other type of recyclable', '♻️','Floor3Wing3')

@app.route('/NonRecyclableAtFloor3Wing3')
def OtherNonRecyclableAtFloor3Wing3():
    return choosewaste('Non-recyclable', '🚫','Floor3Wing3')



@app.route('/PlasticAtFloor3Wing4')
def PlasticAtFloor3Wing4():
    return choosewaste('Plastic', '🥤','Floor3Wing4')

@app.route('/MetalAtFloor3Wing4')
def MetalAtFloor3Wing4():
    return choosewaste('Metal', '⚙️','Floor3Wing4')

@app.route('/PaperAtFloor3Wing4')
def PaperAtFloor3Wing4():
    return choosewaste('Paper/Cardboard', '📝/📦','Floor3Wing4')

@app.route('/GlassAtFloor3Wing4')
def GlassAtFloor3Wing4():
    return choosewaste('Glass', '🫙','Floor3Wing4')

@app.route('/OtherRecyclableAtFloor3Wing4')
def OtherRecyclableAtFloor3Wing4():
    return choosewaste('Other type of recyclable', '♻️','Floor3Wing4')

@app.route('/NonRecyclableAtFloor3Wing4')
def OtherNonRecyclableAtFloor3Wing4():
    return choosewaste('Non-recyclable', '🚫','Floor3Wing4')










@app.route('/PlasticAtDormB1Floor1')
def PlasticAtDormB1Floor1():
    return choosewaste('Plastic', '🥤','DormB1Floor1')

@app.route('/MetalAtDormB1Floor1')
def MetalAtDormB1Floor1():
    return choosewaste('Metal', '⚙️','DormB1Floor1')

@app.route('/PaperAtDormB1Floor1')
def PaperAtDormB1Floor1():
    return choosewaste('Paper/Cardboard', '📝/📦','DormB1Floor1')

@app.route('/GlassAtDormB1Floor1')
def GlassAtDormB1Floor1():
    return choosewaste('Glass', '🫙','DormB1Floor1')

@app.route('/OtherRecyclableAtDormB1Floor1')
def OtherRecyclableAtDormB1Floor1():
    return choosewaste('Other type of recyclable', '♻️','DormB1Floor1')

@app.route('/NonRecyclableAtDormB1Floor1')
def OtherNonRecyclableAtDormB1Floor1():
    return choosewaste('Non-recyclable', '🚫','DormB1Floor1')



@app.route('/PlasticAtDormB1Floor2')
def PlasticAtDormB1Floor2():
    return choosewaste('Plastic', '🥤','DormB1Floor2')

@app.route('/MetalAtDormB1Floor2')
def MetalAtDormB1Floor2():
    return choosewaste('Metal', '⚙️','DormB1Floor2')

@app.route('/PaperAtDormB1Floor2')
def PaperAtDormB1Floor2():
    return choosewaste('Paper/Cardboard', '📝/📦','DormB1Floor2')

@app.route('/GlassAtDormB1Floor2')
def GlassAtDormB1Floor2():
    return choosewaste('Glass', '🫙','DormB1Floor2')

@app.route('/OtherRecyclableAtDormB1Floor2')
def OtherRecyclableAtDormB1Floor2():
    return choosewaste('Other type of recyclable', '♻️','DormB1Floor2')

@app.route('/NonRecyclableAtDormB1Floor2')
def OtherNonRecyclableAtDormB1Floor2():
    return choosewaste('Non-recyclable', '🚫','DormB1Floor2')



@app.route('/PlasticAtDormB1Floor3')
def PlasticAtDormB1Floor3():
    return choosewaste('Plastic', '🥤','DormB1Floor3')

@app.route('/MetalAtDormB1Floor3')
def MetalAtDormB1Floor3():
    return choosewaste('Metal', '⚙️','DormB1Floor3')

@app.route('/PaperAtDormB1Floor3')
def PaperAtDormB1Floor3():
    return choosewaste('Paper/Cardboard', '📝/📦','DormB1Floor3')

@app.route('/GlassAtDormB1Floor3')
def GlassAtDormB1Floor3():
    return choosewaste('Glass', '🫙','DormB1Floor3')

@app.route('/OtherRecyclableAtDormB1Floor3')
def OtherRecyclableAtDormB1Floor3():
    return choosewaste('Other type of recyclable', '♻️','DormB1Floor3')

@app.route('/NonRecyclableAtDormB1Floor3')
def OtherNonRecyclableAtDormB1Floor3():
    return choosewaste('Non-recyclable', '🚫','DormB1Floor3')



@app.route('/PlasticAtDormB1Floor4')
def PlasticAtDormB1Floor4():
    return choosewaste('Plastic', '🥤','DormB1Floor4')

@app.route('/MetalAtDormB1Floor4')
def MetalAtDormB1Floor4():
    return choosewaste('Metal', '⚙️','DormB1Floor4')

@app.route('/PaperAtDormB1Floor4')
def PaperAtDormB1Floor4():
    return choosewaste('Paper/Cardboard', '📝/📦','DormB1Floor4')

@app.route('/GlassAtDormB1Floor4')
def GlassAtDormB1Floor4():
    return choosewaste('Glass', '🫙','DormB1Floor4')

@app.route('/OtherRecyclableAtDormB1Floor4')
def OtherRecyclableAtDormB1Floor4():
    return choosewaste('Other type of recyclable', '♻️','DormB1Floor4')

@app.route('/NonRecyclableAtDormB1Floor4')
def OtherNonRecyclableAtDormB1Floor4():
    return choosewaste('Non-recyclable', '🚫','DormB1Floor4')



@app.route('/PlasticAtDormB3Floor1')
def PlasticAtDormB3Floor1():
    return choosewaste('Plastic', '🥤','DormB3Floor1')

@app.route('/MetalAtDormB3Floor1')
def MetalAtDormB3Floor1():
    return choosewaste('Metal', '⚙️','DormB3Floor1')

@app.route('/PaperAtDormB3Floor1')
def PaperAtDormB3Floor1():
    return choosewaste('Paper/Cardboard', '📝/📦','DormB3Floor1')

@app.route('/GlassAtDormB3Floor1')
def GlassAtDormB3Floor1():
    return choosewaste('Glass', '🫙','DormB3Floor1')

@app.route('/OtherRecyclableAtDormB3Floor1')
def OtherRecyclableAtDormB3Floor1():
    return choosewaste('Other type of recyclable', '♻️','DormB3Floor1')

@app.route('/NonRecyclableAtDormB3Floor1')
def OtherNonRecyclableAtDormB3Floor1():
    return choosewaste('Non-recyclable', '🚫','DormB3Floor1')



@app.route('/PlasticAtDormB3Floor2')
def PlasticAtDormB3Floor2():
    return choosewaste('Plastic', '🥤','DormB3Floor2')

@app.route('/MetalAtDormB3Floor2')
def MetalAtDormB3Floor2():
    return choosewaste('Metal', '⚙️','DormB3Floor2')

@app.route('/PaperAtDormB3Floor2')
def PaperAtDormB3Floor2():
    return choosewaste('Paper/Cardboard', '📝/📦','DormB3Floor2')

@app.route('/GlassAtDormB3Floor2')
def GlassAtDormB3Floor2():
    return choosewaste('Glass', '🫙','DormB3Floor2')

@app.route('/OtherRecyclableAtDormB3Floor2')
def OtherRecyclableAtDormB3Floor2():
    return choosewaste('Other type of recyclable', '♻️','DormB3Floor2')

@app.route('/NonRecyclableAtDormB3Floor2')
def OtherNonRecyclableAtDormB3Floor2():
    return choosewaste('Non-recyclable', '🚫','DormB3Floor2')



@app.route('/PlasticAtDormB3Floor3')
def PlasticAtDormB3Floor3():
    return choosewaste('Plastic', '🥤','DormB3Floor3')

@app.route('/MetalAtDormB3Floor3')
def MetalAtDormB3Floor3():
    return choosewaste('Metal', '⚙️','DormB3Floor3')

@app.route('/PaperAtDormB3Floor3')
def PaperAtDormB3Floor3():
    return choosewaste('Paper/Cardboard', '📝/📦','DormB3Floor3')

@app.route('/GlassAtDormB3Floor3')
def GlassAtDormB3Floor3():
    return choosewaste('Glass', '🫙','DormB3Floor3')

@app.route('/OtherRecyclableAtDormB3Floor3')
def OtherRecyclableAtDormB3Floor3():
    return choosewaste('Other type of recyclable', '♻️','DormB3Floor3')

@app.route('/NonRecyclableAtDormB3Floor3')
def OtherNonRecyclableAtDormB3Floor3():
    return choosewaste('Non-recyclable', '🚫','DormB3Floor3')



@app.route('/PlasticAtDormB3Floor4')
def PlasticAtDormB3Floor4():
    return choosewaste('Plastic', '🥤','DormB3Floor4')

@app.route('/MetalAtDormB3Floor4')
def MetalAtDormB3Floor4():
    return choosewaste('Metal', '⚙️','DormB3Floor4')

@app.route('/PaperAtDormB3Floor4')
def PaperAtDormB3Floor4():
    return choosewaste('Paper/Cardboard', '📝/📦','DormB3Floor4')

@app.route('/GlassAtDormB3Floor4')
def GlassAtDormB3Floor4():
    return choosewaste('Glass', '🫙','DormB3Floor4')

@app.route('/OtherRecyclableAtDormB3Floor4')
def OtherRecyclableAtDormB3Floor4():
    return choosewaste('Other type of recyclable', '♻️','DormB3Floor4')

@app.route('/NonRecyclableAtDormB3Floor4')
def OtherNonRecyclableAtDormB3Floor4():
    return choosewaste('Non-recyclable', '🚫','DormB3Floor4')



@app.route('/PlasticAtDormB4Floor1')
def PlasticAtDormB4Floor1():
    return choosewaste('Plastic', '🥤','DormB4Floor1')

@app.route('/MetalAtDormB4Floor1')
def MetalAtDormB4Floor1():
    return choosewaste('Metal', '⚙️','DormB4Floor1')

@app.route('/PaperAtDormB4Floor1')
def PaperAtDormB4Floor1():
    return choosewaste('Paper/Cardboard', '📝/📦','DormB4Floor1')

@app.route('/GlassAtDormB4Floor1')
def GlassAtDormB4Floor1():
    return choosewaste('Glass', '🫙','DormB4Floor1')

@app.route('/OtherRecyclableAtDormB4Floor1')
def OtherRecyclableAtDormB4Floor1():
    return choosewaste('Other type of recyclable', '♻️','DormB4Floor1')

@app.route('/NonRecyclableAtDormB4Floor1')
def OtherNonRecyclableAtDormB4Floor1():
    return choosewaste('Non-recyclable', '🚫','DormB4Floor1')



@app.route('/PlasticAtDormB4Floor2')
def PlasticAtDormB4Floor2():
    return choosewaste('Plastic', '🥤','DormB4Floor2')

@app.route('/MetalAtDormB4Floor2')
def MetalAtDormB4Floor2():
    return choosewaste('Metal', '⚙️','DormB4Floor2')

@app.route('/PaperAtDormB4Floor2')
def PaperAtDormB4Floor2():
    return choosewaste('Paper/Cardboard', '📝/📦','DormB4Floor2')

@app.route('/GlassAtDormB4Floor2')
def GlassAtDormB4Floor2():
    return choosewaste('Glass', '🫙','DormB4Floor2')

@app.route('/OtherRecyclableAtDormB4Floor2')
def OtherRecyclableAtDormB4Floor2():
    return choosewaste('Other type of recyclable', '♻️','DormB4Floor2')

@app.route('/NonRecyclableAtDormB4Floor2')
def OtherNonRecyclableAtDormB4Floor2():
    return choosewaste('Non-recyclable', '🚫','DormB4Floor2')



@app.route('/PlasticAtDormB4Floor3')
def PlasticAtDormB4Floor3():
    return choosewaste('Plastic', '🥤','DormB4Floor3')

@app.route('/MetalAtDormB4Floor3')
def MetalAtDormB4Floor3():
    return choosewaste('Metal', '⚙️','DormB4Floor3')

@app.route('/PaperAtDormB4Floor3')
def PaperAtDormB4Floor3():
    return choosewaste('Paper/Cardboard', '📝/📦','DormB4Floor3')

@app.route('/GlassAtDormB4Floor3')
def GlassAtDormB4Floor3():
    return choosewaste('Glass', '🫙','DormB4Floor3')

@app.route('/OtherRecyclableAtDormB4Floor3')
def OtherRecyclableAtDormB4Floor3():
    return choosewaste('Other type of recyclable', '♻️','DormB4Floor3')

@app.route('/NonRecyclableAtDormB4Floor3')
def OtherNonRecyclableAtDormB4Floor3():
    return choosewaste('Non-recyclable', '🚫','DormB4Floor3')



@app.route('/PlasticAtDormB4Floor4')
def PlasticAtDormB4Floor4():
    return choosewaste('Plastic', '🥤','DormB4Floor4')

@app.route('/MetalAtDormB4Floor4')
def MetalAtDormB4Floor4():
    return choosewaste('Metal', '⚙️','DormB4Floor4')

@app.route('/PaperAtDormB4Floor4')
def PaperAtDormB4Floor4():
    return choosewaste('Paper/Cardboard', '📝/📦','DormB4Floor4')

@app.route('/GlassAtDormB4Floor4')
def GlassAtDormB4Floor4():
    return choosewaste('Glass', '🫙','DormB4Floor4')

@app.route('/OtherRecyclableAtDormB4Floor4')
def OtherRecyclableAtDormB4Floor4():
    return choosewaste('Other type of recyclable', '♻️','DormB4Floor4')

@app.route('/NonRecyclableAtDormB4Floor4')
def OtherNonRecyclableAtDormB4Floor4():
    return choosewaste('Non-recyclable', '🚫','DormB4Floor4')



@app.route('/PlasticAtARC')
def PlasticAtARC():
    return choosewaste('Plastic', '🥤','ARC')

@app.route('/MetalAtARC')
def MetalAtARC():
    return choosewaste('Metal', '⚙️','ARC')

@app.route('/PaperAtARC')
def PaperAtARC():
    return choosewaste('Paper/Cardboard', '📝/📦','ARC')

@app.route('/GlassAtARC')
def GlassAtARC():
    return choosewaste('Glass', '🫙','ARC')

@app.route('/OtherRecyclableAtARC')
def OtherRecyclableAtARC():
    return choosewaste('Other type of recyclable', '♻️','ARC')

@app.route('/NonRecyclableAtARC')
def OtherNonRecyclableAtARC():
    return choosewaste('Non-recyclable', '🚫','ARC')



@app.route('/PlasticAtCanteen')
def PlasticAtCanteen():
    return choosewaste('Plastic', '🥤','Canteen')

@app.route('/MetalAtCanteen')
def MetalAtCanteen():
    return choosewaste('Metal', '⚙️','Canteen')

@app.route('/PaperAtCanteen')
def PaperAtCanteen():
    return choosewaste('Paper/Cardboard', '📝/📦','Canteen')

@app.route('/GlassAtCanteen')
def GlassAtCanteen():
    return choosewaste('Glass', '🫙','Canteen')

@app.route('/OtherRecyclableAtCanteen')
def OtherRecyclableAtCanteen():
    return choosewaste('Other type of recyclable', '♻️','Canteen')

@app.route('/NonRecyclableAtCanteen')
def OtherNonRecyclableAtCanteen():
    return choosewaste('Non-recyclable', '🚫','Canteen')



@app.route('/PlasticAtGym')
def PlasticAtGym():
    return choosewaste('Plastic', '🥤','Gym')

@app.route('/MetalAtGym')
def MetalAtGym():
    return choosewaste('Metal', '⚙️','Gym')

@app.route('/PaperAtGym')
def PaperAtGym():
    return choosewaste('Paper/Cardboard', '📝/📦','Gym')

@app.route('/GlassAtGym')
def GlassAtGym():
    return choosewaste('Glass', '🫙','Gym')

@app.route('/OtherRecyclableAtGym')
def OtherRecyclableAtGym():
    return choosewaste('Other type of recyclable', '♻️','Gym')

@app.route('/NonRecyclableAtGym')
def OtherNonRecyclableAtGym():
    return choosewaste('Non-recyclable', '🚫','Gym')


















@app.route('/stats')
def stats():
    records = table.all()
    data = [record["fields"] for record in records]
    visitor_data = sorted(data, key=lambda x: x["Access time"], reverse=True)
    print(visitor_data)
    # HTML for table header
    table_header = """
    <table style="width: 100%; border-collapse: collapse; background-color: #ffffff; color: #333;">
        <thead style="background-color: #007BFF; color: white;">
            <tr>
                <th style="padding: 10px; text-align: left;">Access Time</th>
                <th style="padding: 10px; text-align: left;">Type of Waste</th>
            </tr>
        </thead>
        <tbody>
    """

    # HTML for table rows
    table_rows = ""
    for visitor in visitor_data:
        table_rows += f"""
        <tr style="border-bottom: 1px solid #ddd;">
            <td style="padding: 8px;">{visitor['Access time']}</td>
            <td style="padding: 8px;">{visitor['Type of waste']}</td>
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
            <p><b>Total Plastic Clicks:</b> {sum(1 for item in visitor_data if item.get("Type of waste") == 'Plastic')}</p>
            <p><b>Total Can Clicks:</b>{sum(1 for item in visitor_data if item.get("Type of waste") == 'Can')}</p>
            <p><b>Total Unique Visitors:</b> {len(set(visitor['Visitor ID'] for visitor in visitor_data))}</p>
            <div class="table-wrapper">
                <h2>Visitor Data</h2>
                {table_html}
            </div>
        </div>
    </body>
    </html>
    """

    return response_html

if __name__ == '__main__':
    app.run(port=5000)
