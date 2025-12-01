from django.http import HttpResponse

def all_posts(request):
    html = """
    <html>
    <head>
        <title>Mera Blog - Posts</title>
        <style>
            body {font-family: Arial; background: #f8f9fa; padding: 40px; color: #333;}
            .container {max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.1);}
            h1 {text-align:center; color:#28a745;}
            .post {background:#f1f8ff; padding:20px; margin:20px 0; border-left:5px solid #007bff; border-radius:5px;}
            .back {text-align:center; margin-top:40px;}
            .back a {padding:12px 30px; background:#007bff; color:white; text-decoration:none; border-radius:50px;}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Mera Blog - Latest Posts</h1>
            <p style="text-align:center; color:green; font-size:18px;">Sab kuch bilkul theek chal raha hai bhai!</p>

            <div class="post">
                <h2>Pehla Post - Django Sikh Gaya!</h2>
                <p><strong>Author:</strong> Tera Bhai | <strong>Date:</strong> 01 December 2025</p>
                <p>Assalam-o-Alaikum! Aaj maine views.py mein naye functions banaye aur sab run ho gaye. Ab real blog banane ja raha hoon!</p>
            </div>

            <div class="post">
                <h2>Doosra Post - Virtual Environment</h2>
                <p><strong>Author:</strong> Pro Coder | <strong>Date:</strong> 30 November 2025</p>
                <p>venv banana bohot zaroori hai bhai. Aaj ek baar phir yaad dila diya!</p>
            </div>

            <div class="back">
                <a href="/">Home Par Wapas Jao</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)