import pymupdf
from deep_translator import GoogleTranslator


# Define color "white"
WHITE = pymupdf.pdfcolor["white"]

# This flag ensures that text will be dehuphenated after extraction.
textflags = pymupdf.TEXT_DEHYPHENATE

# Configure the desired translator
to_portuguese = GoogleTranslator(source="en", target="pt")

# Open the document
doc = pymupdf.open("Young_Childrens_Experience_in_Unplugged_Activitie.pdf")


# Define an Optional Content laer in the document named "Portuguese"
# Activate it by default
ocg_xref = doc.add_ocg("Portuguese", on=True)

# Iterate over all pages
for page in doc:
    #Extract text grouped like lines in a paragraph.
    blocks = page.get_text("blocks", flags=textflags)

    # Every block of text is contained in a rectangle ("bbox")
    for block in blocks:
        bbox = block[:4] # area containing the text
        text = block[4] # the text of this block

        # Invoke the actual translation to deliver us a Portuguese String
        portuguese = to_portuguese.translate(text)

        # Cover the english text with a white rectangle.
        page.draw_rect(bbox, color=None, fill=WHITE, oc=ocg_xref)

        # Write the portuguese text into the original rectangle.
        page.insert_htmlbox(
            bbox, portuguese, css="* {font-family: sans-serif;}", oc=ocg_xref
        )

doc.subset_fonts()
doc.ez_save("Young_Childrens_Experience_in_Unplugged_Activitie_-_portuguese_-_.pdf")

        



