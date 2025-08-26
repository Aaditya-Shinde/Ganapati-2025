#!/usr/bin/env python3
"""
Pattern Generator Script

This script generates LED patterns based on user input of LED numbers.
It loads the all_off list, processes LED numbers to set corresponding bits,
and saves the pattern to a timestamped file.
"""

import csv
import copy
from datetime import datetime
import os

# Import the all_off list from constants
from consants import all_off


def load_led_mapping(csv_file):
    """
    Load LED mapping from CSV file.
    Returns a dictionary mapping led_number to (group, board, bit).
    """
    led_mapping = {}
    
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) == 4:
                    led_number = int(row[0])
                    group = int(row[1])
                    board = int(row[2])
                    bit = int(row[3])
                    led_mapping[led_number] = (group, board, bit)
    except FileNotFoundError:
        print(f"Error: LED mapping file '{csv_file}' not found.")
        return None
    except Exception as e:
        print(f"Error loading LED mapping: {e}")
        return None
    
    return led_mapping


def get_user_input():
    """
    Get LED numbers from user as space-separated input.
    Returns a list of LED numbers.
    """
    while True:
        try:
            user_input = input("\nEnter LED numbers (space-separated): ").strip()
            if not user_input:
                print("Please enter at least one LED number.")
                continue
            
            led_numbers = [int(x.strip()) for x in user_input.split()]
            
            # Validate LED numbers are positive
            if any(led <= 0 for led in led_numbers):
                print("Error: All LED numbers must be positive.")
                continue
                
            return led_numbers
            
        except ValueError:
            print("Error: Please enter valid numbers separated by spaces.")
        except KeyboardInterrupt:
            print("\nExiting...")
            return None


def set_led_bit(pattern, group, board, bit):
    """
    Set a specific bit in the pattern.
    Note: Board and bit indexing is from right to left (0-based).
    """
    # Convert board index (right-to-left) to list index (left-to-right)
    board_list_index = 9 - board
    
    # Set the bit (bit 0 is rightmost, bit 7 is leftmost)
    pattern[group][board_list_index] |= (1 << bit)


def process_led_numbers(led_numbers, led_mapping):
    """
    Process LED numbers and create a pattern.
    Returns the modified pattern and a list of invalid LED numbers.
    """
    # Create a deep copy of all_off to avoid modifying the original
    pattern = copy.deepcopy(all_off)
    invalid_leds = []
    
    print(f"\nProcessing {len(led_numbers)} LED(s)...")
    
    for led_num in led_numbers:
        if led_num in led_mapping:
            group, board, bit = led_mapping[led_num]
            print(f"LED {led_num}: Group {group}, Board {board}, Bit {bit}")
            
            # Validate indices
            if 0 <= group < len(pattern) and 0 <= board <= 9 and 0 <= bit <= 7:
                set_led_bit(pattern, group, board, bit)
                print(f"  ✓ Set bit {bit} on board {board} in group {group}")
            else:
                print(f"  ✗ Invalid mapping for LED {led_num}")
                invalid_leds.append(led_num)
        else:
            print(f"LED {led_num}: Not found in mapping")
            invalid_leds.append(led_num)
    
    return pattern, invalid_leds


def save_pattern(pattern, led_numbers):
    """
    Save the pattern to a timestamped file.
    """
    # Generate timestamp
    now = datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M%S")
    
    filename = f"pattern_{date_str}_{time_str}.py"
    
    try:
        with open(filename, 'w') as file:
            file.write("# LED Pattern generated on " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            file.write(f"# LED numbers used: {', '.join(map(str, led_numbers))}\n\n")
            file.write("pattern = [\n")
            
            for i, group in enumerate(pattern):
                file.write("    [")
                for j, board in enumerate(group):
                    if j > 0:
                        file.write(", ")
                    file.write(f"0b{board:08b}")
                file.write("]")
                if i < len(pattern) - 1:
                    file.write(",")
                file.write("\n")
            
            file.write("]\n")
        
        print(f"\n✓ Pattern saved to: {filename}")
        return filename
        
    except Exception as e:
        print(f"\n✗ Error saving pattern: {e}")
        return None


def display_pattern_summary(pattern, led_numbers):
    """
    Display a summary of the generated pattern.
    """
    print(f"\n{'='*50}")
    print("PATTERN SUMMARY")
    print(f"{'='*50}")
    print(f"LEDs processed: {len(led_numbers)}")
    print(f"LED numbers: {', '.join(map(str, led_numbers))}")
    
    # Count total bits set
    total_bits = 0
    for group in pattern:
        for board in group:
            total_bits += bin(board).count('1')
    
    print(f"Total bits set: {total_bits}")
    
    # Show non-zero boards
    print("\nNon-zero boards:")
    for group_idx, group in enumerate(pattern):
        for board_idx, board in enumerate(group):
            if board != 0:
                actual_board = 9 - board_idx  # Convert back to right-to-left indexing
                print(f"  Group {group_idx}, Board {actual_board}: 0b{board:08b} ({board})")


def main():
    """
    Main function to run the pattern generator.
    """
    print("LED Pattern Generator")
    print("=" * 30)
    
    # Load LED mapping
    csv_file = "/home/pi/Desktop/New/Ganapati/FINAL/led_mapping.csv"
    print(f"Loading LED mapping from {csv_file}...")
    
    led_mapping = load_led_mapping(csv_file)
    if led_mapping is None:
        return
    
    print(f"✓ Loaded mapping for {len(led_mapping)} LEDs")
    
    # Get user input
    led_numbers = get_user_input()
    if led_numbers is None:
        return
    
    # Process LED numbers
    pattern, invalid_leds = process_led_numbers(led_numbers, led_mapping)
    
    # Report invalid LEDs
    if invalid_leds:
        print(f"\n⚠ Warning: {len(invalid_leds)} invalid LED number(s): {', '.join(map(str, invalid_leds))}")
    
    # Display pattern summary
    display_pattern_summary(pattern, [led for led in led_numbers if led not in invalid_leds])
    
    # Save pattern
    filename = save_pattern(pattern, led_numbers)
    
    if filename:
        print(f"\n✓ Process completed successfully!")
        print(f"✓ Pattern file: {filename}")
    else:
        print(f"\n✗ Failed to save pattern file.")


if __name__ == "__main__":
    main()

"""

"""