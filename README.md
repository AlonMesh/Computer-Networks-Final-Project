## Project: WhatsApp Packet Analysis and Visualization

This project involves capturing network packets, extracting WhatsApp messages, generating various plots, and saving results.

### Introduction

Modern Instant Messaging (IM) applications, including WhatsApp, rely on encrypted communication to ensure data privacy and security. In this encryption context, an attacker with access to someone's network traffic might be able to analyze patterns and timings of message transmission within a group to make certain inferences. While the content and metadata of messages remain encrypted, the timings and frequencies of messages can provide insights into group interactions.

### Project Structure

- `src/`: Contains Python script files.
- `resources/`: Contains pcap files for analysis.
- `res/`: Stores generated plots.
- `main.py`: Main script for packet capture, CSV conversion, and plot generation.
- `whatsapp_analysis.py`: Script for analyzing WhatsApp messages and creating plots.

### How to Use

1. Ensure you have Python installed.
2. Install required packages using `pip install pyshark matplotlib`.
3. Place your pcap or pcapng files in the `resources/` folder.

#### Running

Run `main.py` to convert packet captures to CSV format and generate plots:

```python
python main.py
```
The script will convert pcap files in the resources/ folder to CSV format and save them in the same folder. Then, the script will analyze the CSV files and create plots for inter-message delays and message sizes. The plots will be saved in the res/ folder.

### Plots and Analysis
1. **Inter-Message Delay Plot:** This plot shows the time delay between consecutive messages in a specific WhatsApp group. It highlights the temporal patterns of message transmission within the group.

2. **Probability Density Function (PDF) Plot:** The PDF plot provides a visual representation of the probability distribution of inter-message delays. It helps to visualize the likelihood of different delays between messages in the group.

3. **Message Size Plot:** This plot depicts the sizes of messages over time. It enables the observation of variations in message lengths and potential trends within the communication.

Please see the `res/` folder for the generated plots corresponding to each analysis.

### Contributors
This project was done by Alon Meshulam and Israel Gitler as the final project of "Communication Networks" course.

### Acknowledgments
Special thanks to the creators of pyshark and matplotlib for their amazing libraries.

