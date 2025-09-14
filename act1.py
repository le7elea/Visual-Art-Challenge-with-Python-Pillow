# Import required libraries for image manipulation
from PIL import Image, ImageDraw, ImageFont

# Set canvas dimensions (standard 1366x768 resolution)
canvas_w, canvas_h = 1366, 768

# Load and prepare the background image
# Convert to RGBA for transparency support and resize to canvas dimensions
background = Image.open("assets/bground.png").convert("RGBA").resize((canvas_w, canvas_h))
canvas = background.copy()  # Create a working copy of the background
draw = ImageDraw.Draw(canvas)  # Create drawing context for text rendering

# Configure the main title text
font = ImageFont.truetype("Hyperwave.ttf", 128)  # Load custom font at size 128
text = "On Fire, On Point, On the Scene"

# Calculate text dimensions for positioning
text_w = font.getlength(text)  # Get text width
text_h = font.getbbox(text)[3] - font.getbbox(text)[1]  # Calculate text height from bounding box

# Position the text 
x = (canvas_w - text_w) // 5
y = 45

# Add drop shadow effect to text
shadow_offset = 7  # Shadow displacement in pixels
# Draw shadow text (black with transparency)
draw.text((x+shadow_offset, y+shadow_offset), text, font=font, fill=(0,0,0,180))
# Draw main text (deep pink color)
draw.text((x, y), text, font=font, fill=(255,20,147,255))

# Load all image assets and convert to RGBA for transparency support
volleyball2 = Image.open("assets/volleyball2.png").convert("RGBA")
basketball = Image.open("assets/basketball.png").convert("RGBA")
logo = Image.open("assets/ccis_lg.png").convert("RGBA")
mascot1 = Image.open("assets/mascot1.png").convert("RGBA")
mascot2 = Image.open("assets/mascot2.png").convert("RGBA")
mascot_peek = Image.open("assets/mascot_peek.png").convert("RGBA")
mascot2 = Image.open("assets/mascot2.png").convert("RGBA")  # Note: loaded twice (possible duplicate)
volleyball1 = Image.open("assets/volleyball1.png").convert("RGBA")
sepak_takraw = Image.open("assets/sepak_takraw.png").convert("RGBA")

# Helper function to resize and paste images with transparency
def paste_resized(base, img, size, pos):
    
    resized = img.resize(size)  # Resize the image
    base.paste(resized, pos, resized)  # Paste with alpha channel as mask

# Place all images on the canvas with specific sizes and positions
# Large volleyball on the right side
paste_resized(canvas, volleyball2, (400, 400), (890, 200))

# Basketball in the top-right area
paste_resized(canvas, basketball, (400, 400), (830, 50))

# Large volleyball on the left side (overlapping with background edge)
paste_resized(canvas, volleyball1, (500, 500), (50, 20))

# CCIS logo (large, centered)
paste_resized(canvas, logo, (750, 750), (329, 80))

# Sepak takraw ball on the left (partially off-canvas with negative x)
paste_resized(canvas, sepak_takraw, (400, 400), (-40, 150))

# First mascot on the left side
paste_resized(canvas, mascot1, (400, 400), (150, 420))

# Second mascot on the right side (appears twice due to duplicate line)
paste_resized(canvas, mascot2, (370, 370), (870, 450))

# Small peeking mascot in top-right corner
paste_resized(canvas, mascot_peek, (150, 150), (1250, 10))

# Duplicate placement of mascot2 (same position as above)
paste_resized(canvas, mascot2, (370, 370), (870, 450))


# Save the final composite image
canvas.save("PROFELEC2_4_LabradorLea_Activity1.png")
print("Successfully outputed!")  # Success message