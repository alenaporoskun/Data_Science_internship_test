import spacy

def perform_inference(model_path, test_texts):
    # Loading an spaCy model
    loaded_nlp = spacy.load(model_path)
    for test_text in test_texts:
        # Using the downloaded spaCy model for text processing
        doc = loaded_nlp(test_text)
        # Output of the original text
        print("Original Text:", test_text)
        # Displaying named entities and their labels
        print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])
        # Display a divider for better visibility of results
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    # The path to the saved spaCy model
    model_path = "C:/Users/Admin/Test_task/Task_1/model_spacy"

    # Test texts for recognizing named entities
    test_texts = [
        "The majestic K2 is a challenging peak for climbers.",
        "Mount McKinley, also known as Denali, is located in Alaska.",
        "Mont Blanc is a popular destination for alpine enthusiasts.",
        "Kangchenjunga is one of the most beautiful mountains in the Himalayas."
    ]   

    # Calling a function to perform inference
    perform_inference(model_path, test_texts)