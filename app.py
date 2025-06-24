import streamlit as st
import pandas as pd

# Updated color data with refined moods/vibes
color_data = [
    ("Red", "Passion, Energy, Urgency", "#FF0000"),
    ("Crimson", "Romance, Intensity, Luxury", "#DC143C"),
    ("Cherry Red", "Youthful, Playful, Excitement", "#D2042D"),
    ("Burnt Orange", "Warmth, Earthy, Comfort", "#CC5500"),
    ("Coral", "Friendly, Vibrant, Feminine", "#FF7F50"),
    ("Peach", "Softness, Innocence, Calm", "#FFE5B4"),
    ("Golden Yellow", "Success, Optimism, Happiness", "#FFD700"),
    ("Lemon Yellow", "Cheerful, Energetic, Youthful", "#FFF700"),
    ("Buttercream", "Cozy, Delicate, Nostalgic", "#FFF1C1"),
    ("Lime Green", "Freshness, Energy, Fun", "#32CD32"),
    ("Forest Green", "Stability, Growth, Nature", "#228B22"),
    ("Olive Green", "Earthy, Vintage, Natural", "#808000"),
    ("Navy Blue", "Trust, Authority, Professionalism", "#000080"),
    ("Teal", "Calm, Clarity, Sophistication", "#008080"),
    ("Ice Blue", "Cool, Calm, Minimal", "#AFEEEE"),
    ("Lavender", "Relaxing, Feminine, Dreamy", "#E6E6FA"),
    ("Deep Purple", "Luxury, Royalty, Mystery", "#673AB7"),
    ("Blush Pink", "Sweet, Soft, Romantic", "#FFC0CB"),
    ("Hot Pink", "Bold, Confident, Playful", "#FF69B4"),
    ("Jet Black", "Power, Sophistication, Modernity", "#343434"),
    ("Ivory", "Classic, Pure, Soft", "#FFFFF0"),
    ("Ash Gray", "Neutral, Balanced, Industrial", "#B2BEB5"),
    ("Taupe", "Warm, Neutral, Cozy", "#483C32"),
    ("Charcoal", "Strong, Professional, Serious", "#36454F"),
    ("Chocolate Brown", "Earthy, Reliable, Warm", "#7B3F00"),
    ("Pastel Blue", "Gentle, Calm, Innocent", "#AEC6CF"),
    ("Sky Blue", "Hopeful, Open, Free", "#87CEEB"),
    ("Magenta", "Creative, Bold, Energetic", "#FF00FF"),
    ("Cyan", "Fresh, Digital, Clean", "#00FFFF"),
    ("Beige", "Simple, Understated, Natural", "#F5F5DC"),
    ("Maroon", "Deep, Elegant, Serious", "#800000"),
    ("Periwinkle", "Artistic, Quirky, Calm", "#CCCCFF"),
    ("Mint Green", "Fresh, Innocent, Natural", "#98FF98"),
    ("Cream", "Soft, Vintage, Delicate", "#FFFDD0"),
    ("Mauve", "Sophisticated, Calm, Romantic", "#E0B0FF"),
    ("Terracotta", "Warm, Earthy, Bohemian", "#E2725B"),
    ("Midnight Blue", "Deep, Mysterious, Elegant", "#191970"),
    ("Plum", "Sensual, Lush, Sophisticated", "#8E4585"),
]

# Convert to DataFrame
df = pd.DataFrame(color_data, columns=["Color", "Mood / Vibe", "Hex Code"])

# Title and subtitle (centered)
st.markdown("<h1 style='text-align: center;'>🎨 ColorSense</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Find colors based on the mood you want to express</p>", unsafe_allow_html=True)

# Text input for mood
typed_mood = st.text_input("Type a Mood / Vibe:").strip().lower()

# Filter colors by mood keyword
if typed_mood:
    filtered = df[df["Mood / Vibe"].str.lower().str.contains(typed_mood)]

    if filtered.empty:
        st.warning("No colors found for that mood. Try another keyword.")
    else:
        for _, row in filtered.iterrows():
            st.markdown(f"**{row['Color']}** — `{row['Hex Code']}`")
            st.markdown(
                f"<div style='width: 60px; height: 30px; background-color: {row['Hex Code']}; "
                "border: 1px solid #000; margin-bottom: 10px;'></div>",
                unsafe_allow_html=True,
            )
else:
    st.info("Type a mood (e.g., calm, energetic, romantic) to see matching colors.")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center;'>Designed by Athiramol PS – June 24, 2025</div>", unsafe_allow_html=True)
