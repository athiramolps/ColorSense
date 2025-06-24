import streamlit as st
import pandas as pd

# Data
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

# Title and subtitle
st.title("🎨 ColorSense")
st.caption("Find colors based on the mood you want to express")

# Dropdown menu for moods
mood_list = df["Mood / Vibe"].unique()
selected_mood = st.selectbox("Choose a Mood / Vibe:", sorted(mood_list))

# Filter colors by mood
filtered = df[df["Mood / Vibe"] == selected_mood]

# Show results
for _, row in filtered.iterrows():
    st.markdown(f"**{row['Color']}** — `{row['Hex Code']}`")
    st.color_picker("", row['Hex Code'], disabled=True)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center;'>Designed by Athiramol PS – June 24, 2025</div>", unsafe_allow_html=True)
