import packet_capture
import pyshark
import csv
import whatsapp_analysis


def convert_pcap_to_csv(pcap_file_path, csv_file_path):
    """
    Convert a pcap file to a CSV file containing packet information.

    Args:
        pcap_file_path (str): Path to the input pcap file.
        csv_file_path (str): Path to the output CSV file.
    """
    # Open the pcapng file for reading
    capture = pyshark.FileCapture(pcap_file_path, display_filter='ip')  # Use display_filter if needed

    # Create a CSV file and write headers
    with open(csv_file_path, 'w', newline='') as csv_file:
        fieldnames = ['No.', 'Time', 'Source', 'Destination', 'Protocol', 'Length', 'Info']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        # Iterate through packets and write to CSV
        for packet in capture:
            packet_data = {
                'No.': packet.number,
                'Time': packet.sniff_time.strftime('%Y-%m-%d %H:%M:%S.%f'),
                'Source': packet.ip.src if 'ip' in packet else '',
                'Destination': packet.ip.dst if 'ip' in packet else '',
                'Protocol': packet.highest_layer,
                'Length': packet.length,
                'Info': packet.info if hasattr(packet, 'info') else ''
            }
            csv_writer.writerow(packet_data)

    print(f'PCAP file converted to CSV: {csv_file_path}')


def main():
    """
    Main function to execute the packet conversion and analysis process.
    """
    GROUPS = ['Message', 'Photo', 'Audio', 'Video']
    for group in GROUPS:
        pcap_file_path = f"../resources/{group}s_real_1.pcap"
        scv_file_path = f"../resources/{group}s_real_1_.csv"
        print(f"Converting {pcap_file_path} → {scv_file_path}...")
        convert_pcap_to_csv(pcap_file_path, csv_file_path)
        print("Done.")
        print(f"Starting plots for {scv_file_path}...")
        whatsapp_analysis.creating_plots(scv_file_path, group)
        print("Done.")

    pcap_file = "../resources"
    convert_pcap_to_csv(pcap_file, r'C:\Users\Alon\Downloads\tryTOconvert.pcap\output.csv')


if __name__ == "__main__":
    main()
