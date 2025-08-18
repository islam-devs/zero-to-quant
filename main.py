#!/usr/bin/env python3
"""
Zero to Quant - Main Python File
A quantitative finance project for learning and experimentation.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def welcome_message():
    """Display welcome message for the Zero to Quant project."""
    print("🚀 Welcome to Zero to Quant!")
    print("📈 Your journey into quantitative finance starts here!")
    print(f"📅 Started on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

def sample_data_analysis():
    """Create and analyze sample financial data."""
    # Generate sample stock price data
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    np.random.seed(42)  # For reproducible results
    
    # Simulate stock price movement (geometric Brownian motion)
    returns = np.random.normal(0.0005, 0.02, len(dates))  # Daily returns
    prices = 100 * np.exp(np.cumsum(returns))  # Starting price of $100
    
    # Create DataFrame
    stock_data = pd.DataFrame({
        'Date': dates,
        'Price': prices,
        'Returns': returns
    })
    
    print("📊 Sample Stock Data Analysis:")
    print(f"📈 Starting Price: ${stock_data['Price'].iloc[0]:.2f}")
    print(f"📈 Ending Price: ${stock_data['Price'].iloc[-1]:.2f}")
    print(f"📊 Total Return: {((stock_data['Price'].iloc[-1] / stock_data['Price'].iloc[0]) - 1) * 100:.2f}%")
    print(f"📊 Average Daily Return: {stock_data['Returns'].mean() * 100:.4f}%")
    print(f"⚡ Volatility (std): {stock_data['Returns'].std() * 100:.4f}%")
    
    return stock_data

def main():
    """Main function to run the zero-to-quant analysis."""
    welcome_message()
    
    # Run sample analysis
    data = sample_data_analysis()
    
    print("\n🎯 Next steps:")
    print("1. Add real market data APIs (Yahoo Finance, Alpha Vantage)")
    print("2. Implement trading strategies")
    print("3. Add risk management functions")
    print("4. Create backtesting framework")
    
    return data

if __name__ == "__main__":
    # This will run when the script is executed
    sample_data = main()
    print("\n✅ Zero to Quant initialized successfully!")
