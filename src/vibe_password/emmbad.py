import os

import numpy as np

INSTRUCT = "Retrieve sentences that express the same intent as the query, paying attention to negations, sentiment, quantities, and relationships."

def emmbad(config, string)->np.ndarray:
    response = config["client"].embeddings.create(
      model=config["model"],
      input=f"Instruct: {INSTRUCT}\nQuery: {string}",
      encoding_format="float"
    )

    return np.array(
        response.data[0].embedding
    )


class Emmbaded:
    __treshold = float(os.getenv("TRESHOLD", "0.72"))
    @classmethod
    def get_threshold(cls) -> float:
        return cls.__treshold

    @classmethod
    def set_threshold(cls, value: float):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("threshold must be a number")

        if not -1.0 <= value <= 1.0:
            raise ValueError("threshold must be between -1.0 and 1.0")

        cls.__treshold = float(value)


    def __init__(self, config, embadee:str):
       self.__embading = emmbad(config, embadee)
       self.__embadee = embadee

    def similarity(self, other) -> float:
        if not isinstance(other, Emmbaded):
            raise TypeError("other must be an Emmbaded")

        return float(self.__embading @ other.__embading)


    def __eq__(self, other):
        if not isinstance(other, Emmbaded):
            return NotImplemented
        return self.similarity(other) > self.get_threshold()


    def __str__(self):
        return self.__embadee
