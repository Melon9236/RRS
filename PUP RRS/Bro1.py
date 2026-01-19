from flask import Flask, url_for

app = Flask(__name__)

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

                h1 {{
                    background-color: rgba(224,224,224,0.8);
                    color: maroon;
                    padding: 20px;
                    margin: 0;
                    font-size: 40px;
                    border: 3px solid maroon;
                }}

                .button-container {{
                    margin-top: 20px;
                    background-color: rgba(224,224,224,0.8);
                    padding: 15px 0;
                    border: 3px solid maroon;
                    border-radius: 0;
                }}

                .btn {{
                    display: inline-block;
                    margin: 10px;
                    padding: 12px 25px;
                    background-color: #FFD700; /* gold */
                    color: maroon;
                    font-size: 18px;
                    border: 3px solid maroon;
                    border-radius: 8px;
                    cursor: pointer;
                    text-decoration: none;
                    font-family: 'Trajan Pro', serif;
                    transition: all 0.3s ease;
                    font-weight: bold;
                }}

                .btn:hover {{
                    background-color: #FFC300;
                }}

                /* Main box with scroll */
                .main-box {{
                    background-color: rgba(255,255,255,0.8);
                    border: 3px solid maroon;
                    border-radius: 15px;
                    max-width: 900px;
                    max-height: 500px;
                    margin: 20px auto;
                    padding: 30px;
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 20px;
                    overflow-y: auto;
                }}

                .room-box {{
                    width: 120px;
                    height: 120px;
                    border-radius: 15px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-family: 'Trajan Pro', serif;
                    font-size: 16px;
                    color: maroon;
                    margin: 5px;
                }}

                /* Lighter fills with darker borders */
                .available {{
                    background-color: #ccffcc; /* lighter green */
                    border: 3px solid #008000; /* dark green */
                }}
                .reserved {{
                    background-color: #ffddb3; /* lighter orange */
                    border: 3px solid #FF8C00; /* dark orange */
                }}
                .occupied {{
                    background-color: #ff9999; /* lighter red */
                    border: 3px solid #B22222; /* dark red */
                }}
            </style>
        </head>
        <body>
            <h1>Sinta Room Reservation System</h1>

            <div class="button-container">
                <a href="#" class="btn" onclick="showRooms('available')">Available Rooms</a>
                <a href="#" class="btn" onclick="showRooms('reserved')">Reserved Rooms</a>
                <a href="#" class="btn" onclick="showRooms('occupied')">Occupied Rooms</a>
                <a href="#" class="btn" onclick="showRooms('all')">All Rooms</a>
            </div>

            <div class="main-box" id="main-box">
                <!-- Boxes will be dynamically inserted here -->
            </div>

            <script>
                // Room data
                const rooms = {{
                    available: Array.from({{length: 8}}, (_, i) => i+1),
                    reserved: Array.from({{length: 8}}, (_, i) => i+1),
                    occupied: Array.from({{length: 8}}, (_, i) => i+1),
                }};

                // Function to show rooms in main box
                function showRooms(category) {{
                    const mainBox = document.getElementById('main-box');
                    mainBox.innerHTML = ''; // Clear existing content
                    let roomList = [];
                    if(category === 'all') {{
                        // all rooms: combine categories
                        roomList = [
                            ...rooms.available.map(n => ['available', n]),
                            ...rooms.reserved.map(n => ['reserved', n]),
                            ...rooms.occupied.map(n => ['occupied', n])
                        ];
                    }} else {{
                        roomList = rooms[category].map(n => [category, n]);
                    }}

                    // Generate boxes
                    roomList.forEach(([cls, num]) => {{
                        const box = document.createElement('div');
                        box.classList.add('room-box', cls);
                        box.textContent = num;
                        mainBox.appendChild(box);
                    }});
                }}

                // Show available rooms by default on page load
                showRooms('available');
            </script>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
