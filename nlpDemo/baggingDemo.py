from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "Barack Obama was the 44th President of the United States",
    "The President lives in the White House",
    "The United States has a strong economy"
]
vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(documents)
feature_names = vectorizer.get_feature_names_out()
bow_array = bow_matrix.toarray()

print("Feature Names (Words):", feature_names)
print("\nBag of Words Representation:")
print(bow_array)

