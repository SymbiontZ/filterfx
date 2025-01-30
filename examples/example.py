import filterfx as ffx
from PIL import Image

# Applies a grayscale filter to the image located at the specified path
# and saves the resulting image to the output path provided.
ffx.apply_filter_from_path("docs/images/example.jpg", ffx.FILTER.GRAYSCALE, output="docs/images/grayscale.jpg")


# Opens the image from the specified path, applies a sepia filter to it,
# and displays the resulting image in a window.
image = Image.open("docs/images/example.jpg")
ffx.apply_filter(image, ffx.FILTER.VINTAGE, show=True)


image = ffx.image_enhances.enhance_color(image, 3)
