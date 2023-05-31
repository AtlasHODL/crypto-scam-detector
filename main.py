import tkinter as tk

def classify_crypto_scam():
    ticker = ticker_entry.get()
    if ticker.upper() == "$BTC":
        classification_label.config(text="Legitimate Bitcoin")
    else:
        classification_label.config(text="Shitcoin Scam")

# Create the main window
window = tk.Tk()
window.title("Crypto Scam Classifier")

# Create the input label and entry field
ticker_label = tk.Label(window, text="Enter the ticker symbol of a cryptocurrency:")
ticker_label.pack()
ticker_entry = tk.Entry(window)
ticker_entry.pack()

# Create the classify button
classify_button = tk.Button(window, text="Classify", command=classify_crypto_scam)
classify_button.pack()

# Create the classification label
classification_label = tk.Label(window, text="")
classification_label.pack()

# Start the GUI main loop
window.mainloop()
