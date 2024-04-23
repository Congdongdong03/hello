def next_number(number):
    if number % 2 == 0:
        return 3 * number + 1
    else:
        return 2 * number + 2
def main():
    input_num = int(input('Enter the initial number: '))
    print('Sequence:')
    step = 0
    while input_num <= 100:
        print(f"step:{step},{input_num}")
        input_num = next_number(input_num)
        step += 1
    print(f"Step {step}: {input_num}")
main()
