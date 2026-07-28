import ctranslate2
import transformers
from pathlib import Path
from huggingface_hub import snapshot_download
import logging

from app.config import get_settings

logger = logging.getLogger("translator")
settings = get_settings()


class Translator:

    def __init__(self):
        self.translator: ctranslate2.Translator | None = None
        self.tokenizer: transformers.AutoTokenizer | None = None
        self.model_path: Path | None = None

    def load(self):
        logger.info("Telechargement et verification du modele depuis HuggingFace")

        self.model_path = Path(
            snapshot_download(
                repo_id=settings.hf_repo_id,
                token=settings.hf_token or None,
            )
        )

        logger.info(f"Modele telecharge et disponible localement: {self.model_path}")

        self.translator = ctranslate2.Translator(
            str(self.model_path),
            device="auto",
        )

        self.tokenizer = transformers.AutoTokenizer.from_pretrained(
            str(self.model_path),
            src_lang=settings.source_lang,
        )

        logger.info("Modele et tokenizer charges avec succes.")

    def is_ready(self) -> bool:
        return self.translator is not None and self.tokenizer is not None

    def translate(self, text: str) -> str:
        if not self.is_ready():
            raise RuntimeError("Le traducteur n'est pas encore charge")

        source_tokens = self.tokenizer.convert_ids_to_tokens(
            self.tokenizer.encode(text)
        )

        target_prefix = [settings.target_lang]
        results = self.translator.translate_batch(
            [source_tokens],
            target_prefix=[target_prefix],
        )
        output_tokens = results[0].hypotheses[0][1:]
        translated_ids = self.tokenizer.convert_tokens_to_ids(output_tokens)
        translated_text = self.tokenizer.decode(translated_ids, skip_special_tokens=True)
        return translated_text.strip()


translator_instance = Translator()