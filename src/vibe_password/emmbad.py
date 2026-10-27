import numpy as np


def emmbad(config, string)->np.ndarray:
    response = config["client"].embeddings.create(
      model=config["model"],
      input=string,
      encoding_format="float"
    )

    return np.array(
        response.data[0].embedding
    )


class Emmbaded:
    treshold = 0.67
    def __init__(self, config, embadee:str):
       self.__embading = emmbad(config, embadee)
       self.__embadee = embadee

    def __eq__(self, other):
        if not isinstance(other, Emmbaded):
            return NotImplemented
        return (self.__embading @ other.__embading) > self.treshold


    def __str__(self):
        return self.__embadee
