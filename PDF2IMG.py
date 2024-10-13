import fitz
import argparse
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

def extract_pages_as_images(input_pdf):
    doc = fitz.open(input_pdf)
    output_dir = os.path.splitext(input_pdf)[0] + "_page_images"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        image_filename = os.path.join(output_dir, f"page_{page_num+1}.png")
        pix.save(image_filename)

        print(f"Page {page_num+1} saved as {image_filename}")

    doc.close()
    print(f"All pages have been extracted as images to {output_dir}")

def main():
    parser = argparse.ArgumentParser(description="Extract full pages as images from a PDF file.")
    parser.add_argument("-f", "--file", required=True, help="Input PDF file path")
    args = parser.parse_args()

    input_pdf = args.file

    extract_pages_as_images(input_pdf)

if __name__ == "__main__":
    main()
