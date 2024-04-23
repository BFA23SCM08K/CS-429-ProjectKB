from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

class Indexer:
    def __init__(self):
        # Adjusted max_df and min_df
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=1500, ngram_range=(1, 3), min_df=1, max_df=2)

    def create_index(self, docs):
        self.tfidf_matrix = self.vectorizer.fit_transform(docs)
        print("Indexed Terms:", self.vectorizer.get_feature_names_out())
        print("TF-IDF Matrix Shape:", self.tfidf_matrix.shape)

    def save_index(self, file_path):
        with open(file_path, 'wb') as f:
            pickle.dump((self.vectorizer, self.tfidf_matrix), f)

    def load_index(self, file_path):
        with open(file_path, 'rb') as f:
            self.vectorizer, self.tfidf_matrix = pickle.load(f)

    def query(self, text):
        query_vec = self.vectorizer.transform([text])
        cos_sim = (self.tfidf_matrix * query_vec.T).toarray()
        return cos_sim

if __name__ == "__main__":
    indexer = Indexer()
    docs = ["API documentation from Stack Overflow.", "Discussion about API usage and best practices."]
    indexer.create_index(docs)
    indexer.save_index('index.pkl')
    print("Index created and saved.")
