from transformers import DistilBertTokenizer, DistilBertModel
import torch

class NLPModel:
    def __init__(self):
        # Load pre-trained DistilBERT model and tokenizer
        self.tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
        self.model = DistilBertModel.from_pretrained("distilbert-base-uncased")

    def get_embeddings(self, query: str):
        inputs = self.tokenizer(query, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).squeeze()

# Example usage
nlp_model = NLPModel()
query = "Show me manual cars under $30,000"
embeddings = nlp_model.get_embeddings(query)
