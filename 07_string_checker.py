# checks that users enter a valid response (eg yes / no
# cas / credit) based on a list of options


def string_checker(question, num_letters, valid_responses):

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[0] or response == item:
                return item

            print("Please enter a valid response!")


# main routine

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]
