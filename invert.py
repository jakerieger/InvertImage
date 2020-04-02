from PIL import Image, ImageOps
import sys, os

# required for colored text to appear on windows
os.system('color')

# terminal colors class
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


filename = sys.argv[-1]
output = os.path.splitext(filename)[0] + "_inverted" + os.path.splitext(filename)[1]

print("Is this a transparent image? " + bcolors.BOLD + "(y/n)" + bcolors.ENDC)
is_png = input()


def InvertRGBA(filename, output):
    src_img = Image.open(filename).convert('RGBA')

    # extract alpha channel from src image
    alpha = src_img.split()[-1]

    # extract RGB channel from src image and invert
    im_rgb = ImageOps.invert(src_img.convert('RGB'))

    # convert back to RGBA and apply extracted alpha mask
    im_rgba = im_rgb.convert('RGBA')
    im_rgba.putalpha(alpha)

    # save inverted image
    im_rgba.save(output)

    print(bcolors.OKGREEN + '\n[!] Success.' + bcolors.ENDC + '\n[>] File at ' + bcolors.UNDERLINE + output + bcolors.ENDC)


def InvertRGB(filename, output):
    src_img = Image.open(filename).convert('RGB')
    im_rgb = ImageOps.invert(src_img)
    im_rgb.save(output)

    print(bcolors.OKGREEN + '\n[!] Success.' + bcolors.ENDC + '\n[>] File at ' + bcolors.UNDERLINE + output + bcolors.ENDC)


if input == "Y" or input == "y":
	InvertRGBA(filename, output)
else:
    InvertRGB(filename, output)