import json
import sys
import numpy as np
import matplotlib.pyplot as plt


input_file_name = sys.argv[1]

with open(input_file_name, 'r') as json_input:
  data = json.load(json_input)

#data = json.load(json_input)

iterations = np.arange(0,len(data[1]["global_error_history"]))
global_error_history = data[1]["global_error_history"]

plt.plot(iterations,global_error_history)
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.axis([0,iterations[-1],0,1.1*np.max(global_error_history)])
#plt.axis([0,len(iterations),0,np.max(global_error_history)])
plt.show()
