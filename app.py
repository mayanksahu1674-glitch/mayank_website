from flask import Flask, send_from_directory
app = Flask(__name__)
@app.route("/ai.jpg")
def ai_image():
    return send_from_directory(".", "ai.jpg")

@app.route("/robot.jpg")
def robot_image():
    return send_from_directory(".", "robot.jpg")

@app.route("/software.jpg")
def software_image():
    return send_from_directory(".", "software.jpg")

app = Flask(__name__)
print(app.static_folder)

@app.route("/")
def home():

    return """
<!DOCTYPE html>

<html>

<head>

    <title>Mayank techlab.com</title>

    <style>

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            color: #222;
        }

        header {
            background-color: #202020;
            color: white;
            padding: 35px 20px;
            text-align: center;
        }

        header h1 {
            margin: 0;
            font-size: 38px;
        }

        header p {
            font-size: 18px;
        }

        nav {
            background-color: #333;
            padding: 15px;
            text-align: center;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
        }

        .container {
            width: 85%;
            max-width: 1100px;
            margin: 30px auto;
        }

        .welcome {
            background-color: white;
            padding: 30px;
            border-radius: 12px;
            text-align: center;
        }

        .cards {
            display: flex;
            gap: 20px;
            margin-top: 30px;
        }

        .card {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            flex: 1;
            text-align: center;
        }

        .card img {
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-radius: 10px;
        }

        .card h2 {
            margin-top: 20px;
        }

        .card p {
            line-height: 1.6;
        }

        .about {
            background-color: white;
            margin-top: 30px;
            padding: 30px;
            border-radius: 12px;
        }

        footer {
            margin-top: 40px;
            background-color: #202020;
            color: white;
            text-align: center;
            padding: 25px;
        }

        @media (max-width: 800px) {

            .cards {
                flex-direction: column;
            }

        }

    </style>

</head>


<body>


<header>

    <h1>Mayank Sahu</h1>

    <p>
        Technology • AI • Software • Robotics
    </p>

</header>


<nav>

    <a href="/">Home</a>

    <a href="#software">
        Software Tips
    </a>

    <a href="#ai">
        AI Tips
    </a>

    <a href="#robotics">
        Robotics
    </a>

    <a href="#about">
        About
    </a>

</nav>


<div class="container">


    <div class="welcome">

        <h2>
            Welcome to My Website
        </h2>

        <p>
            नमस्ते! मेरा नाम Mayank Sahu है।
        </p>

        <p>
            यह मेरी छोटी-सी Technology Website है।
        </p>

    </div>


    <div class="cards">


        <div class="card" id="software">

            <img src="/software.jpg">

            <h2>
                💻 Software Engineer Tips
            </h2>

            <p>
                Programming सीखते समय रोज थोड़ा code लिखें।
            </p>

            <p>
                छोटे projects बनाएं और problems को खुद solve करें।
            </p>

        </div>


        <div class="card" id="ai">

            <img src="/ai.jpg">

            <h2>
                🤖 AI Engineer Tips
            </h2>

            <p>
                Python और Mathematics की basic knowledge मजबूत करें।
            </p>

            <p>
                Machine Learning और AI के concepts धीरे-धीरे सीखें।
            </p>

        </div>


        <div class="card" id="robotics">

            <img src="/robot.jpg">

            <h2>
                🦾 Robotics
            </h2>

            <p>
                Robotics में programming, sensors और electronics
                का इस्तेमाल होता है।
            </p>

            <p>
                छोटे projects से robotics सीखना शुरू करें।
            </p>

        </div>


    </div>


    <div class="about" id="about">

        <h2>
            About Mayank Sahu
        </h2>

        <p>
            मेरा नाम Mayank Sahu है।
            मुझे Technology, Python, AI, Software और Robotics
            जैसी चीजों में interest है।
        </p>

        <p>
            यह website मैंने Python और Flask का इस्तेमाल करके बनाई है।
        </p>

    </div>


</div>


<footer>

    <p>
        © 2026 Mayank Sahu
    </p>

</footer>


</body>

</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)