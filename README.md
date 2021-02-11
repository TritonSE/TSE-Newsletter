# TSE-Newsletter

[![GitHub last commit](https://img.shields.io/github/last-commit/TritonSE/TSE-Newsletter)](https://github.com/TritonSE/TSE-Newsletter/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg?style=flat)](https://github.com/TritonSE/TSE-Newsletter/pulls)

## Project Description

This project consists of a newsletter template and generator for TSE's own biweekly newsletter. It uses HTML/CSS to create a flexible template that can be customized from newsletter to newsletter. A Python script programatically generates the HTML, abstracting away the hassle of directly editing an HTML file.

## Setup

Dependencies:
- [Python 3.8.3+](https://www.python.org/downloads/)
- [Dominate](https://github.com/Knio/dominate)

Install the dependency inside the project directory.

```
pip install dominate
```

## Running the Project

To generate the HTML and view it in browser.

```
python py/newsletter.py
open newsletter.html
```