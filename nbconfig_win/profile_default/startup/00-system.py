import os
import sys
import datetime
import time
import pandas as pd
import numpy as np
import pyarrow.parquet as pq
from unittest import TestCase

pd.options.display.max_seq_items = 256
pd.options.display.max_rows = 20
pd.options.display.max_columns = 256
pd.options.display.max_colwidth = 256


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# from IPython.core.display import display, HTML
# display(HTML("<style>.container { width:100% !important; }</style>"))
# print('{} is initialized.'.format(__file__))

print('default profile is loaded')