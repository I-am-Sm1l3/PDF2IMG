import fitz
import os

# ASCII Art for PDF. Created this Using https://patorjk.com/software/taag/
ascii_art = r"""
                     ,--,                                                                                              
                ,---.'|       ,----..                                 ,-.----.                                       
   ,---,        |   | :      /   /   \                  ,---,.        \    /  \      ,---,        ,---,.             
,`--.' |        :   : |     /   .     :        ,---.  ,'  .' |        |   :    \   .'  .' `\    ,'  .' |             
|   :  :        |   ' :    .   /   ;.  \      /__./|,---.'   |        |   |  .\ :,---.'     \ ,---.'   |             
:   |  '        ;   ; '   .   ;   /  ` ; ,---.;  ; ||   |   .'        .   :  |: ||   |  .`\  ||   |   .'  .--.--.    
|   :  |        '   | |__ ;   |  ; \ ; |/___/ \  | |:   :  |-,        |   |   \ ::   : |  '  |:   :  :   /  /    '   
'   '  ;        |   | :.'||   :  | ; | '\   ;  \ ' |:   |  ;/|        |   : .   /|   ' '  ;  ::   |  |-,|  :  /`./   
|   |  |        '   :    ;.   |  ' ' ' : \   \  \: ||   :   .'        ;   | |`-' '   | ;  .  ||   :  ;/||  :  ;_     
'   :  ;        |   |  ./ '   ;  \; /  |  ;   \  ' .|   |  |-,        |   | ;    |   | :  |  '|   |   .' \  \    `.  
|   |  '        ;   : ;    \   \  ',  /    \   \   ''   :  ;/|        :   ' |    '   : | /  ; '   :  '    `----.   \ 
'   :  |        |   ,/      ;   :    /      \   `  ;|   |    \        :   : :    |   | '` ,/  |   |  |   /  /`--'  / 
;   |.'         '---'        \   \ .'        :   \ ||   :   .'        |   | :    ;   :  .'    |   :  \  '--'.     /  
'---'                         `---`           '---" |   | ,'          `---'.|    |   ,.'      |   | ,'    `--'---'   
                                                    `----'              `---`    '---'        `----'                 
                                                                                                                                      
"""

print(ascii_art)
print("Usage: Enter pdf path and page number.")
print("To extract all pages, type 'all'.")

def extract_pages_as_images(input_pdf, page_to_find=None):
    doc = fitz.open(input_pdf)
    output_dir = os.path.splitext(input_pdf)[0] + "_images"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    zoom = 300 / 72
    total_pages = len(doc)

    try:
        if page_to_find is not None:
            # First try to find by label (the number before parentheses)
            found = False
            for idx in range(total_pages):
                page = doc[idx]
                label = page.get_label()
                if label and label.isdigit() and int(label) == page_to_find:
                    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
                    pix.save(os.path.join(output_dir, f"page_{page_to_find}.png"))
                    found = True
                    break
            
            # If label not found, try physical page number
            if not found:
                if page_to_find < 1 or page_to_find > total_pages:
                    raise ValueError(f"Page number must be between 1 and {total_pages}")
                page = doc[page_to_find - 1]
                pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
                pix.save(os.path.join(output_dir, f"page_{page_to_find}.png"))
        else:
            # Extract all pages
            for idx in range(total_pages):
                page = doc[idx]
                label = page.get_label()
                # Try to use label if it exists and is a number
                page_num = int(label) if label and label.isdigit() else (idx + 1)
                pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
                pix.save(os.path.join(output_dir, f"page_{page_num}.png"))
    finally:
        doc.close()
        
    return output_dir

def main():
    while True:
        pdf = input("PDF path: ")
        if pdf and os.path.exists(pdf) and pdf.lower().endswith('.pdf'):
            break
        print("Invalid file")

    while True:
        page = input("Page number or 'all': ").lower()
        if page == 'all':
            page_num = None
            break
        try:
            page_num = int(page)
            break
        except ValueError:
            continue
    
    try:
        out_dir = extract_pages_as_images(pdf, page_to_find=page_num)
        print(f"Done -> {out_dir}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
