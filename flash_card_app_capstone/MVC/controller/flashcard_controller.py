import pandas as pd
import random
from paths import CSV_WORDS_PATH


class FlashCardController:
    @staticmethod
    def get_random_word():
        df = pd.read_csv(CSV_WORDS_PATH)
        return random.choice(list(df["English"]))

    @staticmethod
    def get_translation(word):
        df = pd.read_csv(CSV_WORDS_PATH)
        fila = df[df["English"] == word]
        if not fila.empty:
            return fila.iloc[0]["Spanish"]
        return "Traducción no encontrada"

    @staticmethod
    def update_csv(learned_word):
        import os

        df_original = pd.read_csv(CSV_WORDS_PATH)

        match = df_original[df_original["English"] == learned_word]
        if match.empty:
            print(f"La palabra '{learned_word}' no está en el archivo original.")
            return

        df_actualizado = df_original[df_original["English"] != learned_word]

        out_dir = "out"
        os.makedirs(out_dir, exist_ok=True)

        learned_path = os.path.join(out_dir, "learned_words.csv")

        if os.path.exists(learned_path):
            df_learned = pd.read_csv(learned_path)
            df_learned = pd.concat([df_learned, match], ignore_index=True)
        else:
            df_learned = match

        df_actualizado.to_csv(CSV_WORDS_PATH, index=False)
        df_learned.to_csv(learned_path, index=False)

        print(f"'{learned_word}' fue movida a '{learned_path}'.")




