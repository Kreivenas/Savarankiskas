from PIL import Image, ImageEnhance

def apply_contrast(image_path, output_path, contrast_factor):
    image = Image.open(image_path)

    enhancer = ImageEnhance.Contrast(image)

    enhanced_image = enhancer.enhance(contrast_factor)

    enhanced_image.save(output_path)

    print("Nuotrauka atnaujinta ir išsaugota.")

image_path = "kate2.jpg"
output_path = "atnaujinta_nuotrauka.jpg"
contrast_factor = 1.5

apply_contrast(image_path, output_path, contrast_factor)
