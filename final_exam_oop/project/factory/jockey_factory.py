from project.jockey import Jockey


class JockeyFactory:
    @staticmethod
    def create_a_jockey(jockey_name, jockey_age):
        return Jockey(jockey_name, jockey_age)