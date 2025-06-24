import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="ColorSense", layout="wide")

# Color + Mood Data
color_data = [
    ("Red", "Passion, Energy, Urgency", "#FF0000"),
    ("Crimson", "Romance, Intensity, Luxury", "#DC143C"),
    ("Cherry Red", "Youthful, Playful, Excitement", "#D2042D"),
    ("Burnt Orange", "Rustic, Earthy, Warmth", "#CC5500"),
    ("Coral", "Vibrant, Friendly, Feminine", "#FF7F50"),
    ("Peach", "Softness, Innocence, Calm", "#FFE5B4"),
    ("Golden Yellow", "Success, Wealth, Radiance", "#FFD700"),
    ("Lemon Yellow", "Cheerful, Youthful, Zesty", "#FFF700"),
    ("Buttercream", "Delicate, Cozy, Nostalgic", "#FFF1C1"),
    ("Lime Green", "Fresh, Energetic, Fun", "#32CD32"),
    ("Forest Green", "Nature, Stability, Maturity", "#228B22"),
    ("Olive Green", "Earthy, Grounded, Vintage", "#808000"),
    ("Navy Blue", "Trust, Authority, Intelligence", "#000080"),
    ("Teal", "Clarity, Serenity, Trendy", "#008080"),
    ("Ice Blue", "Cool, Calm, Minimal", "#AFEEEE"),
    ("Lavender", "Relaxing, Feminine, Dreamy", "#E6E6FA"),
    ("Deep Purple", "Royalty, Elegance, Mystery", "#673AB7"),
    ("Blush Pink", "Sweet, Soft, Romantic", "#FFC0CB"),
    ("Hot Pink", "Bold, Youthful, Confident", "#FF69B4"),
    ("Jet Black", "Luxury, Power, Modernity", "#343434"),
    ("Ivory", "Classic, Soft, Clean", "#FFFFF0"),
    ("Ash Gray", "Industrial, Balanced, Reserved", "#B2BEB5"),
    ("Taupe", "Neutral, Warm, Cozy", "#483C32"),
    ("Charcoal", "Professional, Strong, Neutral", "#36454F"),
    ("Chocolate Brown", "Earthy, Reliable, Rich", "#7B3F00"),
    ("Pastel Blue", "Babyish, Calm, Gentle", "#AEC6CF"),
    ("Sky Blue", "Hopeful, Free, Open", "#87CEEB"),
    ("Magenta", "Energetic, Bold, Creative", "#FF00FF"),
    ("Cyan", "Digital, Clean, Futuristic", "#00FFFF"),
    ("Beige", "Understated, Natural, Simple", "#F5F5DC"),
    ("Maroon", "Elegant, Classic, Depth", "#800000"),
    ("Periwinkle", "Quirky, Fresh, Artistic", "#CCCCFF"),
    ("Mint Green", "Refreshing, Innocent, Natural", "#98FF98"),
    ("Cream", "Subtle, Vintage, Delicate", "#FFFDD0"),
    ("Mauve", "Sophisticated, Calm, Romantic", "#E0B0FF"),
    ("Terracotta", "Bohemian, Warm, Earthy", "#E2725B"),
    ("Midnight Blue", "Deep, Mysterious, Elegant", "#191970"),
    ("Plum", "Lush, Sensual, Sophisticated", "#8E4585"),
]

# Convert to DataFrame
df = pd.DataFrame(color_data, columns=["Color", "Mood / Vibe", "Hex Code"])

# App title and caption
st.markdown("""
    <h1 style='text-align: center; color: #9C27B0;'>🎨 ColorSense</h1>
    <p style='text-align: center; font-size: 18px;'>
        A mood-to-color matcher for creating emotionally resonant dashboards and interfaces.
    </p>
""", unsafe_allow_html=True)

# Mood input
typed_mood = st.text_input("Type a Mood / Vibe (e.g., calm, romantic, energetic):").strip().lower()

# Results
if typed_mood:
    filtered = df[df["Mood / Vibe"].str.lower().str.contains(typed_mood)]
    
    if filtered.empty:
        st.warning("No colors found for that mood. Try a different keyword.")
    else:
        for _, row in filtered.iterrows():
            st.markdown(f"### {row['Color']} — `{row['Hex Code']}`")
            st.markdown(f"""
                <div style='
                    background-color: {row['Hex Code']};
                    width: 100%;
                    height: 100px;
                    border-radius: 10px;
                    border: 2px solid #333;
                    margin-bottom: 20px;
                '></div>
            """, unsafe_allow_html=True)
else:
    st.info("Enter a mood to discover its matching color.")

# Footer
st.markdown("""
    <hr style="margin-top: 50px;">
    <div style="text-align: center; font-size: 14px; color: gray;">
        Designed by <strong>Athiramol PS</strong> – June 24, 2025
    </div>
""", unsafe_allow_html=True)
