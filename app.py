import streamlit as st
import json
from model import probe_model_5l_profit  # Import the function from model.py

def color_flag(value):
    """Return the color representation based on the flag value."""
    if value == 1:
        return "GREEN"
    elif value == 2:
        return "AMBER"
    elif value == 0:
        return "RED"
    elif value == 3:
        return "MEDIUM_RISK"
    elif value == 4:
        return "WHITE"
    else:
        return "UNKNOWN"

def main():
    st.title("Financial Data Processing and Results")

    # File uploader for JSON file
    uploaded_file = st.file_uploader("Choose a JSON file", type="json")

    if uploaded_file is not None:
        # Display a submit button
        if st.button("Submit"):
            try:
                # Load the JSON data
                data = json.load(uploaded_file)
                
                # Call the function from model.py
                result = probe_model_5l_profit(data["data"])
                
                # Extract flags
                flags = result.get("flags", {})
                
                # Display results
                st.write("Data uploaded and processed successfully!")
                st.write("Results:")
                
                for flag_name, flag_value in flags.items():
                    color = color_flag(flag_value)
                    st.write(f"{flag_name}: {color}")

                    # Display color-coded flag
                    if color == "GREEN":
                        st.markdown(f"<div style='background-color: green; color: white; padding: 5px;'>{flag_name}</div>", unsafe_allow_html=True)
                    elif color == "AMBER":
                        st.markdown(f"<div style='background-color: orange; color: black; padding: 5px;'>{flag_name}</div>", unsafe_allow_html=True)
                    elif color == "RED":
                        st.markdown(f"<div style='background-color: red; color: white; padding: 5px;'>{flag_name}</div>", unsafe_allow_html=True)
                    elif color == "MEDIUM_RISK":
                        st.markdown(f"<div style='background-color: yellow; color: black; padding: 5px;'>{flag_name}</div>", unsafe_allow_html=True)
                    elif color == "WHITE":
                        st.markdown(f"<div style='background-color: white; color: black; padding: 5px;'>{flag_name}</div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div style='background-color: grey; color: white; padding: 5px;'>{flag_name}</div>", unsafe_allow_html=True)

            except json.JSONDecodeError:
                st.error("Error: The uploaded file is not a valid JSON.")
            except KeyError:
                st.error("Error: The uploaded JSON does not contain the required 'data' key.")
            except Exception as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
