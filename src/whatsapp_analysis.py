"""
whatsapp_analysis.py: Module for analyzing WhatsApp message data and generating plots.
"""

import pickle
import matplotlib.pyplot as plt


def load_messages_from_pickle(pickle_file):
    """
    Load WhatsApp messages from a pickle file.
    Args:
        pickle_file (str): Path to the pickle file containing the WhatsApp messages.
    Returns:
        list: List of WhatsApp messages, each message represented as a dictionary.
    """
    with open(pickle_file, "rb") as f:
        messages = pickle.load(f)
    return messages


def filter_messages_by_group(messages, group):
    """
    Filter WhatsApp messages by group.
    Args:
        messages (list): List of WhatsApp messages, each message represented as a dictionary.
        group (str): The group to filter by (e.g., "messages", "images", "audio", "video").
    Returns:
        list: List of WhatsApp messages belonging to the specified group.
    """
    filtered_messages = [message for message in messages if message['group'] == group]
    return filtered_messages


def plot_inter_message_delays(messages, group):
    """
    Generate and display a plot of inter-message delays in a specific WhatsApp group.
    Args:
        messages (list): List of WhatsApp messages, each message represented as a dictionary.
        group (str): The group to plot inter-message delays for (e.g., "messages", "images", "audio", "video").
    Returns:
        None
    """
    # Implement the logic to calculate inter-message delays for the specified group
    # You can use the timestamps of consecutive messages in the group to compute the delays
    # Create a plot using matplotlib and display the inter-message delay distribution

    # Example (Replace with your implementation):
    group_messages = filter_messages_by_group(messages, group)
    inter_message_delays = [message['timestamp'] for message in group_messages]  # Replace with actual delays
    plt.hist(inter_message_delays, bins=20)
    plt.xlabel("Inter-Message Delay (seconds)")
    plt.ylabel("Frequency")
    plt.title(f"Inter-Message Delay Distribution for {group} group")
    plt.show()


def plot_message_sizes(messages, group):
    """
    Generate and display a plot of message sizes in a specific WhatsApp group.
    Args:
        messages (list): List of WhatsApp messages, each message represented as a dictionary.
        group (str): The group to plot message sizes for (e.g., "messages", "images", "audio", "video").
    Returns:
        None
    """
    # Implement the logic to extract message sizes for the specified group from the messages list
    # Create a plot using matplotlib and display the message size distribution

    # Example (Replace with your implementation):
    group_messages = filter_messages_by_group(messages, group)
    message_sizes = [len(message['content']) for message in group_messages]  # Replace with actual message sizes
    plt.hist(message_sizes, bins=20)
    plt.xlabel("Message Size (characters)")
    plt.ylabel("Frequency")
    plt.title(f"Message Size Distribution for {group} group")
    plt.show()
