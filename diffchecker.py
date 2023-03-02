import subprocess
import sys

args = sys.argv

problem_name = args[1]

script = f"{problem_name}/{problem_name}.py"

input_file_path = f"{problem_name}/input.txt"

with open(input_file_path, "r") as input_file:
    result = subprocess.run(["python", script], capture_output=True, stdin=input_file)

assert isinstance(result.stdout, bytes)
generated_out = result.stdout.decode()

output_file_path = f"{problem_name}/output.txt"

with open(output_file_path, "r", encoding="utf-8") as expected_out_file:
    expected_out = expected_out_file.read()

temp = ""
for c in generated_out:
    if c != "\r":
        temp += c
generated_out = temp

equal = expected_out == generated_out

print("Generated = Expected:", equal)

if not equal:
    gen_lines = generated_out.split("\n")
    expec_lines = expected_out.split("\n")
    longest = len(max(gen_lines, key=len))
    for i, c in enumerate(gen_lines):
        if gen_lines[i] != expec_lines[i]:
            print(
                f"{gen_lines[i] + ''.join(' ' for _ in range(longest - len(gen_lines[i])))} | {expec_lines[i]}"
            )
