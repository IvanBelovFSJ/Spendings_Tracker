# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 02:48:55 2019

@author: Ivan
"""

  # This program displays a simple line graph.
import matplotlib.pyplot as plt
  
def main():
      # Create lists with the X,Y coordinates of each data point.
      x_coords = [0, 1, 2, 3, 4]
      y_coords = [1, 4, 4, 3, 2]
      
      # Build the line graph.
      plt.plot(x_coords, y_coords, marker='o')
 
     # Add a title.
      plt.title('Spendings by Year')
 
     # Add labels to the axes.
      plt.xlabel('Year')
      plt.ylabel('Spendings')
     # Customize the tick marks.
      plt.xticks([0, 1, 2, 3, 4, 5],
                ['2015','2016', '2017', '2018', '2019', '2020'])
      plt.yticks([0, 1, 2, 3, 4],
                ['$0k','$10k', '$20k', '$25k', '$30k'])
 
     # Add a grid.
      plt.grid(True)
 
     # Display the line graph.
      plt.show()
 
 # Call the main function.
main()