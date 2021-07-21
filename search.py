import webbrowser

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

#text = "cricket"

def searchOnGoogle(text):
    
    x = search(text,tld="co.in",num = 1,stop =1,pause = 2.0)
    print(x);
    for j in search(text,tld="co.in",num = 1,stop =1,pause = 2.0):
        webbrowser.open_new_tab(j)

#searchOnGoogle(text)
