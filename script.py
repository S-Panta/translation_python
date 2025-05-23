import asyncio
from docx import Document
from googletrans import Translator


async def translate_text(run, translator, language):
    translated = await translator.translate(run.text, dest=language)
    run.text = translated.text
    run.font.name = "Annapurna SIL"


async def translate_all_content_of_document(doc_path, output_path, language="ne"):
    doc = Document(doc_path)
    translator = Translator()
    tasks = []
    for paragraph in doc.paragraphs:
        # run object represent text with styles
        for run in paragraph.runs:
            tasks.append(translate_text(run, translator, language))

    await asyncio.gather(*tasks)
    doc.save(output_path)


asyncio.run(translate_all_content_of_document("test2.docx", "final.docx"))
