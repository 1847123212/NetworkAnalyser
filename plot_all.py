#!/usr/bin/env python

import sys
import numpy as np
from matplotlib import pyplot as plt
import pickle

for f in sys.argv[1:]:
    fp = open(f, 'rb')
    raw = pickle.load(fp)
    for att_idx in range(len(raw['atten_vals'])):
	plt.plot(raw['raw'][:, att_idx], label=f+' '+str(raw['atten_vals'][att_idx]))

    fp.close()
    
plt.legend()
plt.show()

