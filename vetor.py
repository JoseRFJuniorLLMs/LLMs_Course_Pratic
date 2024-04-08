

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Exemplo de vetores que representariam palavras no espaço vetorial
# Estes são vetores aleatórios para fins ilustrativos
word_vectors = {
    "dog": np.array([0.5, 1.2, 0.3]),
    "cat": np.array([0.4, 1.0, 0.2]),
    "apple": np.array([0.1, 0.0, 1.5]),
    "banana": np.array([0.2, 0.1, 1.4])
}

# Calculando a similaridade de cosseno entre 'dog' e 'cat'
similarity_dog_cat = cosine_similarity([word_vectors["dog"]], [word_vectors["cat"]])

# Calculando a similaridade de cosseno entre 'apple' e 'banana'
similarity_apple_banana = cosine_similarity([word_vectors["apple"]], [word_vectors["banana"]])

(similarity_dog_cat, similarity_apple_banana)

