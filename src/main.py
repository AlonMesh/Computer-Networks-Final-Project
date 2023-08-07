"""
main.py: Main script to capture packets, extract WhatsApp messages, generate plots, and save results to pickle.
"""

import packet_capture
import whatsapp_analysis


def main():
    interface = "YOUR_NETWORK_INTERFACE"  # Replace with your Wi-Fi network interface name
    capture_duration = 30  # seconds

    # Create a directory to store the pcap files
    pcap_dir = '../resources'  # Replace with the desired directory path
    os.makedirs(pcap_dir, exist_ok=True)

    # Capture packets for each WhatsApp group
    groups = ['messages', 'images', 'audio', 'video']
    pcap_files = {}
    for group in groups:
        pcap_file = os.path.join(pcap_dir, f"{group}_packets.pcap")
        print(f"Starting packet capture for {group} group...")
        packet_capture.start_packet_capture(interface, capture_duration, pcap_file)
        pcap_files[group] = pcap_file
        print(f"Packet capture for {group} group complete.")

    # Extract WhatsApp messages for each group
    messages = {}
    for group, pcap_file in pcap_files.items():
        print(f"Extracting WhatsApp messages for {group} group...")
        messages[group] = packet_capture.extract_whatsapp_messages(pcap_file)
        print(f"WhatsApp message extraction for {group} group complete.")

    # Create a directory to store the results
    results_dir = '../res'  # Replace with the desired directory path
    os.makedirs(results_dir, exist_ok=True)

    # Analyze and plot for each WhatsApp group
    for group in groups:
        # Filter messages for the current group
        group_messages = messages[group]

        # Plot and save inter-message delays
        whatsapp_analysis.plot_inter_message_delays(group_messages, group)
        inter_message_delays_file = os.path.join(results_dir, f"{group}_inter_message_delays.pickle")
        with open(inter_message_delays_file, 'wb') as f:
            pickle.dump(group_messages, f)

        # Plot and save message sizes
        whatsapp_analysis.plot_message_sizes(group_messages, group)
        message_sizes_file = os.path.join(results_dir, f"{group}_message_sizes.pickle")
        with open(message_sizes_file, 'wb') as f:
            pickle.dump(group_messages, f)

    print("Plots generated and results saved to pickle.")


if __name__ == "__main__":
    main()
