from flask import Flask, send_from_directory, request
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# =========================
# IMAGES
# =========================

@app.route("/ai.jpg")
def ai_image():
    return send_from_directory(BASE_DIR, "ai.jpg")


@app.route("/robot.jpg")
def robot_image():
    return send_from_directory(BASE_DIR, "robot.jpg")


@app.route("/software.jpg")
def software_image():
    return send_from_directory(BASE_DIR, "software.jpg")


# =========================
# COMMON DESIGN
# =========================

def page(title, content):

    return f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{title} | Mayank TechLab</title>

    <style>

        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f2f4f7;
            color: #222;
        }}

        /* LEFT SIDEBAR */

        .sidebar {{
            position: fixed;
            left: 0;
            top: 0;
            width: 230px;
            height: 100vh;
            background: #202020;
            color: white;
            padding: 25px 15px;
            overflow-y: auto;
        }}

        .logo {{
            text-align: center;
            margin-bottom: 30px;
        }}

        .logo h1 {{
            font-size: 24px;
            margin: 0;
        }}

        .logo p {{
            font-size: 13px;
            color: #bbbbbb;
        }}

        .menu a {{
            display: block;
            color: white;
            text-decoration: none;
            padding: 13px 15px;
            margin: 5px 0;
            border-radius: 8px;
            font-size: 16px;
        }}

        .menu a:hover {{
            background: #3b3b3b;
        }}

        /* MAIN AREA */

        .main {{
            margin-left: 230px;
            min-height: 100vh;
        }}

        header {{
            background: #171717;
            color: white;
            padding: 35px 20px;
            text-align: center;
        }}

        header h1 {{
            margin: 0;
            font-size: 36px;
        }}

        header p {{
            margin-top: 10px;
            font-size: 17px;
        }}

        .container {{
            width: 90%;
            max-width: 1100px;
            margin: 30px auto;
        }}

        .hero {{
            background: white;
            padding: 40px 25px;
            text-align: center;
            border-radius: 15px;
        }}

        .hero h2 {{
            font-size: 30px;
            margin-top: 0;
        }}

        .hero p {{
            line-height: 1.7;
        }}

        .button {{
            display: inline-block;
            background: #1677ff;
            color: white;
            text-decoration: none;
            padding: 12px 20px;
            border-radius: 8px;
            margin-top: 15px;
        }}

        .button:hover {{
            background: #005dcc;
        }}

        .cards {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-top: 30px;
        }}

        .card {{
            background: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
        }}

        .card img {{
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-radius: 10px;
        }}

        .card h3 {{
            margin-top: 18px;
        }}

        .card p {{
            line-height: 1.6;
        }}

        .section {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 20px;
        }}

        .section h2 {{
            margin-top: 0;
        }}

        .list {{
            line-height: 2;
        }}

        .download-box {{
            background: white;
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 20px;
        }}

        .download-box h3 {{
            margin-top: 0;
        }}

        input, textarea {{
            width: 100%;
            padding: 12px;
            margin: 8px 0 15px;
            border: 1px solid #ccc;
            border-radius: 7px;
            font-size: 15px;
        }}

        textarea {{
            height: 140px;
            resize: vertical;
        }}

        button {{
            background: #1677ff;
            color: white;
            border: none;
            padding: 12px 22px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 15px;
        }}

        footer {{
            margin-top: 50px;
            background: #171717;
            color: white;
            text-align: center;
            padding: 25px;
        }}

        /* MOBILE */

        @media (max-width: 800px) {{

            .sidebar {{
                position: relative;
                width: 100%;
                height: auto;
            }}

            .main {{
                margin-left: 0;
            }}

            .cards {{
                grid-template-columns: 1fr;
            }}

            .menu a {{
                display: block;
                text-align: left;
            }}

        }}

    </style>
</head>

<body>

<!-- LEFT MENU -->

<div class="sidebar">

    <div class="logo">
        <h1>Mayank TechLab</h1>
        <p>Technology Website</p>
    </div>

    <div class="menu">

        <a href="/">🏠 Home</a>

        <a href="/software">💻 Software</a>

        <a href="/ai">🤖 AI</a>

        <a href="/robotics">🦾 Robotics</a>

        <a href="/tech-tips">📱 Tech Tips</a>

        <a href="/articles">📝 Articles</a>

        <a href="/downloads">⬇️ Downloads</a>

        <a href="/about">👤 About</a>

        <a href="/contact">📩 Contact</a>

    </div>

</div>


<!-- MAIN WEBSITE -->

<div class="main">

<header>

    <h1>Mayank TechLab</h1>

    <p>
        Technology • Python • AI • Software • Robotics
    </p>

</header>


<div class="container">

{content}

</div>


<footer>

    <p>© 2026 Mayank TechLab</p>

    <p>Made with Python & Flask</p>

</footer>

</div>

</body>
</html>
"""


# =========================
# HOME
# =========================

@app.route("/")
def home():

    content = """

    <div class="hero">

        <h2>Welcome to Mayank TechLab 🚀</h2>

        <p>
            नमस्ते! मेरा नाम Mayank Sahu है।
        </p>

        <p>
            Mayank TechLab एक Technology Website है,
            जहाँ Python, Software, AI, Robotics और
            Technology से जुड़ी जानकारी मिलेगी।
        </p>

        <a class="button" href="/about">
            मेरे बारे में जानें
        </a>

    </div>


    <div class="cards">

        <div class="card">

            <img src="/software.jpg">

            <h3>💻 Software</h3>

            <p>
                Software, Programming और Computer से
                जुड़ी useful जानकारी।
            </p>

            <a class="button" href="/software">
                Open
            </a>

        </div>


        <div class="card">

            <img src="/ai.jpg">

            <h3>🤖 Artificial Intelligence</h3>

            <p>
                AI, Machine Learning और AI Tools
                के बारे में आसान जानकारी।
            </p>

            <a class="button" href="/ai">
                Open
            </a>

        </div>


        <div class="card">

            <img src="/robot.jpg">

            <h3>🦾 Robotics</h3>

            <p>
                Robotics, Sensors, Arduino और
                Projects की जानकारी।
            </p>

            <a class="button" href="/robotics">
                Open
            </a>

        </div>

    </div>


    <div class="section">

        <h2>🌟 इस Website पर क्या मिलेगा?</h2>

        <ul class="list">

            <li>Python और Programming</li>
            <li>Software और Computer Tips</li>
            <li>Artificial Intelligence</li>
            <li>Robotics</li>
            <li>Technology Articles</li>
            <li>Useful Downloads</li>
            <li>Tech Tips</li>

        </ul>

    </div>

    """

    return page("Home", content)


# =========================
# SOFTWARE
# =========================

@app.route("/software")
def software():

    content = """

    <div class="section">

        <h2>💻 Software</h2>

        <p>
            यहाँ Software और Programming से जुड़ी
            जानकारी मिलेगी।
        </p>

        <h3>Topics</h3>

        <ul class="list">

            <li>Python Programming</li>
            <li>Windows Tips</li>
            <li>Computer Basics</li>
            <li>Programming Projects</li>
            <li>Useful Software</li>

        </ul>

    </div>

    """

    return page("Software", content)


# =========================
# AI
# =========================

@app.route("/ai")
def ai():

    content = """

    <div class="section">

        <h2>🤖 Artificial Intelligence</h2>

        <p>
            AI यानी Artificial Intelligence technology
            computers को intelligent tasks करने में मदद करती है।
        </p>

        <h3>AI Topics</h3>

        <ul class="list">

            <li>AI Basics</li>
            <li>Machine Learning</li>
            <li>AI Tools</li>
            <li>AI Projects</li>
            <li>Python for AI</li>

        </ul>

    </div>

    """

    return page("AI", content)


# =========================
# ROBOTICS
# =========================

@app.route("/robotics")
def robotics():

    content = """

    <div class="section">

        <h2>🦾 Robotics</h2>

        <p>
            Robotics में programming, electronics,
            sensors और mechanical systems का उपयोग होता है।
        </p>

        <h3>Robotics Topics</h3>

        <ul class="list">

            <li>Arduino</li>
            <li>Sensors</li>
            <li>Robotics Programming</li>
            <li>Robot Projects</li>
            <li>Automation</li>

        </ul>

    </div>

    """

    return page("Robotics", content)


# =========================
# TECH TIPS
# =========================

@app.route("/tech-tips")
def tech_tips():

    content = """

    <div class="section">

        <h2>📱 Tech Tips</h2>

        <p>
            रोजमर्रा की technology और computer से जुड़े
            आसान tips यहाँ मिलेंगे।
        </p>

        <ul class="list">

            <li>Windows Shortcuts</li>
            <li>Computer Tips</li>
            <li>Phone Tips</li>
            <li>Browser Tips</li>
            <li>Programming Tips</li>

        </ul>

    </div>

    """

    return page("Tech Tips", content)


# =========================
# ARTICLES
# =========================

@app.route("/articles")
def articles():

    content = """

    <div class="section">

        <h2>📝 Articles</h2>

        <p>
            यहाँ Technology से जुड़े articles
            और tutorials प्रकाशित किए जाएंगे।
        </p>

    </div>


    <div class="cards">

        <div class="card">

            <h3>🐍 Python क्या है?</h3>

            <p>
                Python programming language की basic जानकारी।
            </p>

        </div>


        <div class="card">

            <h3>🤖 AI क्या है?</h3>

            <p>
                Artificial Intelligence को आसान भाषा में समझें।
            </p>

        </div>


        <div class="card">

            <h3>💻 Software क्या होता है?</h3>

            <p>
                Software और computer programs की basic जानकारी।
            </p>

        </div>

    </div>

    """

    return page("Articles", content)


# =========================
# DOWNLOADS
# =========================

@app.route("/downloads")
def downloads():

    content = """

    <div class="section">

        <h2>⬇️ Downloads</h2>

        <p>
            यहाँ Mayank TechLab के useful apps,
            projects और resources के download links होंगे।
        </p>

    </div>


    <div class="download-box">

        <h3>🧮 Mayank Calculator</h3>

        <p>
            Python से बनाया गया हमारा calculator app।
        </p>

        <p>
            <b>Status:</b> Coming Soon
        </p>

    </div>


    <div class="download-box">

        <h3>🐍 Python Projects</h3>

        <p>
            Future में यहाँ छोटे Python projects
            और learning files उपलब्ध होंगी।
        </p>

        <p>
            <b>Status:</b> Coming Soon
        </p>

    </div>

    """

    return page("Downloads", content)


# =========================
# ABOUT
# =========================

@app.route("/about")
def about():

    content = """

    <div class="section">

        <h2>👤 About Mayank TechLab</h2>

        <p>
            मेरा नाम Mayank Sahu है।
        </p>

        <p>
            Mayank TechLab मेरी Technology Website है।
            इस website पर Python, Software, AI,
            Robotics और Technology से जुड़ी जानकारी
            उपलब्ध कराने का उद्देश्य है।
        </p>

        <h3>🛠️ Website Technology</h3>

        <ul class="list">

            <li>Python</li>
            <li>Flask</li>
            <li>HTML</li>
            <li>CSS</li>

        </ul>

        <h3>🎯 हमारा उद्देश्य</h3>

        <p>
            Technology और Programming को आसान भाषा में
            समझाना और useful resources उपलब्ध कराना।
        </p>

    </div>

    """

    return page("About", content)


# =========================
# CONTACT
# =========================

@app.route("/contact", methods=["GET", "POST"])
def contact():

    message = ""

    if request.method == "POST":

        name = request.form.get("name", "")

        message = f"""

        <div class="section">

            <h2>✅ Message Received</h2>

            <p>
                धन्यवाद {name}!
            </p>

            <p>
                आपका message प्राप्त हुआ।
            </p>

            <p>
                अभी यह demo contact system है।
            </p>

        </div>

        """

    content = f"""

    {message}

    <div class="section">

        <h2>📩 Contact Us</h2>

        <p>
            कोई सवाल या suggestion है तो नीचे form भरें।
        </p>

        <form method="POST">

            <label>Name</label>

            <input
                type="text"
                name="name"
                placeholder="अपना नाम लिखें"
                required
            >


            <label>Email</label>

            <input
                type="email"
                name="email"
                placeholder="अपना email लिखें"
                required
            >


            <label>Message</label>

            <textarea
                name="message"
                placeholder="अपना message लिखें"
                required
            ></textarea>


            <button type="submit">
                Send Message
            </button>

        </form>

    </div>

    """

    return page("Contact", content)


# =========================
# RUN
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
