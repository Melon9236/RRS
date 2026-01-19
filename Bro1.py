from flask import Flask, url_for

app = Flask(__name__)

# Home page with semi-transparent background image
@app.route("/")
def home():
    return f"""
    <html>
        <head>
            <title>Sinta Room Reservation System</title>
            <style>
                @import url('https://fonts.cdnfonts.com/css/trajan-pro');

                body {{
                    font-family: 'Trajan Pro', serif;
                    margin: 0;
                    text-align: center;
                    background-image: url('{url_for('static', filename='images.png')}');
                    background-size: cover;
                    background-position: center;
                    background-repeat: no-repeat;
                    position: relative;
                }}

                /* Semi-transparent overlay for readability */
                body::before {{
                    content: "";
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background-color: rgba(255,255,255,0.2);
                    z-index: -1;
                }}

                /* Header */
                h1 {{
                    background-color: rgba(224,224,224,0.8); /* light gray, semi-transparent */
                    color: maroon;
                    padding: 20px;
                    margin: 0;
                    font-size: 40px;
                    border: 3px solid maroon; /* maroon border */
                }}

                /* Subheader / category buttons container */
                .button-container {{
                    margin-top: 20px;
                    background-color: rgba(255,215,0,0.8); /* gold/yellow, semi-transparent */
                    padding: 15px 0;
                    border: 3px solid maroon; /* maroon border */
                }}

                /* Buttons inside subheader */
                .btn {{
                    display: inline-block;
                    margin: 10px;
                    padding: 12px 25px;
                    background-color: yellow; /* button background */
                    color: gray;              /* button text */
                    font-size: 18px;
                    border: none;
                    border-radius: 8px;
                    cursor: pointer;
                    text-decoration: none;
                    font-family: 'Trajan Pro', serif;
                    transition: all 0.3s ease;
                }}

                .btn:hover {{
                    background-color: #ffd700; /* darker yellow on hover */
                    font-weight: bold;
                }}

                /* Make the text of links in subheader maroon */
                .button-container a {{
                    color: maroon;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <h1>Sinta Room Reservation System</h1>

            <div class="button-container">
                <a href="/available" class="btn">Available Rooms</a>
                <a href="/reserved" class="btn">Reserved Rooms</a>
                <a href="/occupied" class="btn">Occupied Rooms</a>
                <a href="/all" class="btn">All Rooms</a>
            </div>
        </body>
    </html>
    """

# Function to create room pages with color-coded boxes
def rooms_page(title, description, color):
    boxes_html = ''.join([
        f'<div class="box" style="border-color:{color};">{i+1}</div>'
        for i in range(8)
    ])
    return f"""
    <html>
        <head>
            <title>{title}</title>
            <style>
                @import url('https://fonts.cdnfonts.com/css/trajan-pro');
                body {{
                    font-family: 'Trajan Pro', serif;
                    margin: 0;
                    text-align: center;
                    background-color: #f5f5f5;
                }}
                h2 {{ color: maroon; margin-top: 20px; }}
                .subtext {{ font-weight: bold; color: maroon; font-size: 20px; margin: 10px 0 30px 0; }}
                .boxes {{
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 20px;
                    margin-bottom: 30px;
                }}
                .box {{
                    width: 120px;
                    height: 120px;
                    border: 3px solid {color};
                    border-radius: 15px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-family: 'Trajan Pro', serif;
                    font-size: 16px;
                    color: maroon;
                    background-color: #ffffff;
                }}
            </style>
        </head>
        <body>
            <h2>{title}</h2>
            <p class="subtext">{description}</p>
            <div class="boxes">
                {boxes_html}
            </div>
        </body>
    </html>
    """

# Routes for subpages
@app.route("/available")
def available():
    return rooms_page("Available Rooms", "These rooms are available.", "green")

@app.route("/reserved")
def reserved():
    return rooms_page("Reserved Rooms", "These rooms are reserved.", "orange")

@app.route("/occupied")
def occupied():
    return rooms_page("Occupied Rooms", "These rooms are occupied.", "red")

@app.route("/all")
def all_rooms():
    colors = ["green"]*3 + ["orange"]*3 + ["red"]*2
    boxes_html = ''.join([
        f'<div class="box" style="border-color:{c};">{i+1}</div>'
        for i, c in enumerate(colors)
    ])
    return f"""
    <html>
        <head>
            <title>All Rooms</title>
            <style>
                @import url('https://fonts.cdnfonts.com/css/trajan-pro');
                body {{
                    font-family: 'Trajan Pro', serif;
                    margin: 0;
                    text-align: center;
                    background-color: #f5f5f5;
                }}
                h2 {{ color: maroon; margin-top: 20px; }}
                .subtext {{ font-weight: bold; color: maroon; font-size: 20px; margin: 10px 0 30px 0; }}
                .boxes {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-bottom: 30px; }}
                .box {{
                    width: 120px; height: 120px; border: 3px solid; border-radius: 15px;
                    display: flex; align-items: center; justify-content: center;
                    font-family: 'Trajan Pro', serif; font-size: 16px; color: maroon; background-color: #ffffff;
                }}
            </style>
        </head>
        <body>
            <h2>All Rooms</h2>
            <p class="subtext">All rooms regardless of status.</p>
            <div class="boxes">
                {boxes_html}
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
