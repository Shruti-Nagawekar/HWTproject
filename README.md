# MaxCard

MaxCard is a smart credit card recommendation tool designed to help users maximize rewards on every purchase. By analyzing Merchant Category Codes (MCC) and matching them with the best credit card in your wallet, MaxCard ensures you get the highest rewards, whether it's cashback, points, or other perks.

## Features

- **Credit Card Reward Optimization**: Automatically recommends the best card for a given MCC code.
- **Geo-Location Integration**: Detects the user's location and inputs the MCC code of the store automatically, updating Apple Wallet with the best card to use.
- **Chrome Extension**: Fetches the MCC code when visiting certain websites and picks the best card at checkout.
- **Real-Time Data**: Utilizes Stripe Issuing API to get real-time transaction information.
- **Multiple Card Support**: Supports multiple credit cards and tracks their reward rates.

## Inspiration

The inspiration for MaxCard came from the need to maximize credit card rewards efficiently. With so many cards offering different benefits across various spending categories, it can be challenging to decide which card to use. MaxCard was designed to simplify this process and make sure users get the most value out of their purchases.

## What it does

MaxCard allows users to input an MCC (Merchant Category Code) and instantly see which of their selected credit cards offers the highest reward, whether it’s points or cashback. It also automates this process with geo-location and a Chrome extension, ensuring the user gets the best card every time, without having to think about it.

## How we built it

MaxCard was built using:
- **Languages**: Python
- **Frameworks**: Tkinter (GUI)
- **Data Processing**: Pandas
- **APIs**: Stripe Issuing API
- **Storage**: Excel for initial reward data storage

## Challenges we ran into

One of the main challenges was ensuring that the rewards data was properly parsed and normalized across various formats (cashback percentages, points multipliers, etc.). Another challenge was handling user input errors, such as invalid MCC codes, and integrating geo-location and Chrome extensions seamlessly.

## Accomplishments that we're proud of

We are proud of building a functional tool that helps users make better financial decisions by maximizing rewards. We’re also proud of the seamless integration of different technologies, including Excel, Pandas, Tkinter, and the Stripe Issuing API.

## What we learned

We learned a lot about data processing, API integration, and user interface design. We also deepened our understanding of how credit card rewards work and the importance of automating reward maximization for ease of use.

## What's next for MaxCard

- Expanding the database to support more cards.
- Adding more real-time features using the Stripe Issuing API.
- Improving the recommendation engine with detailed analytics on user spending patterns.
- Geo-location support to detect stores and automatically update the best card in Apple Wallet.
- A Chrome extension to fetch the MCC code when browsing websites and recommend the best card at checkout.

## Getting Started

### Prerequisites

To run the MaxCard project, you’ll need:
- Python 3.x
- Tkinter (for GUI)
- Pandas (for data processing)
- Stripe Issuing API (optional for real-time features)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MaxCard.git

### Installation

1. Install required dependencies:
   ```bash
   pip install pandas
