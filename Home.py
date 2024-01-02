import streamlit as st

# Set the page config
st.set_page_config(page_title="DocsVisqa", page_icon='✨')

# Add a header
st.header("DocsVisqa")

# Add a description
st.markdown("""
This project allows you to search in your PDF using the Gemini Pro API, 
search in your image by Gemini Pro, or chat using Gemini Pro.
""")





# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Load Animation
animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)

















# Create columns for the buttons
col1, col2, col3 = st.columns(3)

# Add the buttons
with col1:
    if st.button('Talk with Image'):
        # Redirect to the 'Talk with Image' page
        st.write('Redirecting to the Talk with Image page...')
with col2:
    if st.button('Talk with PDF'):
        # Redirect to the 'Talk with PDF' page
        st.write('Redirecting to the Talk with PDF page...')
with col3:
    if st.button('Chatbot'):
        # Redirect to the 'Chatbot' page
        st.write('Redirecting to the Chatbot page...')


# Define a list of pages
pages = ["Home", "Talk with Image", "Talk with PDF", "Chatbot"]

# Use a selectbox for the page selection
current_page = st.sidebar.selectbox("Select the page:", pages)

# Display the selected page
if current_page == "Talk with Image":
    # Import and display the 'Talk with Image' page
    import pages.Talk_With_Image as Talk_With_Image
    Talk_With_Image.display()
elif current_page == "Talk with PDF":
    # Import and display the 'Talk with PDF' page
    import pages.Talk_With_PDF as Talk_With_PDF
    Talk_With_PDF.display()
elif current_page == "Chatbot":
    # Import and display the 'Chatbot' page
    import pages.Chatbot as Chatbot
    Chatbot.display()