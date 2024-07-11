import cv2

def pencil_sketch(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)

    # Blur the inverted image using a Gaussian filter
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX=0, sigmaY=0)

    # Invert the blurred image
    inverted_blurred_image = cv2.bitwise_not(blurred_image)

    # Create the pencil sketch by dividing the grayscale image by the inverted blurred image
    sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

    # Save the result
    cv2.imwrite(output_path, sketch)

    # Display the result
    cv2.imshow('Original Image', image)
    cv2.imshow('Pencil Sketch', sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
pencil_sketch('Jagadeesh.jpg', 'output_sketch.png')
