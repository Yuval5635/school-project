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
st.write("Duplicate rows: 5")
st.write("Missing values: 0")

st.subheader("Dataset Columns")

st.write("Result: The result of the chess game.")
st.write("WhiteElo: The ELO rating of the player playing White.")
st.write("BlackElo: The ELO rating of the player playing Black.")
st.write("Time: The initial time control of the game.")
st.write("AddedTime: The additional time given to players during the game.")
st.write("NumberOfMoves: The number of moves played in the game.")

st.subheader("Average Values")

st.write("WhiteElo: 1630.55")
st.write("BlackElo: 1625.27")
st.write("Time: 288.82")
st.write("AddedTime: 2.09")
st.write("NumberOfMoves: 33.97")

st.subheader("Additional Statistical Information")

st.write("WhiteElo - minimum: 849, maximum: 2579")
st.write("BlackElo - minimum: 850, maximum: 2579")
st.write("Time - minimum: 0, maximum: 10800")
st.write("AddedTime - minimum: 0, maximum: 180")
st.write("NumberOfMoves - minimum: 1, maximum: 170")

# 3. Prediction goal
st.header("3. Prediction Goal")

st.write("Our goal is to predict the ELO rating of the White player.")

st.write("Y (target): WhiteElo")

st.write("X (features):")
st.write("- BlackElo")
st.write("- Result")
st.write("- Time")
st.write("- AddedTime")
st.write("- NumberOfMoves")

st.write("Reasons for choosing these columns:")
st.write(
    "BlackElo describes the skill level of the opponent. Result tells us "
    "whether the White player won, lost, or drew. Time and AddedTime "
    "describe the time conditions of the game. NumberOfMoves may provide "
    "information about the length and style of the game, which could help "
    "identify patterns related to player strength."
)

st.write(
    "A note about NumberOfMoves: the number of moves does not directly "
    "show how quickly players made their moves. It shows how long the game "
    "lasted in moves. To measure playing speed, we would need information "
    "about the actual time each player spent thinking."
)
