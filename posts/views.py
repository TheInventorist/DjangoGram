from django.http import HttpResponse
from datetime import datetime

# Create your views here.

posts = [
    {
        'name' : "Mont Blanc",
        'user' : "Yesica lalala",
        'timestamp' : datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
        'picture' : "https://picsum.photos/200/200/?image=1036",
    },
    {
        'name' : "Via lactea",
        'user' : "C. Vander",
        'timestamp' : datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
        'picture' : "https://picsum.photos/200/200/?image=903",
    },
    {
        'name' : "ASDADSaasd",
        'user' : "ASDASDASDasd",
        'timestamp' : datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
        'picture' : "https://picsum.photos/200/200/?image=1076",
    }
]

def listPosts(request):
    #posts = [1,3,5]
    content = []
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i> {timestamp}</i></small></p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))