import time
import webbrowser

count = 0

while count < 3:
    count = count + 1
    time.sleep(2)
    webbrowser.open("https://de.wikipedia.org/wiki/%C3%9Cberwachtes_Lernen")
    print("Webbrowser #" + str(count) + " opened at time " + time.ctime())

print("Done.")
