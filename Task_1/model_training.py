import spacy
import random
import pickle
from spacy.training.example import Example

def train_ner_model(train_data_path, output_dir, n_iter=10):
    # Loading training data from a file
    with open(train_data_path, 'rb') as file:
        loaded_train_data = pickle.load(file)

    # Print the number of training examples
    print(f"Number of training examples: {len(loaded_train_data)}")

    # Loading an empty spaCy model
    nlp = spacy.blank("en")

    # Adding a component for named entity recognition (NER)
    ner = nlp.add_pipe("ner")

    # Start training the model
    nlp.begin_training()

    for epoch in range(n_iter):  # Example: 10 iterations of training
        random.shuffle(loaded_train_data)
        losses = {}

        for text, annotations in loaded_train_data:
            example = Example.from_dict(text, annotations)
            nlp.update([example], drop=0.5, losses=losses)

        print(losses)

    # Збереження навченої моделі
    nlp.to_disk(output_dir)

if __name__ == "__main__":
    # Path to the training data file
    train_data_path = "C:/Users/Admin/Test_task/Task_1/data/train_data.pkl"

    # Way to save a trained model
    output_dir = "C:/Users/Admin/Test_task/Task_1/model_spacy"

    # Model training
    train_ner_model(train_data_path, output_dir)