# TSE-Newsletter

## Project Description

This project consists of a newsletter template for TSE's own biweekly newsletter. It uses HTML/CSS to create a flexible template that can be customized from newsletter to newsletter.

The project also uses a script to generate the HTML files using the [Dominate library](https://github.com/Knio/dominate).

## Run Project and Setup Environment
### Setup
Dependencies:
- Python3 and pip
- Dominate

Install [Python3] (https://www.python.org/downloads/)

Clone the repository and install dependency.
```
git clone https://github.com/TritonSE/TSE-Newsletter.git
cd TSE-Newsletter
pip install dominate
```

### Running the Project

To generate the HTML and view it in browser.
```
python py/newsletter.py
open newsletter.html
```