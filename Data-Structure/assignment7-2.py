# Prompt the user for a file name
filename = input("Enter the file name: ")

try:
    # Open the file
    with open(filename, 'r') as file:
        count = 0
        total_confidence = 0

        # Iterate through each line in the file
        for line in file:
            if line.startswith('X-DSPAM-Confidence:'):
                # Extract the floating point value from the line
                confidence_value = float(line.split(':')[1].strip())

                # Update count and total_confidence
                count += 1
                total_confidence += confidence_value

        if count > 0:
            # Calculate the average
            average_confidence = total_confidence / count

            # Print the result
            print(f"Average spam confidence: {average_confidence}")
        else:
            print("No X-DSPAM-Confidence lines found in the file.")

except FileNotFoundError:
    print(f"File '{filename}' not found. Please enter a valid file name.")
except Exception as e:
    print(f"An error occurred: {e}")
