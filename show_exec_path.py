# copy this in streamlit app to get exec.path

import os
import sys

########################################################################
# Code to get exec path information for this app
########################################################################
# Get the path of the Python executable
python_executable = sys.executable
# Get the path of the currently running script
script_path = os.path.abspath(__file__)

full_command = f"{python_executable} -m streamlit run {script_path}"  # for streamlit apps
# full_command = f"{python_executable} {script_path}"  # for python apps
#######################################################################
#######################################################################

print(full_command) # use in normal py script
# st.write(full_command) # use in streamlit app