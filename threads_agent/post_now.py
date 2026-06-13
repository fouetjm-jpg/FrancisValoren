import os
import time
import requests
from datetime import date, datetime

THREADS_USER_ID = os.environ["THREADS_USER_ID"]
THREADS_TOKEN   = os.environ["THREADS_ACCESS_TOKEN"]
GRAPH_URL       = "https://graph.threads.net/v1.0"
EPOCH           = date(2026, 6, 11)

def post_number():
    days = (date.today() - EPOCH).days
    h = datetime.now().hour
    slot = 0 if h < 10 else (1 if h < 17 else 2)
    return days * 3 + slot

BOOKS = [
    {
        "title": "Le Jardin du Premier Souffle",
        "image_url": "https://raw.githubusercontent.com/fouetjm-jpg/FrancisValoren/main/images/jardin.jpg",
    },
    {
        "title": "Liberté, Égalité, Facturé",
        "image_url": "https://raw.githubusercontent.com/fouetjm-jpg/FrancisValoren/main/images/liberte.jpg",
    },
    {
        "title": "Le Chant de la Terre",
        "image_url": "https://raw.githubusercontent.com/fouetjm-jpg/FrancisValoren/main/images/terre.jpg",
    },
    {
        "title": "Quand l'Humanité Cesse d'Écouter",
        "image_url": "https://raw.githubusercontent.com/fouetjm-jpg/FrancisValoren/main/images/arbres.jpg",
    },
    {
        "title": "La Danse des Corps Perdus",
        "image_url": "https://raw.githubusercontent.com/fouetjm-jpg/FrancisValoren/main/images/danse.jpg",
    },
]

CAPTIONS = {
    "Le Jardin du Premier Souffle": [
        "Un prêtre disparaît. Un carnet crypté. Une quête qui mène de Rome à Babylone.\nEt si le jardin d'Éden existait vraiment ?\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=le+jardin+du+premier+souffle\n#FrancisValoren #LeJardinDuPremierSouffle #Thriller #Ésotérisme",
        "Alexandre Dornier n'était que bibliothécaire.\nJusqu'au jour où il hérite du secret le mieux gardé de l'humanité.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=le+jardin+du+premier+souffle\n#FrancisValoren #LeJardinDuPremierSouffle #Thriller #Ésotérisme",
        "Rome. Constantinople. Babylone. Les montagnes du Zagros.\nDans le carnet, des indices sont cachés. Il faut savoir les lire.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=le+jardin+du+premier+souffle\n#FrancisValoren #LeJardinDuPremierSouffle #Thriller #Ésotérisme",
        "Trouver le jardin d'Éden n'est que le début.\nLe vrai dilemme : faut-il le révéler au monde — ou le protéger pour toujours ?\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=le+jardin+du+premier+souffle\n#FrancisValoren #LeJardinDuPremierSouffle #Thriller #Ésotérisme",
        "Entre thriller ésotérique et quête spirituelle, un roman qui pose l'ultime question :\ncertaines vérités méritent-elles d'être connues ?\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=le+jardin+du+premier+souffle\n#FrancisValoren #LeJardinDuPremierSouffle #Thriller #Ésotérisme",
        "Un carnet crypté. Des secrets millénaires. Un homme ordinaire face au plus grand mystère de l'histoire.\nLe jardin d'Éden existe. Et il change tout.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=le+jardin+du+premier+souffle\n#FrancisValoren #LeJardinDuPremierSouffle #Thriller #Ésotérisme",
    ],
    "Liberté, Égalité, Facturé": [
        "En 2025, avoir une douche fait de vous un privilégié.\nEn 1789, ne pas manger trois jours était une condamnation.\nTrois siècles. Le même génie fiscal.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=Libert%C3%A9+%C3%89galit%C3%A9+Factur%C3%A9\n#FrancisValoren #LibertéÉgalitéFacturé #Roman #Satire",
        "Les Présidents taxent les taxes.\nLes Rois taxaient le pain.\nLa France ne change que de costume et de titre.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=Libert%C3%A9+%C3%89galit%C3%A9+Factur%C3%A9\n#FrancisValoren #LibertéÉgalitéFacturé #Roman #Satire",
        "Un peuple qui encaisse, qui patiente, qui survit… jusqu'au jour où il ne peut plus.\nCe jour-là, il crie.\nEt les oreilles d'État sont miraculeusement bouchées — depuis plus de trois siècles.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=Libert%C3%A9+%C3%89galit%C3%A9+Factur%C3%A9\n#FrancisValoren #LibertéÉgalitéFacturé #Roman #Satire",
        "Julien, 2025. Jean-Baptiste, 1789.\nDeux destins ordinaires. Une France épuisée, une France affamée. Un seul miroir.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=Libert%C3%A9+%C3%89galit%C3%A9+Factur%C3%A9\n#FrancisValoren #LibertéÉgalitéFacturé #Roman #Satire",
        "Quand la faim devient politique, l'Histoire cesse d'être un souvenir.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=Libert%C3%A9+%C3%89galit%C3%A9+Factur%C3%A9\n#FrancisValoren #LibertéÉgalitéFacturé #Roman #Satire",
        "Liberté, Égalité, Facturé — deux époques, un seul constat :\nla France a toujours su habiller l'injustice en institution.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=Libert%C3%A9+%C3%89galit%C3%A9+Factur%C3%A9\n#FrancisValoren #LibertéÉgalitéFacturé #Roman #Satire",
    ],
    "Le Chant de la Terre": [
        "2030. La Terre s'effondre sous le poids de son propre progrès.\nEliott Varner s'envole pour la sauver.\nDeux siècles plus tard, il s'éveille sur une planète vivante. Elle s'appelle Éliane.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/dp/B0GGHRVC7C\n#FrancisValoren #LeChantDeLaTerre #Roman #ScienceFiction",
        "Elle se souvient des hommes… et de leurs fautes.\nCe n'est pas vraiment un roman de science-fiction.\nC'est une confession à voix basse, une lettre adressée à l'avenir.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/dp/B0GGHRVC7C\n#FrancisValoren #LeChantDeLaTerre #Roman #ScienceFiction",
        "Et si la Terre, après tout ce qu'on lui a fait subir, finissait par se souvenir ?\nÉliane se souvient. Et elle a des choses à dire.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/dp/B0GGHRVC7C\n#FrancisValoren #LeChantDeLaTerre #Roman #ScienceFiction",
        "Astronaute, mari, père.\nEliott Varner part sauver la Terre.\nIl ne savait pas que c'est elle qui allait le juger.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/dp/B0GGHRVC7C\n#FrancisValoren #LeChantDeLaTerre #Roman #ScienceFiction",
        "Deux siècles de sommeil. Un réveil sur une planète consciente.\nLe Chant de la Terre — une lettre adressée à l'avenir.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/dp/B0GGHRVC7C\n#FrancisValoren #LeChantDeLaTerre #Roman #ScienceFiction",
        "La Terre ne meurt pas. Elle se souvient.\nEt quand elle parle, il vaut mieux être prêt à écouter.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/dp/B0GGHRVC7C\n#FrancisValoren #LeChantDeLaTerre #Roman #ScienceFiction",
    ],
    "Quand l'Humanité Cesse d'Écouter": [
        "Un bûcheron. Une forêt. Et le jour où il entend enfin ce qu'il avait toujours ignoré : les arbres parlent.\nIls murmurent leur mémoire. Ils savent ce qu'il vient chercher.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/dp/B0H2W6L43H\n#FrancisValoren #QuandLHumanitéCesseDÉcouter #ContePhilosophique #Nature",
        "Ils se souviennent de tout ce que l'humanité a détruit.\nEt ils observent, endurent, résistent.\n« Que devenons-nous quand nous entendons enfin ce que nous détruisons ? »\n\n📖 Disponible sur Amazon → https://www.amazon.fr/dp/B0H2W6L43H\n#FrancisValoren #QuandLHumanitéCesseDÉcouter #ContePhilosophique #Nature",
        "D'un côté, les hommes qui calculent et exploitent.\nDe l'autre, la forêt qui observe et résiste.\nUn bûcheron coincé entre les deux.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/dp/B0H2W6L43H\n#FrancisValoren #QuandLHumanitéCesseDÉcouter #ContePhilosophique #Nature",
        "La forêt parle. Elle murmure sa mémoire, son organisation, ses peurs.\nElle sait ce que l'homme vient chercher. Et elle se souvient de tout.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/dp/B0H2W6L43H\n#FrancisValoren #QuandLHumanitéCesseDÉcouter #ContePhilosophique #Nature",
        "Un conte philosophique sur la déforestation, la mémoire du vivant,\net la possibilité fragile d'un équilibre entre l'homme et la nature.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/dp/B0H2W6L43H\n#FrancisValoren #QuandLHumanitéCesseDÉcouter #ContePhilosophique #Nature",
        "Au bord d'une forêt sans limites, un homme vivait seul avec sa hache.\nJusqu'au jour où la forêt a décidé de lui parler. Il n'était pas prêt.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/dp/B0H2W6L43H\n#FrancisValoren #QuandLHumanitéCesseDÉcouter #ContePhilosophique #Nature",
    ],
    "La Danse des Corps Perdus": [
        "Strasbourg, juillet 1518. Une femme se met à danser seule dans une rue. Elle ne s'arrêtera plus.\nQuatre cents personnes la suivront. Certaines en mourront.\nLes faits ont eu lieu. Personne ne sait pourquoi.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=La+Danse+des+Corps+Perdus+Francis+Valoren\n#FrancisValoren #LaDanseDesCorpsPerdus #Roman #Histoire",
        "Le chirurgien Gregor Metz observe, note, cherche.\nIl traverse une ville paralysée par la peur, des corps épuisés qui dansent jusqu'au sang.\nNi la science ni la foi ne parviennent à nommer ce qu'il voit.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=La+Danse+des+Corps+Perdus+Francis+Valoren\n#FrancisValoren #LaDanseDesCorpsPerdus #Roman #Histoire",
        "Un roman sobre et tendu sur les limites de la raison humaine face à l'inexplicable.\nEt sur ce que la peur collective peut faire à des corps, à une ville, à une époque entière.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=La+Danse+des+Corps+Perdus+Francis+Valoren\n#FrancisValoren #LaDanseDesCorpsPerdus #Roman #Histoire",
        "Ils dansaient jusqu'au sang. Jusqu'à l'épuisement. Jusqu'à la mort.\nSans musique. Sans volonté. Sans pouvoir s'arrêter. C'est une histoire vraie.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=La+Danse+des+Corps+Perdus+Francis+Valoren\n#FrancisValoren #LaDanseDesCorpsPerdus #Roman #Histoire",
        "Que se passe-t-il quand la peur collective s'empare d'une ville entière ?\nStrasbourg, 1518. La réponse est terrifiante — et réelle.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=La+Danse+des+Corps+Perdus+Francis+Valoren\n#FrancisValoren #LaDanseDesCorpsPerdus #Roman #Histoire",
        "L'une des épidémies les plus étranges de l'histoire humaine.\nUn chirurgien seul face à l'inexplicable.\nLes faits ont eu lieu. Personne ne sait pourquoi.\n\n📖 Disponible sur Amazon → https://www.amazon.fr/s?k=La+Danse+des+Corps+Perdus+Francis+Valoren\n#FrancisValoren #LaDanseDesCorpsPerdus #Roman #Histoire",
    ],
}


def pick_book_and_caption():
    n = post_number()
    book = BOOKS[n % len(BOOKS)]
    captions = CAPTIONS[book["title"]]
    caption = captions[(n // len(BOOKS)) % len(captions)]
    return book, caption


def post_once():
    book, caption = pick_book_and_caption()
    print(f"Livre : {book['title']}")
    print(f"Post #{post_number()}")
    print(f"Caption :\n{caption}\n")
    print(f"Caption :\n{caption}\n")
    resp = requests.post(
        f"{GRAPH_URL}/{THREADS_USER_ID}/threads",
        params={"media_type": "IMAGE", "image_url": book["image_url"],
                "text": caption, "access_token": THREADS_TOKEN},
    )
    resp.raise_for_status()
    container_id = resp.json()["id"]
    time.sleep(30)
    resp2 = requests.post(
        f"{GRAPH_URL}/{THREADS_USER_ID}/threads_publish",
        params={"creation_id": container_id, "access_token": THREADS_TOKEN},
    )
    resp2.raise_for_status()
    print(f"Post publié — ID : {resp2.json()['id']}")


if __name__ == "__main__":
    post_once()
