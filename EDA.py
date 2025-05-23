#!/usr/bin/env python
# coding: utf-8

# Premier League 2021-22 Season Analysis
# This script analyzes various aspects of Premier League teams' performance including:
# - Expected goals (xG) vs Expected goals against (xGA)
# - Offensive efficiency and chance creation
# - Defensive performance and goalkeeper impact

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set plot style
plt.style.use("seaborn-v0_8")
sns.set_palette("husl")


# Helper Functions
def display_df_info(df, name, show_head=True, show_info=True, show_describe=True):
    """Display common DataFrame information."""
    print(f"\n{name}:")
    if show_head:
        print("\nFirst few rows:")
        print(df.head())
    if show_info:
        print("\nDataFrame Info:")
        print(df.info())
    if show_describe:
        print("\nStatistical Description:")
        print(df.describe())


def clean_dataframe(df, drop_cols=None, rename_cols=None, fill_na=None):
    """Clean DataFrame by dropping columns, renaming columns, and filling NA values."""
    if drop_cols:
        # Only drop columns that exist in the DataFrame
        existing_cols = [col for col in drop_cols if col in df.columns]
        df = df.drop(columns=existing_cols)
    if rename_cols:
        # Only rename columns that exist in the DataFrame
        existing_rename = {k: v for k, v in rename_cols.items() if k in df.columns}
        df = df.rename(columns=existing_rename)
    if fill_na:
        # Only fill NA for columns that exist in the DataFrame
        existing_fill = {k: v for k, v in fill_na.items() if k in df.columns}
        df = df.fillna(existing_fill)
    return df


def plot_scatter(df, x, y, title, xlabel=None, ylabel=None, hue=None, figsize=(12, 8)):
    """Create a standardized scatter plot."""
    plt.figure(figsize=figsize)
    sns.scatterplot(data=df, x=x, y=y, hue=hue, s=100)
    plt.title(title, fontsize=14, pad=20)
    if xlabel:
        plt.xlabel(xlabel, fontsize=12)
    if ylabel:
        plt.ylabel(ylabel, fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_bar(
    df,
    x,
    y,
    title,
    xlabel=None,
    ylabel=None,
    hue=None,
    figsize=(12, 8),
    palette="viridis",
    rotate_xlabels=True,
):
    """Create a standardized bar plot."""
    plt.figure(figsize=figsize)
    sns.barplot(data=df, x=x, y=y, hue=hue, palette=palette)
    plt.title(title, fontsize=14, pad=20)
    if xlabel:
        plt.xlabel(xlabel, fontsize=12)
    if ylabel:
        plt.ylabel(ylabel, fontsize=12)
    if rotate_xlabels:
        plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(
    df, columns=None, title="Correlation Matrix", figsize=(10, 8), cmap="coolwarm"
):
    """Create a correlation heatmap."""
    if columns:
        df = df[columns]
    corr = df.corr()
    plt.figure(figsize=figsize)
    sns.heatmap(corr, annot=True, cmap=cmap, center=0, fmt=".2f")
    plt.title(title, fontsize=14, pad=20)
    plt.tight_layout()
    plt.show()


def calculate_efficiency_metrics(df, x_col, y_col, new_col_name):
    """Calculate efficiency metrics and add them to the dataframe."""
    df[new_col_name] = df[y_col] / df[x_col]
    return df


def load_csv_file(filename, required_columns=None):
    """Load a CSV file with error handling and column validation."""
    try:
        df = pd.read_csv(filename)
        if required_columns:
            missing_cols = [col for col in required_columns if col not in df.columns]
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")
        return df
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Skipping this dataset.")
        return None
    except Exception as e:
        print(f"Error loading {filename}: {str(e)}")
        return None


# Load and clean datasets
print("Loading and cleaning datasets...")

# Overall stats
overall = load_csv_file(
    "overall.csv", required_columns=["Squad", "GF", "GA", "xG", "xGA"]
)
if overall is not None:
    overall = clean_dataframe(
        overall,
        drop_cols=["Rk", "Attendance", "Top Team Scorer", "Goalkeeper", "Notes"],
        rename_cols={"Squad": "Squad", "xG": "xG", "xGA": "xGA"},
        fill_na={"xG": 0, "xGA": 0},
    )
    display_df_info(overall, "Overall Stats")

# Goalkeeping stats
goalkeeping_standard = load_csv_file("goalkeeping_standard.csv")
if goalkeeping_standard is not None:
    goalkeeping_standard = clean_dataframe(
        goalkeeping_standard,
        drop_cols=["Rk", "MP", "Starts", "Min", "90s", "W", "D", "L", "CS", "CS%"],
        fill_na={"Save%": 0},
    )
    display_df_info(goalkeeping_standard, "Goalkeeping Standard Stats")

goalkeeping_adv = load_csv_file("goalkeeping_adv.csv")
if goalkeeping_adv is not None:
    goalkeeping_adv = clean_dataframe(
        goalkeeping_adv,
        drop_cols=[
            "Rk",
            "MP",
            "Min",
            "90s",
            "PKatt",
            "PKA",
            "PKsv",
            "PKm",
            "Save%",
            "CS",
            "CS%",
        ],
    )
    display_df_info(goalkeeping_adv, "Goalkeeping Advanced Stats")

# Merge goalkeeping datasets if both are available
if goalkeeping_standard is not None and goalkeeping_adv is not None:
    goalkeeping = pd.merge(
        goalkeeping_standard, goalkeeping_adv, on="Squad", suffixes=("", "_adv")
    )
    display_df_info(goalkeeping, "Merged Goalkeeping Stats")
else:
    goalkeeping = None

# Defensive stats
squad_defensive = load_csv_file("squad_defensive.csv")
if squad_defensive is not None:
    squad_defensive = clean_dataframe(
        squad_defensive,
        drop_cols=[
            "Rk",
            "MP",
            "Min",
            "90s",
            "Tkl",
            "TklW",
            "Def 3rd",
            "Mid 3rd",
            "Att 3rd",
            "Tkl.1",
            "Att",
            "Tkl%",
            "Lost",
            "Blocks",
            "Sh",
            "Pass",
            "Int",
            "Tkl+Int",
            "Clr",
            "Err",
        ],
    )
    display_df_info(squad_defensive, "Squad Defensive Stats")

# Merge defensive stats with overall if both are available
if squad_defensive is not None and overall is not None:
    defenses = pd.merge(
        squad_defensive, overall[["Squad", "Poss", "xGA", "GA"]], on="Squad"
    )
    defenses["DefAct"] = defenses["Tkl+Int"] + defenses["Clr"]
    display_df_info(defenses, "Merged Defensive Stats")
else:
    defenses = None

# Squad creation stats
squad_creation = load_csv_file("squad_creation.csv")
if squad_creation is not None:
    squad_creation = clean_dataframe(
        squad_creation,
        drop_cols=[
            "Rk",
            "MP",
            "Min",
            "90s",
            "SCA90",
            "PassLive",
            "PassDead",
            "Drib",
            "Sh",
            "Fld",
            "Def",
            "GCA90",
            "PassLive.1",
            "PassDead.1",
            "Drib.1",
            "Sh.1",
            "Fld.1",
            "Def.1",
        ],
    )
    display_df_info(squad_creation, "Squad Creation Stats")

# Squad shooting stats
squad_shooting = load_csv_file("squad_shooting.csv")
if squad_shooting is not None:
    squad_shooting = clean_dataframe(
        squad_shooting,
        drop_cols=[
            "Rk",
            "MP",
            "Min",
            "90s",
            "SoT%",
            "Dist",
            "FK",
            "PK",
            "PKatt",
            "G-xG",
            "np:G-xG",
        ],
    )
    display_df_info(squad_shooting, "Squad Shooting Stats")

# Merge creation stats with overall if both are available
if squad_creation is not None and overall is not None:
    chance_creation = pd.merge(
        squad_creation,
        overall[["Squad", "Prog", "SCA", "GCA", "npxG", "xA"]],
        on="Squad",
    )
    display_df_info(chance_creation, "Merged Chance Creation Stats")
else:
    chance_creation = None

# Analysis and Visualization
print("\nPerforming analysis and creating visualizations...")

# Only create visualizations if we have the required data
if overall is not None:
    # 1. Goals Scored vs Goals Conceded
    plot_scatter(
        overall,
        "GF",
        "GA",
        "Goals Scored vs Goals Conceded",
        "Goals Scored",
        "Goals Conceded",
        "Squad",
    )

    # 2. Expected Goals Analysis
    plot_scatter(
        overall,
        "xG",
        "xGA",
        "Expected Goals (xG) vs Expected Goals Against (xGA)",
        "Expected Goals (xG)",
        "Expected Goals Against (xGA)",
        "Squad",
    )

    # 3. Goals vs Expected Goals
    plot_scatter(
        overall,
        "GF",
        "xG",
        "Goals Scored vs Expected Goals",
        "Goals Scored",
        "Expected Goals (xG)",
        "Squad",
    )

    # 4. Goals Against vs Expected Goals Against
    plot_scatter(
        overall,
        "GA",
        "xGA",
        "Goals Against vs Expected Goals Against",
        "Goals Against",
        "Expected Goals Against (xGA)",
        "Squad",
    )

if defenses is not None:
    # 5. Defensive Actions Analysis
    plot_scatter(
        defenses,
        "DefAct",
        "GA",
        "Defensive Actions vs Goals Conceded",
        "Defensive Actions",
        "Goals Conceded",
        "Squad",
    )

    # Defensive correlation analysis
    plot_correlation_heatmap(
        defenses,
        ["DefAct", "xGA", "Poss", "GA"],
        "Correlation Matrix of Defensive Metrics",
    )

if goalkeeping is not None:
    # 6. Goalkeeping Performance
    plot_scatter(
        goalkeeping,
        "PSxG",
        "GA",
        "Post-Shot Expected Goals vs Goals Against",
        "Post-Shot Expected Goals",
        "Goals Against",
        "Squad",
    )

    # Goalkeeping correlation analysis
    plot_correlation_heatmap(
        goalkeeping, ["/90", "Stp%", "GA"], "Correlation Matrix of Goalkeeping Metrics"
    )

# Calculate and plot efficiency metrics if we have the required data
if chance_creation is not None:
    chance_creation = calculate_efficiency_metrics(
        chance_creation, "Prog", "SCA", "SCA_per_Prog"
    )
    chance_creation = calculate_efficiency_metrics(
        chance_creation, "Prog", "GCA", "GCA_per_Prog"
    )
    chance_creation = calculate_efficiency_metrics(
        chance_creation, "SCA", "GCA", "GCA_per_SCA"
    )

    plot_scatter(
        chance_creation,
        "SCA_per_Prog",
        "GCA_per_Prog",
        "Chance Creation Efficiency",
        "SCA per Progressive Action",
        "GCA per Progressive Action",
        hue="Squad",
        figsize=(12, 8),
    )

    plot_correlation_heatmap(
        chance_creation,
        columns=["SCA_per_Prog", "GCA_per_Prog", "GCA_per_SCA"],
        title="Correlation Matrix of Chance Creation Efficiency Metrics",
    )

if squad_shooting is not None:
    # Calculate efficiency metrics
    squad_shooting = calculate_efficiency_metrics(squad_shooting, "Sh", "Gls", "G/Sh")
    squad_shooting = calculate_efficiency_metrics(squad_shooting, "SoT", "Gls", "G/SoT")
    squad_shooting = calculate_efficiency_metrics(
        squad_shooting, "Sh", "npxG", "npxG/Sh"
    )

    # Plot shooting efficiency
    plot_scatter(
        squad_shooting,
        "G/Sh",
        "npxG/Sh",
        "Shooting Efficiency",
        "Goals per Shot",
        "Non-Penalty Expected Goals per Shot",
        hue="Squad",
        figsize=(12, 8),
    )

    # Plot correlation heatmap
    plot_correlation_heatmap(
        squad_shooting,
        columns=["G/Sh", "G/SoT", "npxG/Sh", "Sh/90", "SoT/90"],
        title="Correlation Matrix of Shooting Efficiency Metrics",
    )

if defenses is not None:
    defenses = calculate_efficiency_metrics(
        defenses, "Poss", "DefAct", "DefAct_per_Poss"
    )
    defenses = calculate_efficiency_metrics(defenses, "DefAct", "GA", "GA_per_DefAct")

    plot_scatter(
        defenses,
        "DefAct_per_Poss",
        "GA_per_DefAct",
        "Defensive Efficiency",
        "Defensive Actions per Possession",
        "Goals Against per Defensive Action",
        hue="Squad",
        figsize=(12, 8),
    )

    plot_correlation_heatmap(
        defenses,
        columns=["DefAct_per_Poss", "GA_per_DefAct", "xGA", "GA"],
        title="Correlation Matrix of Defensive Efficiency Metrics",
    )

if goalkeeping is not None:
    goalkeeping = calculate_efficiency_metrics(goalkeeping, "PSxG", "GA", "GA_per_PSxG")

    plot_scatter(
        goalkeeping,
        "GA_per_PSxG",
        "Stp%",
        "Goalkeeping Efficiency",
        "Goals Against per Post-Shot Expected Goals",
        "Save Percentage",
        hue="Squad",
        figsize=(12, 8),
    )

    plot_correlation_heatmap(
        goalkeeping,
        columns=["GA_per_PSxG", "Stp%", "GA", "PSxG"],
        title="Correlation Matrix of Goalkeeping Efficiency Metrics",
    )

print("Analysis complete!")
