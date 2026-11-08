import streamlit as st

st.title("Chess Games Dataset Analysis")

# 1. Dataset explanation
st.header("1. About the Dataset")

st.write(
    "The dataset is called ChessGames.csv. It contains information "
    "about chess games."
)

st.write(
    "Each row represents one chess game between two players: "
    "White and Black."
)

# 2. Information about the data
st.header("2. Dataset Information")

st.write("Number of rows: 40,000")
st.write("Number of columns: 6")

st.subheader("Dataset Columns")

st.write("Result: The result of the chess game. The values are -1, 0, and 1.")
st.write("WhiteElo: The ELO rating of the player playing White.")
st.write("BlackElo: The ELO rating of the player playing Black.")
st.write("Time: The time control of the game.")
st.write("AddedTime: The additional time given to players during the game.")
st.write("NumberOfMoves: The number of moves played in the game.")

st.subheader("Missing Values")

st.write(
    "The exact number of missing values in each column is not available "
    "in the information currently known about the dataset."
)

st.subheader("Average Values")

st.write(
    "The exact averages are not available in the information currently "
    "known about the dataset. Averages can be calculated for numeric "
    "columns such as WhiteElo, BlackElo, and NumberOfMoves."
)

# 3. Prediction goal
st.header("3. Prediction Goal")

st.write(
    "Our goal is to predict the result of a chess game."
)

st.write("Y (target): Result")

st.write("X (features):")
st.write("- WhiteElo")
st.write("- BlackElo")
st.write("- Time")
st.write("- AddedTime")

st.write("Reasons for choosing these columns:")
st.write(
    "The ELO ratings describe the skill level of both players. "
    "The time control and additional time describe the time conditions "
    "of the game. These details are known before the game starts and "
    "may help predict its result."
)

st.write(
    "NumberOfMoves is not included as a prediction feature because "
    "the number of moves is only known after the game has finished."
)
