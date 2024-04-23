# CS429-InformationRetrieval

# Project Report

## Abstract
This project presents the development of an innovative information retrieval system tailored to facilitate efficient web document search and retrieval. The system comprises three primary components: a robust web crawler, an efficient indexer, and a responsive search server. Leveraging state-of-the-art technologies such as Scrapy, Scikit-Learn, and Flask.

### Objective:
1.	Web Crawling Using Scrapy:
•	Develop a web crawler utilizing Scrapy to retrieve web documents in HTML format.
•	Configure the crawler to start from a specified seed URL/domain, with controls for maximum pages to crawl and the depth of navigation.
•	Enhance efficiency with concurrent crawling capabilities, employing Scrapy's AutoThrottle feature to regulate the crawling speed.
2.	Document Indexing with Scikit-Learn:
•	Create an indexing system using Scikit-Learn to build an inverted index stored in pickle format.
•	Calculate TF-IDF values for effective document representation and use Cosine similarity for assessing document relevance.
3.	Query Management with Flask:
•	Construct a Flask application to process textual queries in JSON format.
•	Ensure rigorous validation and error-checking of incoming queries and deliver the most relevant top-K results from the indexed documents.

### Future Enhancements:
1.	Advancements in Web Crawling:
•	Investigate and implement distributed crawling using scrapyd to facilitate expansive web crawling across multiple servers.
2.	Improvements in Search Indexing:
•	Integrate advanced document representation methods like word2vec to enhance search precision.
•	Apply FAISS for advanced k-Nearest Neighbors (kNN) methods to improve semantic search capabilities.
3.	Enhancements in Query Processing:
•	Implement spell-check and suggestions for queries using NLTK to improve query accuracy.
•	Expand query capabilities with WordNet for a broader and more relevant search.

## Project Overview:

### System Design:

•	Web Scraping Component: Efficiently scrapes quotes and authors from various sources, saving them into designated files (quotes_page_1 to quotes_page_100) with a set depth limit of 2.
•	Indexing Component: Utilizes TF-IDF scoring to create a structured and efficient inverted index.
•	Query Handling Component: Manages and processes user queries, providing accurate and relevant search results via a Flask application.

### Interaction Flow:

1.	Crawler to Indexer Workflow:
•	The Scrapy crawler fetches documents, storing them as text files. These files are subsequently indexed by the Scikit-Learn indexer, which computes TF-IDF scores and constructs the inverted index.
2.	Indexer to Query Processor Workflow:
•	Queries received by the Flask application are processed using the pre-built inverted index to determine document relevance through Cosine similarity, delivering precise search results to the user.

### Integration and Architecture:

•	Web Scraping: Managed through crawler.py.

•	Indexing: Handled by indexer.py.

•	Query Processing: Operated via server.py.

### Relevant Literature:

"Information Retrieval" by Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze provides foundational concepts.

Official Scrapy and Scikit-Learn documentation for detailed guidance on technical implementations.

### Interfaces

- Web Interface
- RESTful API

### Implementation

- Python for backend development
- Scrapy for web scraping
- Scikit-Learn for TF-IDF calculations
- Flask for web server and API

## Operation

### Commands
#### Note: See to it that you are in correct directory inorder to run the code. The modules are present inside the goodreads_quotes folder.
- `python crawler.py`: Run the web scraping module 
- `python indexer.py`: Run the indexer 
- `python processor.py`: Run the Flask server

# Project API Usage Guide

## Introduction
This guide provides detailed instructions on how to interact with the Flask server using `curl` commands for querying processed data. It includes steps to run the Flask application and sample commands to send queries to the server.

## Getting Started

### Starting the Server
- **Run the Flask Application**:
  Execute the file `server.py` to start the query processing module and initiate the Flask server:


## Sending Queries

### Basic Query
Send a basic query to the Flask server using the following `curl` command:
```bash
curl -X POST "http://localhost:5000/search" -H "Content-Type: application/json" -d "{\"query\":\"API\"}"

# Installation Guide

## Prerequisites

Before installation, ensure you have the following requirements:

- Python 3.10 or newer
- pip (Python package installer)

## Installation Instructions

Follow these detailed steps to set up the project environment:

### 1. Install Python

Download and install the latest version of Python from the [Python Official Website](https://www.python.org).

### 2. Install Scrapy

Install Scrapy using pip. Open your terminal or command prompt and run:

```bash
pip install scrapy

### 3. Install Scikit-Learn

pip install scikit-learn

### 4. Install Flask

pip install Flask

```
### Project Conclusion

The initiative has led to the successful development of a basic search engine focused on quotes. It efficiently processes simple search queries but demonstrates potential areas for further development, especially in scalability and search result accuracy. Future enhancements will focus on integrating advanced search algorithms, refining the user interface, and optimizing system performance for better overall efficiency.

## Data Sources

- Stackover Flow: [Link](https://stackoverflow.com/questions/tagged/api)
- Mozilla: [Link](https://developer.mozilla.org/en-US/docs/Web/API)

## Test Cases
-  This is positive test case where the query is found and returns a similarity score
  `curl -v -X POST http://localhost:5000/search -H "Content-Type: application/json" -d "{\"query\":\"test query\"}"`
![image](https://github.com/BFA23SCM08K/CS-429-ProjectKB/assets/112521349/aad755fb-23e3-481f-8f4c-1cd7791892f9)

## Source Code

- All source code files are available in the project repository
- Documentation is included in the `README.md` file
- Open-source dependencies are listed in `requirements.txt` and are needed to be installed for the files to run.

## Bibliography
1.	Scrapinghub Ltd. "Scrapy - A Fast and Powerful Scraping and Web Crawling Framework." https://scrapy.org/. 
2.	Pedregosa, F. et al. "Scikit-learn: Machine Learning in Python." Journal of Machine Learning Research, vol. 12, pp. 2825-2830, 2011. 
3.	Ronacher, A. "Flask: A Python Microframework." https://flask.palletsprojects.com/.
4.	Visual Studio Code Documentation. "Visual Studio Code - Code Editing. Redefined." https://code.visualstudio.com/docs. 
5.	Microsoft. "Visual Studio Code - Code Editing. Redefined." https://code.visualstudio.com/.
6.	Python Software Foundation. "Welcome to Python.org." https://www.python.org/. 
7.	van Rossum, Guido, and Drake, Fred L. "Python 3 Reference Manual." CreateSpace Independent Publishing Platform, 2009.
8.	Daniel Stenberg. "cURL - command line tool and library for transferring data with URLs." https://curl.se/. 
9.	Stenberg, D. "Everything curl: The book." Daniel Stenberg, 2019.
10.	https://chat.openai.com/c/dacd1
11.	https://gemini.google.com/app/d7ac57a59f7d3254



 




