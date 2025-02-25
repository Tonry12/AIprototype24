from flask import Flask, render_template, request, render_template_string, jsonify
import random
import json


app = Flask(__name__)

@app.route("/") 
def helloworld():
    return "Hello, World!"

@app.route("/stat") 
def helloSTAT():
    return "Hello, STAT KKU!"

@app.route("/research")
def research_page():
    faculty_research = {
    "Dr. Alice Smith": [
        "สภาพอากาศ Statistical Modeling of Climate Change Impacts",
        "อนุกรมเวลา Advanced Methods in Time Series Analysis",
        "การเรียนรู้ของเครื่อง Machine Learning Applications in Biostatistics",
    ],
    "Dr. Bob Johnson": [
        "Bayesian Inference in Social Sciences",
        "Quantitative Analysis of Economic Trends",
        "Development of Robust Statistical Software",
    ],
    "Dr. Carol Davis": [
        "Optimization Techniques in Big Data Analytics",
        "Statistical Approaches to Epidemiology",
        "Survey Data Analysis for Policy Decisions",
    ],
    }

    faculty, research_projects = random.choice(list(faculty_research.items()))
    
    return render_template("research.html", faculty=faculty, research_projects=research_projects)

##api
# @app.route('/simpleAPI',methods=['POST'])
# def web_service_API():

#     payload = request.data.decode("utf-8")
#     inmessage = json.loads(payload)

#     print(inmessage)
    
#     json_data = json.dumps({'y': 'received!'})
#     return json_data

@app.route('/simpleAPI', methods=['POST'])
def simpleAPI():
    try:
        # Receive data from the request
        payload = request.data.decode("utf-8")
        inmessage = json.loads(payload)

        # Log received data
        print("\n[INFO] Received data from user:")
        print(f"----------------------------")
        print(f"Message: {inmessage.get('msg')}")
        print(f"Sender: {inmessage.get('sender')}")
        print(f"Recipient: {inmessage.get('recipient')}")
        print(f"Recipient's IP: {inmessage.get('ip')}")
        print(f"----------------------------\n")

        # Create response data
        json_data = json.dumps({'response': 'received!'})

        # Send response back
        return json_data, 200  # Return HTTP Status 200 to indicate success

    except Exception as e:
        # Handle any errors
        error_message = f"[ERROR] Exception: {str(e)}"
        print(error_message)

        # Send error response
        return jsonify({'error': 'An error occurred while processing the data'}), 400


@app.route("/contact",methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        user_email = request.form.get("email")
        with open("email.txt", "a") as myfile:
            myfile.write(f'{user_email} \n')
        return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contact Us</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f9f9f9;
                    color: #333;
                }
                header {
                    background-color: #0078d7;
                    color: white;
                    text-align: center;
                    padding: 1rem 0;
                }
                main {
                    padding: 2rem;
                    max-width: 600px;
                    margin: auto;
                    text-align: left;
                    background: white;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }
                h1 {
                    color: #005ea6;
                }
                p {
                    line-height: 1.6;
                }
                footer {
                    text-align: center;
                    margin-top: 2rem;
                    font-size: 0.9rem;
                    color: #666;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Contact Us</h1>
            </header>
            <main>
                <h2><a href="/statHTML">Admin</a> Contact Details</h2>
                <p><strong>Name:</strong> John Doe</p>
                <p><strong>Email:</strong> admin@example.com</p>
                <p><strong>Phone:</strong> +1-234-567-890</p>
                <p>If you have any questions or need assistance, please don’t hesitate to reach out. Our admin is here to help you!</p>
                <h2>Thank you {{user}}</h2>
            </main>
            <footer>
                <p>&copy; 2025 Stat KKU. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """,user=user_email)
    else:
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contact Us</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f9f9f9;
                    color: #333;
                }
                header {
                    background-color: #0078d7;
                    color: white;
                    text-align: center;
                    padding: 1rem 0;
                }
                main {
                    padding: 2rem;
                    max-width: 600px;
                    margin: auto;
                    text-align: left;
                    background: white;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }
                h1 {
                    color: #005ea6;
                }
                p {
                    line-height: 1.6;
                }
                footer {
                    text-align: center;
                    margin-top: 2rem;
                    font-size: 0.9rem;
                    color: #666;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Contact Us</h1>
            </header>
            <main>
                <h2><a href="/statHTML">Admin</a> Contact Details</h2>
                <p><strong>Name:</strong> John Doe</p>
                <p><strong>Email:</strong> admin@example.com</p>
                <p><strong>Phone:</strong> +1-234-567-890</p>
                <p>If you have any questions or need assistance, please don’t hesitate to reach out. Our admin is here to help you!</p>
                <h2>Submit Your Email So We Can Contact You Back</h2>
                <form method="POST">
                    <label for="email">Your Email:</label>
                    <input type="email" id="email" name="email" required placeholder="Enter your email">
                    <button type="submit">Submit</button>
                </form>
            </main>
            <footer>
                <p>&copy; 2025 Stat KKU. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """

@app.route("/statHTML") 
def helloSTAThtml():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Stat KKU - Homepage</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }
            header {
                background-color: #0078d7;
                color: white;
                padding: 1.5rem 0;
                text-align: center;
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
            }
            nav {
                background-color: #005ea6;
                display: flex;
                justify-content: center;
                padding: 1rem;
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 1rem;
                font-weight: bold;
                transition: color 0.3s;
            }
            nav a:hover {
                color: #ffdd57;
            }
            main {
                padding: 2rem;
                text-align: center;
            }
            main section {
                margin-bottom: 2rem;
                background: #fff;
                padding: 1.5rem;
                box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
            }
            footer {
                background-color: #0078d7;
                color: white;
                text-align: center;
                padding: 1rem 0;
                position: fixed;
                bottom: 0;
                width: 100%;
                box-shadow: 0px -2px 5px rgba(0, 0, 0, 0.2);
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to Stat KKU</h1>
            <p>Department of Statistics, Khon Kaen University</p>
        </header>
        <nav>
            <a href="#about">About Us</a>
            <a href="#programs">Programs</a>
            <a href="/research">Research</a>
            <a href="/contact">Contact</a>
        </nav>
        <main>
            <section id="about">
                <h2>About Us</h2>
                <p>The Department of Statistics at Khon Kaen University is dedicated to excellence in teaching and research in the field of statistics.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus vehicula arcu id ligula vehicula, ac tincidunt mauris aliquet. Nulla facilisi. Cras et varius erat, nec luctus orci.</p>
    <p>Donec convallis lacus eget suscipit ullamcorper. Curabitur luctus ante in vestibulum egestas. Proin non dui nec erat fermentum euismod. Aenean a tincidunt augue, in eleifend orci.</p>
    <p>Suspendisse potenti. Integer non felis ac eros congue pellentesque. Nunc sit amet bibendum nisi, a ultricies elit. Sed id facilisis mauris, id consequat justo.</p>
    <p>Maecenas feugiat velit ut libero vulputate, a tincidunt elit blandit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.</p>
    <p>Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aliquam a tincidunt libero, nec viverra tortor. Suspendisse sit amet luctus ligula.</p>
    <p>Curabitur eget nisi vitae eros vulputate efficitur vel sit amet elit. Phasellus id nisl ut ligula convallis pharetra. Donec lacinia eros a lectus pulvinar, eget varius risus tincidunt.</p>
    <p>Praesent vitae tortor eget augue congue dapibus. Etiam at fermentum turpis, non fringilla ex. Vestibulum tristique libero a urna tincidunt suscipit.</p>
    <p>Integer ut urna non ipsum gravida feugiat. Aliquam a consequat ligula. Proin et sapien a nisi faucibus fringilla non in nunc. Vivamus vel turpis eget lacus mollis viverra.</p>
    <p>Nulla facilisi. Nam et justo eget quam lacinia bibendum. Etiam id arcu sit amet nisl dapibus convallis. Suspendisse potenti.</p>
    <p>Fusce ut est risus. Nunc consequat mauris euismod ligula blandit, vel posuere tortor rhoncus. Sed convallis, turpis at sodales aliquam, lorem nisl malesuada erat, non varius magna sapien ac libero.</p>
            </section>
            <section id="programs">
                <h2>Programs</h2>
                <p>We offer undergraduate and postgraduate programs in statistics to prepare students for successful careers.</p>
            </section>
            <section id="research">
                <h2>Research</h2>
                <p>Our faculty members are engaged in cutting-edge research to address real-world challenges using statistical methods.</p>
            </section>
        </main>
        <footer>
            <p>&copy; 2025 Stat KKU. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":   
    app.run(host='0.0.0.0', port=5000)