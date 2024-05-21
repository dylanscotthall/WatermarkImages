import os
from PIL import Image, ImageDraw, ImageFont, ImageStat

def get_contrasting_color(avg_color):
    r, g, b = avg_color
    brightness = (r*299 + g*587 + b*114) / 1000
    return (255, 255, 255) if brightness < 128 else (0, 0, 0)

def add_watermark(image_path, watermark_text, font_path, font_scale, position):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            font_size = int(height * font_scale)

            font = ImageFont.truetype(font_path, font_size)

            draw = ImageDraw.Draw(img)

            # Calculate text size
            bbox = draw.textbbox((0, 0), watermark_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            if position == 'top_left':
                x, y = 20, 20
            elif position == 'top_right':
                x, y = width - text_width - 20, 20
            elif position == 'bottom_left':
                x, y = 20, height - text_height - 20
            elif position == 'bottom_right':
                x, y = width - text_width - 20, height - text_height - 20
            else:
                raise ValueError("Invalid position argument. Choose from 'top_left', 'top_right', 'bottom_left', or 'bottom_right'.")

            region = img.crop((x, y, x + text_width, y + text_height))
            avg_color = ImageStat.Stat(region).mean[:3]

            text_color = get_contrasting_color(avg_color)

            draw.text((x, y), watermark_text, font=font, fill=text_color)
            img.save(image_path)
    except Exception as e:
        print(f"Failed to add watermark to {image_path}: {e}")

def process_images_in_directory(root_directory, font_path, font_scale, position):
    for subdir, _, files in os.walk(root_directory):
        folder_name = os.path.basename(subdir)
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                image_path = os.path.join(subdir, file)
                add_watermark(image_path, folder_name, font_path, font_scale, position)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Add folder name as watermark to images.")
    parser.add_argument("directory", type=str, help="The root directory containing image subfolders.")
    parser.add_argument("font", type=str, help="The path to the .ttf font file to use for the watermark.")
    parser.add_argument("--scale", type=float, default=0.05, help="Font size scale as a proportion of the image height (e.g., 0.05 for 5%).")
    parser.add_argument("--position", type=str, choices=['top_left', 'top_right', 'bottom_left', 'bottom_right'], default='bottom_right', help="Position of the watermark text.")
    args = parser.parse_args()

    process_images_in_directory(args.directory, args.font, args.scale, args.position)
