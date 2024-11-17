import cv2
import numpy as np

def image_interpolation(image, scale_factor=2):
    """Perform efficient linear interpolation using OpenCV by resizing the image."""
    # Ensure the image is not empty
    if image is None:
        raise ValueError("Input image is empty or not found!")
    
    # Get the current dimensions of the image
    original_height, original_width = image.shape[:2]
    print(f"Original Image Dimensions: Height = {original_height}, Width = {original_width}")
    
    # Use the provided scale_factor to resize the image
    new_height, new_width = int(original_height * scale_factor), int(original_width * scale_factor)
    interpolated_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    
    print(f"Interpolated Image Dimensions: Height = {new_height}, Width = {new_width}")
    
    # Return the interpolated image
    return interpolated_image

def check_if_interpolated(original_image, interpolated_image, scale_factor=2):
    """Check if an image is interpolated by comparing dimensions."""
    # Compare the dimensions of the original and interpolated images
    original_height, original_width = original_image.shape[:2]
    interpolated_height, interpolated_width = interpolated_image.shape[:2]
    
    # Check if the dimensions match the expected scale factor
    expected_height = int(original_height * scale_factor)
    expected_width = int(original_width * scale_factor)
    
    if interpolated_height == expected_height and interpolated_width == expected_width:
        print(f"The image has been successfully interpolated (scaled by {scale_factor}x).")
        return True
    else:
        print(f"The image has not been interpolated correctly.")
        return False

def load_image(image_path):
    """Helper function to load an image and handle errors."""
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Error: Unable to load image from the path: {image_path}")
    
    return image

def save_image(image, output_path):
    """Save the processed image to a file."""
    cv2.imwrite(output_path, image)
    print(f"Image saved successfully at: {output_path}")

def main():
    # Provide the path to your image
    image_path = 'Screenshot 2024-11-15 161526.png'  # Replace this with the correct path to your image
    
    # Define the scale factor dynamically based on your needs
    scale_factor = 4  # Set the scale factor to whatever you need (e.g., 1.5, 2, etc.)
    
    try:
        # Step 1: Load the image
        original_image = load_image(image_path)
        
        # Step 2: Interpolate the image (increase its size) with the dynamic scale factor
        interpolated_image = image_interpolation(original_image, scale_factor)
        
        # Step 3: Check if the image has been interpolated
        if check_if_interpolated(original_image, interpolated_image, scale_factor):
            # Step 4: Save the interpolated image
            save_image(interpolated_image, 'interpolated_image.png')
            
            # Optional: Display the original and interpolated images (for visual verification)
            cv2.imshow('Original Image', original_image)
            cv2.imshow('Interpolated Image', interpolated_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error: {e}")

# Run the main function
if __name__ == "__main__":
    main()
