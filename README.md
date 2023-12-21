# DEVcember Programming Calendar

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.3.2+-5646ED?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://reflex.dev)
[![NES.css](https://img.shields.io/badge/NES.css-2.3.0-007bff?style=for-the-badge&logo=css3&logoColor=white&labelColor=101010)](https://nostalgic-css.github.io/NES.css)
[![Vercel](https://img.shields.io/badge/Vercel-static-gray?style=for-the-badge&logo=vercel&logoColor=white&labelColor=101010)](https://vercel.com)

## What is it about?

Recently I've been interested in web development with Python. Found a tutorial from [Mouredev](https://github.com/mouredev) in YouTube where he shows how to make a web page with Python and Reflex. The main porpouse of his project is to give away a present every day related to the worl of programming.

I followed the tutorial and develop the web page with a similar format and style. However, I wanted to modify something and not just copy a project, so instead of opening a present each day, a python exercise would be open every day!

#### [Checkout Mouredev's tutorial](https://github.com/mouredev/adeviento-web/tree/main)
#### [Checkout my final project](https://advent-py.vercel.app/)

## Project

The structure of the project is as follows

* **advent_py**: main codebase
	* **advent_py.py**: web site index
	* **constants.py**: global constants
	* **styles**: styles directory (css, colors and fonts)
	* **views**: views directory (graphical sections)
	* **components**: components directory (graphic elements with less entity than a view)
* **assets**: graphic resources and JavaScript utilities (snow and countdown)
* **rxconfig.py**: main project configuration (set by default with reflex)
* **requirements.txt**: project dependencies
* **build.sh**: script to generate the static web to deploy it to production
* **[created] public**: static package of the project that would be deployed to production (HTML, CSS, JS and images)

## Configuration

1. `Fork` the repository
2. Clone this forked repo into your local machine. I recommend using SSH:
   ```bash
   git clone git@github.com:<USERNAME>/advent-py.git
   ```
3. Go to the project root directory
   ```bash
   cd advent-py
   ```
4. Create a virtual environment and activate it
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
5. Install the project dependencies
   ```bash
   pip install -r requirements.txt
   ```
6. Initialize Reflex project
   ```bash
   reflex init
   ```
7. Run the project in your local machine
    ```bash
    reflex run
    ```
   It will prompt the ip link where the project is deployed. Click it directly or type in your browser `http://localhost:3000/`

## Resources

![Python](https://img.shields.io/github/stars/python/cpython?label=Python&style=social)
![Reflex](https://img.shields.io/github/stars/reflex-dev/reflex?label=Reflex&style=social)
![NES.css](https://img.shields.io/github/stars/nostalgic-css/NES.css?label=NES.css&style=social)
![Vercel](https://img.shields.io/github/stars/vercel/vercel?label=Vercel&style=social)

* Language: [Python](https://www.python.org/)
* Framework: [Reflex](https://reflex.dev/)
* CSS: [NES.css](https://nostalgic-css.github.io/NES.css/)
* Font: [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P)
* Hosting: [Vercel](https://vercel.com/)

### Visit my GitHub profile for more projects 🚀

[![Web](https://img.shields.io/badge/GitHub-Dimanu.py-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/dimanu-py)
