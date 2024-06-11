import streamlit as st
import math

def calculate_earthquake_parameters(latitude, longitude, depth):
    """
    Calculate XM, MD, and Richter values based on latitude, longitude, and depth.
    
    Parameters:
    latitude (float): Latitude of the earthquake epicenter.
    longitude (float): Longitude of the earthquake epicenter.
    depth (float): Depth of the earthquake in kilometers.
    
    Returns:
    dict: A dictionary containing XM, MD, and Richter values.
    """
    
    # Mock calculations for demonstration purposes
    # Replace these with actual formulas or data sources if available
    
    # XM (eXtended Magnitude) - Placeholder formula
    xm = (latitude ** 2 + longitude ** 2 + depth ** 2) ** 0.5
    
    # MD (Magnitude Depth) - Placeholder formula
    md = math.log1p(abs(latitude) + abs(longitude) + depth)
    
    # Richter scale (Richter Magnitude) - Placeholder formula
    if depth > 700:
        richter = 8.0  # Deep earthquakes tend to be very strong
    elif depth > 300:
        richter = 7.0  # Intermediate-depth earthquakes
    else:
        richter = 6.0  # Shallow earthquakes are often less intense
    
    return {
        'XM': round(xm, 2),
        'MD': round(md, 2),
        'Richter': round(richter, 2)
    }

def main():
    st.title("Earthquake Parameters Calculator")
    
    # User input fields
    latitude = st.number_input("Enter latitude:")
    longitude = st.number_input("Enter longitude:")
    depth = st.number_input("Enter depth (km):")
    
    # Calculate earthquake parameters
    parameters = calculate_earthquake_parameters(latitude, longitude, depth)
    
    # Display results
    st.write(f"XM: {parameters['XM']}")
    st.write(f"MD: {parameters['MD']}")
    st.write(f"Richter: {parameters['Richter']}")

if __name__ == "__main__":
    main()
