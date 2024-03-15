from tkinter import simpledialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import subprocess
import tempfile
from text_manipulation import draw_text_psd_style, draw_pseudobold, wraparound
import sys
import json
import os

if not os.path.exists("./config.json"):
    raise FileNotFoundError("Missing config.json file! Copy template.json to config.json to get started.")

def styled_rectangle(draw, xybox, theme):
    x = xybox[0]
    y = xybox[1]
    x2 = xybox[2]
    y2 = xybox[3]

    draw.line([(x+1,y+1), (x+1,y2-1)], theme["style"]["highlight"], 1)
    draw.line([(x+1,y+1), (x2-1,y+1)], theme["style"]["highlight"], 1)
    draw.line([(x2,y), (x2,y2)], theme["style"]["outline"], 1)
    draw.line([(x,y2), (x2,y2)], theme["style"]["outline"], 1)
    draw.line([(x+1,y2-1), (x2-1,y2-1)], theme["style"]["shadow"], 1)
    draw.line([(x2-1,y+1), (x2-1,y2-1)], theme["style"]["shadow"], 1)

def draw_button(draw, xy, text, font, theme, enabled = True):
    draw.rectangle([(xy[0]-37,xy[1]),(xy[0]+37,xy[1]+23)], theme["style"]["outline"])
    draw.rectangle([(xy[0]-36,xy[1]+1),(xy[0]+36,xy[1]+22)], theme["background"])
    styled_rectangle(draw, (xy[0]-37,xy[1],xy[0]+36,xy[1]+22), theme)
    draw.text((xy[0], xy[1]+6), text, theme["textcolor"] if enabled else theme["style"]["shadow"], font=font, anchor="mt", align="center")
    

config = json.load(open("config.json", encoding="utf8"))

data_theme = open("assets/" + config["theme"] + ".json", encoding="utf8")
theme = json.load(data_theme)

doublesize = False
icon = config["default_icon"] if len(sys.argv) < 2 else sys.argv[1]

for arg in sys.argv[2:]:
    if arg.startswith("--theme:"):
        theme = json.load(open("assets/" + arg.split(":", 1)[1] + ".json", encoding="utf8"))
    if arg == "--double":
        doublesize == True


youricon = Image.open("assets/icons/" + icon + ".png").convert("RGBA")

font = ImageFont.FreeTypeFont("assets/Windows Regular.ttf", 12.5)

textbox_content = simpledialog.askstring("Textbox content", "Enter content of textbox:")

if textbox_content is None:
    raise ValueError("Cancelled")

img = Image.new("RGBA", (min(max(200, int(font.getlength(textbox_content)) + 80), 800), 110), (0, 0, 0, 0))
xicon = Image.open("assets/x.png").convert("RGBA")
draw = ImageDraw.Draw(img)
draw.fontmode = "1"

draw.rectangle([(0,0), (img.size[0]-1,img.size[1]-1)], theme["background"])
draw.rectangle([(3,3), (img.size[0]-4,20)], theme["titlebar"]["backdrop"])

styled_rectangle(draw, (0,0,img.size[0]-1,img.size[1]-1), theme)

img.paste(xicon, ((img.size[0]-5)-xicon.size[0],5))
img.paste(youricon, (12, 32), youricon)

linebreak_textbox_content = wraparound(textbox_content, font, img.size[0]-80)

draw_pseudobold(draw, (4,4), config["title_text"], font, theme["titlebar"]["textcolor"])
draw.multiline_text((60,32), linebreak_textbox_content, fill=theme["textcolor"], font=font)

# "OK" button
middle = int(img.size[0]/2)
for i in range(len(config["buttons"])):
    pivot = (middle - ((len(config["buttons"])-1)*40) + 80*i, 75)
    draw_button(draw, pivot, config["buttons"][i][0], font, theme, config["buttons"][i][1])


if doublesize:
    img = img.resize((img.size[0]*2, img.size[1]*2), Image.Resampling.NEAREST)
temp = tempfile.NamedTemporaryFile("w+b", suffix=".png")
img.save(temp, "png")
img.save("test.png")

print(textbox_content)

subprocess.call("xclip -t image/png -sel c < " + temp.name, shell=True)
# subprocess.call("xclip -sel c < " + temp.name, shell=True)
