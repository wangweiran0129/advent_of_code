import pandas as pd
import numpy as np

def read_input(input_file):
    
    with open(input_file, "r") as file:
        content = file.read()
    
    return content


def cal_diff(input_content):

    rows = [line.split() for line in input_content.strip().split("\n")]
    df = pd.DataFrame(rows, columns=["First", "Second"]).astype(int)

    df["First"] = sorted(df["First"])
    df["Second"] = sorted(df["Second"])

    df["Difference"] = abs(df["Second"] - df["First"])
    total_difference = df["Difference"].sum()

    return total_difference


def cal_similarity_score(input_content):

    rows = [line.split() for line in input_content.strip().split("\n")]
    df = pd.DataFrame(rows, columns=["First", "Second"]).astype(int)
    counts = df["Second"].value_counts()

    # Map the counts to the "First" column
    df["Frequency"] = df["First"].map(counts).fillna(0).astype(int)
    df["Similarity"] = df["First"] * df["Frequency"]

    total_similarity_score = df["Similarity"].sum()
    
    return total_similarity_score


if __name__ == "__main__":
    input_file = "input.txt"
    input_content = read_input(input_file)
    # part1_result = cal_diff(input_content)
    # print("part 1 result: ", part1_result)
    part2_result = cal_similarity_score(input_content)
    print("part 2 result: \n", part2_result)