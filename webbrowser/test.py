import webbrowser

if __name__=='__main__':
    print(webbrowser._browsers)
    
    webbrowser.open_new('http://www.google.com')

'''
import webbrowser

url = 'https://pythonexamples.org'
webbrowser.register('firefox',
	None,
	webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
webbrowser.get('firefox').open(url)
'''