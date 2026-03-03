import streamlit as st
import requests
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="SHL Assessment Recommender",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Use localhost for local testing, but allow easy switching for cloud deployment
API_URL = "http://localhost:8000/recommend"

# 2. Header Section
st.title("🎯 SHL Assessment Recommendation Engine")
st.markdown("""
Welcome to the intelligent assessment routing tool. 
Paste a **Job Description** or type a **Natural Language Query** below, and the RAG engine will fetch the most highly balanced and relevant SHL assessments.
""")

st.divider()

# 3. User Input
query = st.text_area(
    "Job Description / Query", 
    height=150, 
    placeholder="e.g., Looking to hire mid-level professionals who are proficient in Python, SQL and JavaScript, but also need strong leadership and communication skills."
)

# 4. Action Button & Processing
if st.button("Generate Recommendations", type="primary", use_container_width=True):
    if not query.strip():
        st.warning("Please enter a query or job description to proceed.")
    else:
        with st.spinner("Analyzing query, searching vector space, and balancing domains..."):
            try:
                # Send the POST request to your FastAPI backend
                response = requests.post(API_URL, json={"query": query}, timeout=60)
                
                if response.status_code == 200:
                    data = response.json()
                    assessments = data.get("recommended_assessments", [])
                    
                    if assessments:
                        st.success(f"Successfully retrieved {len(assessments)} balanced recommendations!")
                        
                        # Convert JSON to a Pandas DataFrame for clean rendering
                        df = pd.DataFrame(assessments)
                        
                        # Reorder columns for better UX readability
                        df = df[['name', 'test_type', 'duration', 'adaptive_support', 'remote_support', 'description', 'url']]
                        
                        # 5. Render the Interactive Data Table
                        st.dataframe(
                            df,
                            column_config={
                                "name": st.column_config.TextColumn("Assessment Name", width="medium"),
                                "test_type": st.column_config.ListColumn("Category"),
                                "duration": st.column_config.NumberColumn("Duration (min)", format="%d"),
                                "adaptive_support": st.column_config.TextColumn("Adaptive?"),
                                "remote_support": st.column_config.TextColumn("Remote?"),
                                "description": st.column_config.TextColumn("Description", width="large"),
                                "url": st.column_config.LinkColumn("SHL Link", display_text="View Test")
                            },
                            hide_index=True,
                            use_container_width=True
                        )
                    else:
                        st.info("No relevant assessments found matching those criteria.")
                else:
                    st.error(f"API Error {response.status_code}: {response.text}")
                    
            except requests.exceptions.ConnectionError:
                st.error("Connection Error: Could not reach the FastAPI backend. Please ensure it is running on port 8000.")