import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class FAQChatbot:

    def __init__(self, faq_file):

        self.data = pd.read_csv(faq_file)

        self.vectorizer = TfidfVectorizer()

        self.question_vectors = self.vectorizer.fit_transform(
            self.data["question"]
        )

    def get_response(self, user_question):

        user_vector = self.vectorizer.transform(
            [user_question]
        )

        similarity = cosine_similarity(
            user_vector,
            self.question_vectors
        )

        best_match = similarity.argmax()

        confidence = similarity[0][best_match]

        if confidence < 0.3:
            return (
                "Sorry, I couldn't find a relevant answer."
            )

        return self.data.iloc[
            best_match
        ]["answer"]