import pyshark
import csv
import os
import whatsapp_analysis  # The second file


def convert_pcap_to_csv(pcap_file_path, csv_file_path):
    """
    Convert a pcap file to a CSV file containing packet information.

    Args:
        pcap_file_path (str): Path to the input pcap file.
        csv_file_path (str): Path to the output CSV file.
    """
    # Open the pcapng file for reading
    capture = pyshark.FileCapture(pcap_file_path, display_filter='ip')  # Use display_filter if needed

    # Get the sniff time of the first packet
    first_sniff_time = None
    for packet in capture:
        first_sniff_time = packet.sniff_time
        break

    # Create a CSV file and write headers
    with open(csv_file_path, 'w', newline='') as csv_file:
        fieldnames = ['No.', 'Time', 'Source', 'Destination', 'Protocol', 'Length', 'Info']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        # Iterate through packets and write to CSV
        for packet in capture:
            # Calculate Time by seconds as the time of the current packet - time of the current packet
            delta = packet.sniff_time - first_sniff_time
            delta_seconds = delta.total_seconds()  # Convert timedelta to seconds

            packet_data = {
                'No.': packet.number,
                'Time': delta_seconds,
                'Source': packet.ip.src if 'ip' in packet else '',
                'Destination': packet.ip.dst if 'ip' in packet else '',
                'Protocol': packet.highest_layer,
                'Length': packet.length,
                'Info': packet.info if hasattr(packet, 'info') else ''
            }
            csv_writer.writerow(packet_data)

    print(f'PCAP file converted to CSV: {csv_file_path}')


def main():
    # Modify this list to specify different WhatsApp group types for analysis
    GROUPS = ['Message', 'Photo', 'Audio', 'Video']
    # GROUPS = ['YesFilter', 'NoFilter']
    for group in GROUPS:
        pcap_file_path = f"resources/{group}s_record.pcap"
        csv_file_path = f"resources/{group}s_record.csv"
        if not os.path.exists(pcap_file_path):
            raise FileNotFoundError(f"{pcap_file_path} does not exist.")
        try:
            print(f"Converting {pcap_file_path} → {csv_file_path} ...")
            convert_pcap_to_csv(pcap_file_path, csv_file_path)
            print("Conversion complete.")
        except Exception as e:
            print(f"Error occurred during conversion: {e}")
        try:
            print(f"Starting plots for {csv_file_path} ...")
            whatsapp_analysis.creating_plots(csv_file_path, group)
            print("Plots generated.")
        except Exception as e:
            print(f"Error occurred during plot generation: {e}")


if __name__ == "__main__":
    main()
