import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd

# Path to the Excel file
synthetic_rewards_path = r'C:\Users\shruti\OneDrive - Texas Tech University\Desktop\HWTProject\maxcard\synthetic_mcc_rewards.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(synthetic_rewards_path)

# Function to convert reward strings into numerical values
def reward_to_value(reward):
    if 'points' in reward:
        return int(reward.split('x')[0])  # Extract the multiplier (e.g., "3x points" -> 3)
    elif 'cashback' in reward:
        return float(reward.split('%')[0]) / 100  # Convert percentage to decimal (e.g., "1% cashback" -> 0.01)
    else:
        return 0  # Default value if no recognizable reward type

# Apply the reward conversion to all card columns (skip 'MCC Code' column)
for col in df.columns[1:]:
    df[col] = df[col].apply(reward_to_value)

# Function to handle card selections
def card_selected():
    selected_cards = [cards_listbox.get(i) for i in cards_listbox.curselection()]
    
    if not selected_cards:
        messagebox.showwarning("No Selection", "Please select at least one card.")
        return
    
    # Ask for MCC code
    mcc_code = simpledialog.askinteger("MCC Code", "Please enter the MCC Code:")
    
    if mcc_code is not None:
        if mcc_code in df['MCC Code'].values:
            # Find the card with the best reward for the input MCC code
            rewards = {card: df.loc[df['MCC Code'] == mcc_code, card].values[0] for card in selected_cards}
            best_card = max(rewards, key=rewards.get)
            best_reward = rewards[best_card]
            
            # Display the best card and its reward
            messagebox.showinfo("Best Card", f"The best card for MCC {mcc_code} is: {best_card} with a reward of {best_reward}")
        else:
            messagebox.showwarning("No Data", f"No rewards data available for MCC {mcc_code}")
    
    root.destroy()  # Close the window after selection

# Create the main window
root = tk.Tk()
root.title("Select Your Credit Card")

# List of credit cards
credit_cards = [
    "Chase Freedom Unlimited", 
    "Chase Freedom Unlimited", 
    "Capital One Venture Rewards Credit Card",
    "Blue Cash Preferred Card from American Express",
    "Capital One SavorOne Cash Rewards Credit Cardac",
    "Chase Sapphire Preferred Card",
    "Wells Fargo Reflect Card",
    "Discover it Cash Back",
    "Wells Fargo Active Cash"
]

# Create a label
label = tk.Label(root, text="Please select one or more credit cards:", font=("Arial", 14))
label.pack(pady=10)

# Create a Listbox for multiple card selections
cards_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=10)
for card in credit_cards:
    cards_listbox.insert(tk.END, card)
cards_listbox.pack(pady=10)

# Create a button to submit the selection
submit_button = tk.Button(root, text="Submit", width=20, command=card_selected)
submit_button.pack(pady=10)

# Run the main event loop
root.mainloop()