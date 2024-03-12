#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
import copy

from functions import *



def menu():
    print("Possible commands:")
    print("1. list (display all scores)")
    print("2. list sorted(display all scores sorted by average)")
    print("3. list [ < | = | > ] <score>")
    print("4. add <P1 score> <P2 score> <P3 score>")
    print("5. insert <P1 score> <P2 score> <P3 score> at <position>")
    print("6. remove <position>")
    print("7. remove <start position> to <end position>")
    print("8. replace <participant's_index> <P1 | P2 | P3> with <new score>")
    print("8. top <number>")
    print("9. top <number> <P1 | P2 | P3> (shows top at certain problem)")
    print("10. remove [ < | = | > ] <score> (removes all scores with a certain property)")
    print("11. undo (undo the last operation)")
    print("11. exit")
    print("\n")


def main():
    undo_stack = []
    scores_dictionary = get_ten_rand_scores()
    command_splitted_list = []
    commands_list = ["list", "add", "insert", "remove", "replace", "list", "top", "undo", "exit"]
    #undo_list = []
    while True:

        first_commands_list_element = 0
        second_commands_list_element = 1
        third_commands_list_element = 2
        fourth_commands_list_element = 3
        fifth_commands_list_element = 4
        sixth_command_list_element = 5



        calculate_average(scores_dictionary)

        users_choice = input("Enter your command: ")
        strip_users_choice = users_choice.strip()
        command_splitted_list = command_splitter(strip_users_choice)

        #undo_list.append([scores_dictionary.copy() for score in scores_dictionary])
        if command_splitted_list[first_commands_list_element] not in commands_list:
            print("Invalid input, pls try again!")


        try:
            lenght_of_list_for_list_command = 1

            if len(command_splitted_list) == lenght_of_list_for_list_command and command_splitted_list[first_commands_list_element] == "list":
                if command_splitted_list[first_commands_list_element] == "list":
                    sort_scores_list_by_index(scores_dictionary)
                    display_all_scores(scores_dictionary)
                else:
                    raise ValueError("Invalid input, pls try again!")
        except ValueError as ve:
            print(ve)
        try:
            lenght_of_list_for_add = 4

            if len(command_splitted_list) == lenght_of_list_for_add and command_splitted_list[first_commands_list_element] == "add":
                if command_splitted_list[second_commands_list_element].isdigit() and command_splitted_list[third_commands_list_element].isdigit() and command_splitted_list[fourth_commands_list_element].isdigit():
                    score1 = int(command_splitted_list[second_commands_list_element])
                    score2 = int(command_splitted_list[third_commands_list_element])
                    score3 = int(command_splitted_list[fourth_commands_list_element])
                    new_index = len(scores_dictionary) + 1
                    undo_stack.append(copy.deepcopy(scores_dictionary))

                    add_a_score(scores_dictionary, new_index, score1, score2, score3)
                else:
                    raise ValueError("Invalid input, pls try again!")
        except ValueError as ve:
            print(ve)

        try:
            lenght_of_list_for_insert_command = 6

            if len(command_splitted_list) == lenght_of_list_for_insert_command and command_splitted_list[first_commands_list_element] == "insert":
                if command_splitted_list[second_commands_list_element].isdigit() and command_splitted_list[third_commands_list_element].isdigit() and command_splitted_list[fourth_commands_list_element].isdigit() and command_splitted_list[sixth_command_list_element].isdigit() and command_splitted_list[fifth_commands_list_element] == "at":
                    if int(command_splitted_list[sixth_command_list_element]) <= len(scores_dictionary):
                        score1 = int(command_splitted_list[second_commands_list_element])
                        score2 = int(command_splitted_list[third_commands_list_element])
                        score3 = int(command_splitted_list[fourth_commands_list_element])
                        index_insert = int(command_splitted_list[sixth_command_list_element])
                        undo_stack.append(copy.deepcopy(scores_dictionary))
                        insert_score_at_index(scores_dictionary, score1, score2, score3, index_insert)

                    else:
                        raise ValueError("Invalid input, pls try again!")
                else:
                    raise ValueError("Invalid input, pls try again!")
        except ValueError as ve:
            print(ve)

        try:
            lenght_of_list_for_remove_command = 2

            if len(command_splitted_list) == lenght_of_list_for_remove_command and command_splitted_list[first_commands_list_element] == "remove":
                if int(command_splitted_list[second_commands_list_element]) <= len(scores_dictionary):
                    if command_splitted_list[second_commands_list_element].isdigit():
                        index_to_be_removed = int(command_splitted_list[second_commands_list_element])
                        undo_stack.append(copy.deepcopy(scores_dictionary))
                        remove_scores_at_position(scores_dictionary, index_to_be_removed)

                    else:
                        raise ValueError("Invalid input, pls try again!")
                else:
                    raise  ValueError("Index too big, pls try again!")
        except ValueError as ve:
            print(ve)

        try:
            lenght_of_list_for_remove_property_command = 4
            #beginning_of_the_array = 0

            if len(command_splitted_list) == lenght_of_list_for_remove_property_command and command_splitted_list[first_commands_list_element] == "remove":
                if command_splitted_list[second_commands_list_element].isdigit() and command_splitted_list[third_commands_list_element] == "to" and command_splitted_list[fourth_commands_list_element].isdigit():
                    start_index = int(command_splitted_list[second_commands_list_element])
                    end_index = int(command_splitted_list[fourth_commands_list_element])
                    if start_index >= 0 and start_index <= len(scores_dictionary)-1 and start_index < end_index and end_index >= 1 and end_index <= len(scores_dictionary):
                        undo_stack.append(copy.deepcopy(scores_dictionary))
                        remove_from_startposition_to_endposition(scores_dictionary, start_index, end_index)

                    else:
                        raise ValueError("Invalid indexes (start<end and must exist)")
                else:
                    raise ValueError("Invalid input, pls try again!")
        except ValueError as ve:
            print(ve)


        problem_list = ["P1", "P2", "P3"]
        try:
            lenght_of_list_for_replace_command = 5
            if len(command_splitted_list) == lenght_of_list_for_replace_command and command_splitted_list[first_commands_list_element] == "replace" and command_splitted_list[fourth_commands_list_element] == "with":
                if command_splitted_list[second_commands_list_element].isdigit() and command_splitted_list[fifth_commands_list_element].isdigit() and command_splitted_list[third_commands_list_element] in problem_list:
                    index_to_be_replaced = int(command_splitted_list[second_commands_list_element])
                    problem_score_to_be_replaced = command_splitted_list[third_commands_list_element]
                    new_score = int(command_splitted_list[fifth_commands_list_element])
                    undo_stack.append(copy.deepcopy(scores_dictionary))
                    replace_score_at_index(scores_dictionary, index_to_be_replaced, problem_score_to_be_replaced, new_score)

        except ValueError as ve:
            print(ve)
        #todo
        copy_dictionary = scores_dictionary
        try:
            lenght_of_list_for_list_sorted_command = 2

            if len(command_splitted_list) == lenght_of_list_for_list_sorted_command and command_splitted_list[first_commands_list_element] == "list":
                if command_splitted_list[second_commands_list_element] == "sorted":
                    #new_scores_dictionary = []
                    #display_all_scores_sorted_by_average(scores_dictionary, new_scores_dictionary)
                    display_all_scores_sorted_by_average2(copy_dictionary)

                else:
                    raise ValueError("Invalid input, pls try again!")
        except ValueError as ve:
            print(ve)

        symbol_list = ["<", "=", ">"]
        list_property = []
        try:
            lenght_of_list_for_list_sorted_of_certain_problem_command = 3

            if len(command_splitted_list) == lenght_of_list_for_list_sorted_of_certain_problem_command and command_splitted_list[first_commands_list_element] == "list":
                if command_splitted_list[second_commands_list_element] in symbol_list and command_splitted_list[third_commands_list_element].isdigit():
                    symbol = command_splitted_list[second_commands_list_element]
                    display_list_with_property(scores_dictionary, command_splitted_list)
                    #display_all_scores(list_property)
                else:
                    raise ValueError("Invalid input, pls try again!")
        except ValueError as ve:
            print(ve)

        try:
            lenght_of_list_for_top_command = 2
            if len(command_splitted_list) == lenght_of_list_for_top_command and command_splitted_list[first_commands_list_element] == "top":
                if command_splitted_list[second_commands_list_element].isdigit():
                    top_number = int(command_splitted_list[second_commands_list_element])
                    display_top(scores_dictionary, top_number)
                else:
                    raise ValueError("Invalid input, pls try again!")
        except ValueError as ve:
            print(ve)


        try:
            lenght_of_list_for_top_at_certain_problem_command = 3
            if len(command_splitted_list) == lenght_of_list_for_top_at_certain_problem_command and command_splitted_list[first_commands_list_element] == "top":
                if command_splitted_list[second_commands_list_element].isdigit() and command_splitted_list[third_commands_list_element] in problem_list:
                    top_number = int(command_splitted_list[second_commands_list_element])
                    problem = command_splitted_list[third_commands_list_element]
                    display_top_at_certain_problem(scores_dictionary, top_number, problem)
                else:
                    raise ValueError("Invalid input, pls try again!")
        except ValueError as ve:
            print(ve)

        #remove[ < | = | >] < score >
        try:
            lenght_of_list_for_remove_all_property_command = 3

            if len(command_splitted_list) == lenght_of_list_for_remove_all_property_command and command_splitted_list[first_commands_list_element] == "remove":
                if command_splitted_list[second_commands_list_element] in symbol_list and command_splitted_list[third_commands_list_element].isdigit():
                    symbol = command_splitted_list[second_commands_list_element]
                    score = command_splitted_list[third_commands_list_element]
                    undo_stack.append(copy.deepcopy(scores_dictionary))
                    remove_all_participants_with_property(scores_dictionary, command_splitted_list)

                else:
                    raise ValueError("Invalid input, pls try again!")
        except ValueError as ve:
            print(ve)


        # undo_list = []
        # #undo
        # try:
        #     if len(command_splitted_list) == 1 and command_splitted_list[0] == "undo":
        #         undo(scores_dictionary, undo_list)
        # except ValueError as ve:
        #     print(ve)
        if command_splitted_list[first_commands_list_element] == "undo":
            #undo2(scores_dictionary, undo_list, list_idk)
            #undo_list.append([scores_dictionary.copy() for score in scores_dictionary])
            # use deep copy for undo
            undo(scores_dictionary, undo_stack)





        if command_splitted_list[first_commands_list_element] == "exit":
            print("Goodbye")
            break
