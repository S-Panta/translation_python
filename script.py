import asyncio
from docx import Document
from googletrans import Translator

async def translate_text(text, language="ne") -> str:
    async with Translator() as translator:
        result = await translator.translate(text, dest=language)
    return result.text

doc = Document("test.docx")

for paragraph in doc.paragraphs:
    # run object represent text with styles

    for run in paragraph.runs:
        run.text = asyncio.run(translate_text(run.text))
        run.font.name = "Annapurna SIL"

doc.save("final_translation.docx")
