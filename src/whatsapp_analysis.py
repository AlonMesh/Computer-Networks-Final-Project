"""
whatsapp_analysis.py: Script for analyzing WhatsApp messages and generating plots.
"""

import matplotlib.pyplot as plt
import csv
from datetime import datetime, timedelta
from scipy.stats import gaussian_kde
import numpy as np


def calculate_and_add_timestamps(csv_file_path):
    """
    Calculate timestamps from CSV file and return a list of timestamps.

    Args:
        csv_file_path (str): Path to the CSV file containing packet information.

    Returns:
        list: List of calculated timestamps.
    """
    timestamps = []

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            timestamps.append(datetime.fromtimestamp(float(row['Time'])))

    print("Timestamps calculated and saved")
    return timestamps


def plot_inter_message_delays(timestamps, group: str):
    """
    Plot inter-message delays using vertical lines.

    Args:
        timestamps (list): List of timestamps.
        group (str): Type of WhatsApp group (Message, Photo, Audio, Video).
    """
    inter_delays = []

    for i in range(1, len(timestamps)):
        delay = timestamps[i] - timestamps[i - 1]
        inter_delays.append(delay.total_seconds())

    plt.figure(figsize=(12, 6))

    # Use vlines to plot vertical lines
    plt.vlines(range(len(inter_delays)), ymin=0, ymax=inter_delays, lw=2, color='darkslateblue', alpha=0.7)

    plt.xlabel(f'{group} Index', size=12)
    plt.ylabel(f'Inter-{group} Delay (seconds)', size=12)
    plt.title(f'Inter-{group} Delays', size=20)

    plt.ylim(0, max(inter_delays) * 1.1)
    y_ticks = range(0, int(max(inter_delays)) + 2, 1)
    plt.yticks(y_ticks)
    plt.xlim(0, len(inter_delays))

    plt.grid(linewidth=0.5, linestyle='--')

    plt.savefig(f"res/{group}_delays.png")
    plt.show()


def plot_inter_message_delays_pdf(csv_file_path, group: str):
    """
    Plot probability density function of inter-message delays.

    Args:
        csv_file_path (str): Path to the CSV file containing packet information.
        group (str): Type of WhatsApp group (Message, Photo, Audio, Video).
    """
    timestamps = []

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            timestamps.append(datetime.fromtimestamp(float(row['Time'])))

        inter_delays = [(timestamps[i] - timestamps[i - 1]).total_seconds() for i in range(1, len(timestamps))]

    # Calculate kernel density estimation (KDE) for the inter-message delays
    kde = gaussian_kde(inter_delays)

    # Generate x values for the KDE plot
    x_vals = np.linspace(min(inter_delays), max(inter_delays), num=1000)

    plt.figure(figsize=(12, 6))

    plt.plot(x_vals, kde(x_vals), color='darkslateblue')
    plt.xlabel(f'Inter-{group} Delay (seconds)', size=12)
    plt.ylabel(f'Probability Density', size=12)
    plt.title(f'Probability Density Function of Inter-{group} Delays', size=20)

    plt.ylim(0, 1.02)

    plt.grid(linewidth=0.5, linestyle='--')

    plt.savefig(f"res/{group}_delays_pdf.png")
    plt.show()


# def plot_message_sizes(csv_file_path, group: str):
#     """
#     Plot message sizes over time.
#
#     Args:
#         csv_file_path (str): Path to the CSV file containing packet information.
#         group (str): Type of WhatsApp group (Message, Photo, Audio, Video).
#     """
#     message_sizes = []
#     message_time = []
#
#     with open(csv_file_path, 'r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#
#         for row in csv_reader:
#             message_sizes.append(int(row['Length']))
#             message_time.append(float(row['Time']))
#
#     plt.figure(figsize=(12, 6))
#
#     # Plot rounded lines with gray color
#     plt.vlines(message_time, ymin=0, ymax=message_sizes, lw=2, color='darkslateblue', alpha=0.7)
#
#     # Add black circles at the end of each line
#     #     plt.plot(message_time, message_sizes, 'o', color="g", markersize=5, alpha=0.3)
#
#     plt.xlabel('Time', size=12)
#     plt.ylabel(f'{group} Length', size=12)
#     plt.title(f'{group} Length by Time', size=20)
#
#     # Set y-axis limits and ticks
#     plt.ylim(0, max(message_sizes) + 500)
#     y_ticks = range(0, max(message_sizes) + 500, 1000)
#     plt.yticks(y_ticks)
#     plt.xlim(min(message_time) - 2, max(message_time) + 2)
#
#     plt.grid(linewidth=0.7, linestyle='--', color='lightgray')
#
#     plt.savefig(f"res/{group}_sizes.png")
#     plt.show()

def plot_message_sizes(csv_file_path, group: str):
    """
    Plot message sizes over time.

    Args:
        csv_file_path (str): Path to the CSV file containing packet information.
        group (str): Type of WhatsApp group (Message, Photo, Audio, Video).
    """
    message_sizes = []
    message_time = []

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            message_sizes.append(int(row['Length']))
            message_time.append(float(row['Time']))

    plt.figure(figsize=(12, 6))

    # Plot rounded lines with gray color
    plt.vlines(message_time, ymin=0, ymax=message_sizes, lw=2, color='darkslateblue', alpha=0.7)

    # Add black circles at the end of each line
    #     plt.plot(message_time, message_sizes, 'o', color="g", markersize=5, alpha=0.3)

    plt.xlabel('Time', size=12)
    plt.ylabel(f'{group} Length', size=12)
    plt.title(f'{group} Length by Time', size=20)

    # Set y-axis limits and ticks
    plt.ylim(0, max(message_sizes) + 500)
    y_ticks = range(0, max(message_sizes) + 500, 1000)
    plt.yticks(y_ticks)
    plt.xlim(min(message_time) - 2, max(message_time) + 2)

    plt.grid(linewidth=0.7, linestyle='--', color='lightgray')

    plt.savefig(f"res/{group}_sizes.png")
    plt.show()


def creating_plots(csv_file_path, group: str):
    """
    Generate and save plots for WhatsApp message analysis.

    Args:
        csv_file_path (str): Path to the CSV file containing packet information.
        group (str): Type of WhatsApp group (Message, Photo, Audio, Video).
    """
    plot_inter_message_delays(calculate_and_add_timestamps(csv_file_path), group)
    plot_inter_message_delays_pdf(csv_file_path, group)
    plot_message_sizes(csv_file_path, group)
