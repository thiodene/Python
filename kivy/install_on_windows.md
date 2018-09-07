# Source: https://kivy.org/doc/stable/installation/installation-windows.html

# Installation follow step by step:
# Now that python is installed, open the Command line and make sure python is available by typing python --version. 
# Then, do the following to install.

# 1. Ensure you have the latest pip and wheel:
python -m pip install --upgrade pip wheel setuptools

# 2. Install the dependencies (skip gstreamer (~120MB) if not needed, see Kivy’s dependencies):
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer

# Install kivy:
python -m pip install kivy

# (Optionally) Install the kivy examples:
python -m pip install kivy_examples

# The examples are installed in the share directory under the root directory where python is installed.
# That’s it. You should now be able to import kivy in python or run a basic example if you installed the kivy examples:
python share\kivy-examples\demo\showcase\main.py
