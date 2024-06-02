import os

import streamlit as st
# from crewai import Agent, Task, Crew

st. write("yesssss")


# Streamlit interface
def run_crewai_app():
    st.title("AI Agent Business Product Launch")
    with st.expander("About the Team:"):
        st.subheader("Diagram")
        left_co, cent_co,last_co = st.columns(3)
        with cent_co:
            # st.image("my_img.png")
            st.write("yes")

        st.subheader("Market Research Analyst")
        st.text("""       
        Role = Market Research Analyst
        Goal = Analyze the market demand for {product_name} and suggest marketing strategies
        Backstory = Expert at understanding market demand, target audience, 
                    and competition for products like {product_name}. 
                    Skilled in developing marketing strategies 
                    to reach a wide audience.
        Task = Analyze the market demand for {product_name}. Current month is Jan 2024.
               Write a report on the ideal customer profile and marketing 
               strategies to reach the widest possible audience. 
               Include at least 10 bullet points addressing key marketing areas. """)
        
        st.subheader("Technology Expert")
        st.text("""       
        Role = Technology Expert
        Goal = Assess technological feasibilities and requirements for producing high-quality {product_name}
        Backstory = Visionary in current and emerging technological trends, 
                    especially in products like {product_name}. 
                    Identifies which technologies are best suited 
                    for different business models. 
        Task = Assess the technological aspects of manufacturing 
               high-quality {product_name}. Write a report detailing necessary 
               technologies and manufacturing approaches. 
               Include at least 10 bullet points on key technological areas.""")

        st.subheader("Business Development Consultant")
        st.text("""       
        Role = Business Development Consultant 
        Goal= Evaluate the business model for {product_name}
              focusing on scalability and revenue streams
        Backstory = Seasoned in shaping business strategies for products like {product_name}. 
                    Understands scalability and potential 
                    revenue streams to ensure long-term sustainability.
        Task = Summarize the market and technological reports 
               and evaluate the business model for {product_name}. 
               Write a report on the scalability and revenue streams 
               for the product. Include at least 10 bullet points 
               on key business areas. Give Business Plan, 
               Goals and Timeline for the product launch. Current month is Jan 2024. """)
    
    product_name = st.text_input("Enter a product name to analyze the market and business strategy.")

    if st.button("Run Analysis"):
        # Placeholder for stopwatch
        stopwatch_placeholder = st.empty()
        
        # Start the stopwatch
        start_time = time.time()
        with st.expander("Processing!"):
            sys.stdout = StreamToExpander(st)
            with st.spinner("Generating Results"):
                crew_result = create_crewai_setup(product_name)

        # Stop the stopwatch
        end_time = time.time()
        total_time = end_time - start_time
        stopwatch_placeholder.text(f"Total Time Elapsed: {total_time:.2f} seconds")

        st.header("Tasks:")
        st.table({"Tasks" : task_values})

        st.header("Results:")
        st.markdown(crew_result)

if __name__ == "__main__":
    run_crewai_app()
