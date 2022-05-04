import matplotlib.pyplot as plt
# Prepare table
columns = ('A', 'B', 'C', 'D', 'E')
rows = ["A", "B"]
cell_text = [["1", "1","1","1","1"], ["2","2","2","2","2"]]
# Add a table at the bottom of the axes
colors = [["#56b5fd","w","w","w","w"],[ "#1ac3f5","w","w","w","w"]]

fig, ax = plt.subplots()
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=cell_text,cellColours=colors,
                     colLabels=columns,loc='center')

plt.show()