import plotext as plt
                                            #Fullground     #Style       #Background      #Show
plt.colorize("black on white, bold",        "black",        "bold",      "white",         True)
plt.colorize("red on green, italic",        "red",          "italic",    "green",         True)
plt.colorize("yellow on blue, flash",       "yellow",       "flash",     "blue",          True)
plt.colorize("magenta on cyan, underlined", "magenta",      "underline", "cyan",          True)
plt.colorize("integer color codes",         201,            "default",   158,             True)
plt.colorize("RGB color codes",             (16, 100, 200), "default",   (200, 100, 100), True)