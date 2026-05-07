import pickle

class DeliveryMdl:
    def predict(self, dist, weight):
        time = 0.5 + (dist * 0.2) + (weight * 0.1)
        return time

model = DeliveryMdl()

with open("delivery_mdl.pkl", "wb") as f:
    pickle.dump(model, f)