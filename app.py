import streamlit as st
import ollama

st.set_page_config(page_title="Social Media Caption Generator", page_icon="📱", layout="centered")

st.title("📱 Social Media Caption Generator")
st.caption("PS #05 | Arvind Pramod Malvade (Roll No: 05, LY-AIA-04)")

description = st.text_area(
    "Post Description",
    placeholder="e.g., Just completed my final-year Generative AI mini-project using local LLMs and Streamlit!",
    height=120
)

platform = st.selectbox(
    "Select Platform",
    ["Instagram", "LinkedIn", "X (Twitter)", "All Platforms"]
)

PLATFORM_PROMPTS = {
    "Instagram": (
        "You are an expert Instagram content creator. Based on the user's description, "
        "generate 3 engaging, aesthetic captions with relevant emojis. Keep each caption punchy "
        "(under 150 words) and include 8-10 trending, relevant hashtags at the end of each caption."
    ),
    "LinkedIn": (
        "You are a professional LinkedIn content strategist. Based on the user's description, "
        "generate 3 insightful, professional posts with a strong hook and clear takeaway. "
        "Keep each post between 100-200 words and include 4-5 industry-relevant hashtags at the end of each."
    ),
    "X (Twitter)": (
        "You are a viral X (Twitter) copywriter. Based on the user's description, "
        "generate 3 crisp, high-impact tweets. Strict constraint: each tweet INCLUDING hashtags "
        "must be under 280 characters. Include 2-3 relevant hashtags per tweet."
    )
}

def generate_captions(desc: str, plat: str) -> str:
    system_instruction = PLATFORM_PROMPTS[plat]
    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Post Description: {desc}\n\nProvide 3 numbered options clearly separated."}
        ]
    )
    return response["message"]["content"]

if st.button("Generate Captions", type="primary"):
    if not description.strip():
        st.warning("Please enter a short description of your post first.")
    else:
        targets = ["Instagram", "LinkedIn", "X (Twitter)"] if platform == "All Platforms" else [platform]
        for target in targets:
            with st.spinner(f"Generating {target} captions..."):
                try:
                    output = generate_captions(description, target)
                    st.subheader(f"{target} Options")
                    st.markdown(output)
                    st.divider()
                except Exception as e:
                    st.error(f"Error connecting to Ollama: {e}")