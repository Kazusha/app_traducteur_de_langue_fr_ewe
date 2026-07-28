# Traducteur Français → Ewe

API de traduction automatique du français vers l'ewe, construite avec FastAPI et un modèle NLLB fine-tuné, servi via CTranslate2.

## Fonctionnalités

- Traduction texte français → ewe via le modèle [`liman21/nllb-fr-ewe-midjie21`](https://huggingface.co/liman21/nllb-fr-ewe-midjie21)
- Endpoint `/translate` protégé par un rate limiting (slowapi)
- Endpoint de santé pour vérifier l'état de chargement du modèle
- Gestion centralisée des erreurs (exceptions personnalisées + handler dédié pour le rate limiting)

## Stack technique

- **Backend** : FastAPI + Uvicorn
- **Traduction** : CTranslate2 + Transformers (tokenizer NLLB)
- **Modèle** : téléchargé automatiquement depuis Hugging Face Hub au démarrage
- **Rate limiting** : slowapi
- **Configuration** : Pydantic Settings (`.env`)
- **Frontend** *(à venir)* : Next.js + SweetAlert2

## Structure du projet

```
app_traducteur-fr-ewe/
├── app/
│   ├── __init__.py
│   ├── config.py          # Configuration (Pydantic Settings)
│   ├── exceptions.py      # Exceptions personnalisées + handlers
│   ├── main.py            # Point d'entrée FastAPI
│   ├── models.py          # Schémas Pydantic (requêtes/réponses)
│   ├── translator.py      # Chargement du modèle et logique de traduction
│   ├── middleware/
│   │   ├── __init__.py
│   │   └── rate_limit.py  # Configuration du rate limiting
│   └── routes/
│       ├── __init__.py
│       └── translate.py   # Route POST /translate
├── venv/
├── .env
└── README.md
```

## Prérequis

- Python 3.12
- 

## Installation

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

Créer un fichier `.env` à la racine avec au minimum :

```
```

## Lancement

```bash
uvicorn app.main:app --reload
```

L'API est ensuite disponible sur `http://127.0.0.1:8000`, avec la documentation interactive Swagger sur `http://127.0.0.1:8000/docs`.

Au premier démarrage, le modèle (~623 Mo) est téléchargé depuis Hugging Face Hub et mis en cache localement ; les démarrages suivants sont beaucoup plus rapides.

## Utilisation

### `POST /translate`

**Requête :**
```json
{
  "text": "Dieu est grand"
}
```

**Réponse :**
```json
{
  "source_text": "Dieu est grand",
  "translated_text": "Mawue nye gã",
  "source_lang": "fra_Latn",
  "target_lang": "ewe_Latn"
}
```

## Feuille de route

- [ ] Frontend Next.js avec SweetAlert2 (modal d'accueil avec instructions + gestion des erreurs)
- [ ] Déploiement

## Licence

À définir.