from PIL import Image
import os


def convert_to_grayscale(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # List all the .jpg files in the input folder
    jpeg_files = [
        file for file in os.listdir(input_folder) if file.lower().endswith(".jpg")
    ]

    # Convert each JPEG file to grayscale and save as PNG in the output folder
    for jpeg_file in jpeg_files:
        input_path = os.path.join(input_folder, jpeg_file)
        output_path = os.path.join(
            output_folder, os.path.splitext(jpeg_file)[0] + ".png"
        )

        with Image.open(input_path) as img:
            # Convert to grayscale
            gray_img = img.convert("L")

            # Save as PNG
            gray_img.save(output_path)


if __name__ == "__main__":
    input_folder = (
        "./Module 8/"  # Replace with the path to the folder containing the JPEG files
    )
    output_folder = (
        "./Module 8/Grayscale_Images"  # Name of the new folder for grayscale PNG files
    )
    convert_to_grayscale(input_folder, output_folder)
