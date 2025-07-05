import os

PROJECT_ROOT = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(PROJECT_ROOT, "images")

CARD_FRONT_PATH = os.path.join(IMAGES_DIR, "card_front.png")
CARD_BACK_PATH = os.path.join(IMAGES_DIR, "card_back.png")
RIGHT_IMAGE_PATH = os.path.join(IMAGES_DIR, "right.png")
WRONG_IMAGE_PATH = os.path.join(IMAGES_DIR, "wrong.png")

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
CSV_WORDS_PATH = os.path.join(DATA_DIR, "100_most_common_english_words.csv")
