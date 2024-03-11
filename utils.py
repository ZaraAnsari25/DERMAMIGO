
import base64
import requests

import translator_config


TRANSLATE_CATEGORIES = {
    "Acne and Rosacea Photos": "Fotos de Acné y Rosácea",
    "Atopic Dermatitis Photos": "Fotos de dermatitis atópica",
    "Eczema Photos": "Fotos de eccema",
    "Urticaria Hives": "urticaria urticaria",
    "Melanoma Skin Cancer Nevi and Moles": "Melanoma Cáncer de piel Nevos y lunares",
    "Psoriasis pictures Lichen Planus and related diseases": "Imágenes de psoriasis Liquen plano y enfermedades relacionadas",
    "Vasculitis Photos": "Fotos de vasculitis",
    "Warts and other viral infections": "Verrugas y otras infecciones virales",
    "Seborrheic Keratoses and other Benign Tumors": "Queratosis seborreicas y otros tumores benignos",
    "Herpes HPV and other STDs Photos": "Herpes VPH y otras ETS Fotos"
}


CATEGORIES = [
    "Acne and Rosacea Photos",
    "Atopic Dermatitis Photos",
    "Eczema Photos",
    "Urticaria Hives",
    "Melanoma Skin Cancer Nevi and Moles",
    "Psoriasis pictures Lichen Planus and related diseases",
    "Vasculitis Photos",
    "Warts and other viral infections",
    "Seborrheic Keratoses and other Benign Tumors",
    "Herpes HPV and other STDs Photos",
]

CATEGORIES.sort()


def translate(sent: str, lan: str) -> str:
    return translator_config.SENTENCE[sent][lan]


def get_prediction(image_data):
    #replace your image classification ai service URL
    url = 'https://askai.aiclub.world/4e2b380d-48f8-4e20-a311-9d171553fc7a'
    r = requests.post(url, data=image_data)
    response = r.json()['predicted_label']
    return int(response)


def get_label(index: int, lan: str = "en"):
    label = CATEGORIES[index]
    if lan == "sp":
        label = TRANSLATE_CATEGORIES.get(label, "")
        return label

    return label

def encoder(path):
    with open(path, 'rb') as image:
        payload = base64.b64encode(image.read())
        payload = payload.decode('utf-8')

        return payload


