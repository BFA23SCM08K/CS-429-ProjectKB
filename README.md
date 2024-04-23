# CS429-InformationRetrieval

# Project Report

## Abstract
This project presents the development of an innovative information retrieval system tailored to facilitate efficient web document search and retrieval. The system comprises three primary components: a robust web crawler, an efficient indexer, and a responsive search server. Leveraging state-of-the-art technologies such as Scrapy, Scikit-Learn, and Flask.

Objective:
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
Future Enhancements:
1.	Advancements in Web Crawling:
•	Investigate and implement distributed crawling using scrapyd to facilitate expansive web crawling across multiple servers.
2.	Improvements in Search Indexing:
•	Integrate advanced document representation methods like word2vec to enhance search precision.
•	Apply FAISS for advanced k-Nearest Neighbors (kNN) methods to improve semantic search capabilities.
3.	Enhancements in Query Processing:
•	Implement spell-check and suggestions for queries using NLTK to improve query accuracy.
•	Expand query capabilities with WordNet for a broader and more relevant search.

Project Overview:

System Design:

•	Web Scraping Component: Efficiently scrapes quotes and authors from various sources, saving them into designated files (quotes_page_1 to quotes_page_100) with a set depth limit of 2.
•	Indexing Component: Utilizes TF-IDF scoring to create a structured and efficient inverted index.
•	Query Handling Component: Manages and processes user queries, providing accurate and relevant search results via a Flask application.

Interaction Flow:

1.	Crawler to Indexer Workflow:
•	The Scrapy crawler fetches documents, storing them as text files. These files are subsequently indexed by the Scikit-Learn indexer, which computes TF-IDF scores and constructs the inverted index.
2.	Indexer to Query Processor Workflow:
•	Queries received by the Flask application are processed using the pre-built inverted index to determine document relevance through Cosine similarity, delivering precise search results to the user.

Integration and Architecture:

•	Web Scraping: Managed through crawler.py.

•	Indexing: Handled by indexer.py.

•	Query Processing: Operated via server.py.
