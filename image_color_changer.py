import streamlit as st
import cv2
import numpy as np

def change_color(image, color):
  """Changes the color of the object in the image.

  Args:
    image: A numpy array representing the image.
    color: A tuple of (R, G, B) values representing the desired color.

  Returns:
    A numpy array representing the image with the changed color.
  """

  # Convert the image to HSV color space.
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

  # Hue is the hue angle of the color.
  hue = color[0]

  # Saturation is the intensity of the color.
  saturation = color[1]

  # Value is the brightness of the color.
  value = color[2]

  # Set the hue of the object to the desired hue.
  hsv[:, :, 0] = hue

  # Convert the image back to BGR color space.
  bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

  return bgr

# Create a Streamlit app.
st.title("Image Color Changer")

# Upload the image.
uploaded_image = st.file_uploader("Upload an image:", type=["png", "jpg"])

# If the image is uploaded, display it and allow the user to change its color.
if uploaded_image is not None:

  # Convert the uploaded_image object to a string.
  image_path = str(uploaded_image)

  # Load the image.
  image = cv2.imread(image_path)

  # Display the image.
  st.image(image, use_column_width=True)

  # Create a list of color tabs.
  color_tabs = st.tabs(["Red", "Green", "Blue"])

  # Display the selected color tab.
  selected_color_tab = color_tabs.active_tab

  # Change the color of the object in the image based on the selected color tab.
  if selected_color_tab == "Red":
    color = (255, 0, 0)
  elif selected_color_tab == "Green":
    color = (0, 255, 0)
  elif selected_color_tab == "Blue":
    color = (0, 0, 255)

  # Change the color of the object in the image.
  changed_image = change_color(image, color)

  # Display the changed image.
  st.image(changed_image, use_column_width=True)
