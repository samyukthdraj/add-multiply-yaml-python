import yaml

# Load YAML configuration
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

# Get user inputs
try:
    input1 = float(input("Enter the first number: "))
    input2 = float(input("Enter the second number: "))
    input3 = float(input("Enter the third number: "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

# Stage 1
if config["stage1_operation"] == "add":
    stage1_result = input1 + input2
elif config["stage1_operation"] == "subtract":  # Example of extending the config
    stage1_result = input1 - input2
else:
    print("Invalid stage1_operation in config.yml")
    exit()

# Stage 2
if config["stage2_operation"] == "multiply":
    final_result = stage1_result * input3
elif config["stage2_operation"] == "divide":  # Example of extending the config
    if input3 == 0:
        print("Division by zero error.")
        exit()
    final_result = stage1_result / input3
else:
    print("Invalid stage2_operation in config.yml")
    exit()


print("The final result is:", final_result)