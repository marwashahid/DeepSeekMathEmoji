
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Emoji Math Solver",
    page_icon="💬",
    layout="centered"
)

# Add a title and description
st.title("Emoji Math Solver")
st.write("Enter your problem below and get a response!")

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get user input
user_input = st.chat_input("Enter your equation (e.g. 🥭 ÷ (🍋 - 🍊) = 2, 🍋 = 7, 🍊 = 3)")

# Process user input and generate response
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Generate response using your model
    with st.spinner("DeepSeekMath is thinking..."):
        try:
            # Call your process_input function
            response = process_input(user_input)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            # Display assistant response
            with st.chat_message("assistant"):
                st.write(response)
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
# Add a sidebar with additional options
with st.sidebar:
    st.header("Options")
    
    # Add a button to clear chat history
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()
    
    # Add information about the app
    st.markdown("---")
    st.markdown("### About")
    st.write("""
    This app uses a language model to generate responses.
    The model processes your input and generates text based on its training.
    """)
