import os
from PIL import Image

# 🔧 Configuration
input_folder = "C:\\Users\\HP\\Documents\\Diff_Projects\\Elevate-Lab\\Task-7\\input_images"      
output_folder = "C:\\Users\\HP\\Documents\\Diff_Projects\\Elevate-Lab\\Task-7\\resized_images"   
new_size = (300, 300)             
output_format = "JPEG"            

# 📂 Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# 🧠 Process each image in input folder
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    # ✅ Check if it's an image
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        try:
            # Open image
            img = Image.open(file_path)

            # Resize image
            img_resized = img.resize(new_size)

            # Convert to desired format
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")

            # Save resized image
            img_resized.save(output_path, output_format)
            print(f"✅ Resized and saved: {output_path}")

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

print("\n🎉 All images resized and saved successfully!")
