#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
import random
import copy

main_command = 0
symbol_element = 1
the_element_in_list_that_shows_average = 2


def get_ten_rand_scores():
    return [
        {"index": "01", "problem1": random.randint(1, 10), "problem2": random.randint(1, 10), "problem3": random.randint(1, 10), "average": 0 },
        {"index": "02", "problem1": random.randint(1, 10), "problem2": random.randint(1, 10), "problem3": random.randint(1, 10), "average": 0},
        {"index": "03", "problem1": random.randint(1, 10), "problem2": random.randint(1, 10), "problem3": random.randint(1, 10), "average": 0},
        {"index": "04", "problem1": random.randint(1, 10), "problem2": random.randint(1, 10), "problem3": random.randint(1, 10), "average": 0},
        {"index": "05", "problem1": random.randint(1, 10), "problem2": random.randint(1, 10), "problem3": random.randint(1, 10), "average": 0},
        {"index": "06", "problem1": random.randint(1, 10), "problem2": random.randint(1, 10), "problem3": random.randint(1, 10), "average": 0},
        {"index": "07", "problem1": random.randint(1, 10), "problem2": random.randint(1, 10), "problem3": random.randint(1, 10), "average": 0},
        {"index": "08", "problem1": random.randint(1, 10), "problem2": random.randint(1, 10), "problem3": random.randint(1, 10), "average": 0},
        {"index": "09", "problem1": random.randint(1, 10), "problem2": random.randint(1, 10), "problem3": random.randint(1, 10), "average": 0},
        {"index": "10", "problem1": random.randint(1, 10), "problem2": random.randint(1, 10), "problem3": random.randint(1, 10), "average": 0}
    ]


def add_a_score(scores_dictionary_list, new_index: int, score1: int, score2: int, score3: int):
    #new_index = len(scores_dictionary_list)+1
    #print(new_index) works
    scores_dictionary_list.append({"index": new_index, "problem1": score1, "problem2": score2, "problem3": score3})

def insert_score_at_index(scores_dictionary_list, score1: int, score2: int, score3: int, index_inserter: int):
    #scores_dictionary_list.insert(index_inserter, {"index": index_inserter, "problem1": score1, "problem2": score2, "problem3": score3})
    for score in scores_dictionary_list:
        if int(score["index"]) == index_inserter:
            score["problem1"] = score1
            score["problem2"] = score2
            score["problem3"] = score3


def command_splitter(input):
    comand_split_list = input.split(" ")
    return comand_split_list

def command_checker_for_display(input):
    comand_split_list = command_splitter(input)
    try:
        if comand_split_list[main_command] == "list" and comand_split_list[1] != "":
            raise ValueError("Invalid input, please try again!")
    except ValueError as ve:
        return(ve)
    return comand_split_list

def remove_scores_at_position(scores_dictionary_list, index_to_be_removed: int):
    for score in scores_dictionary_list:
        if int(score["index"]) == index_to_be_removed:
            score["problem1"] = 0
            score["problem2"] = 0
            score["problem3"] = 0

def remove_from_startposition_to_endposition(scores_dictionary_list, start_index: int, end_index: int):
    for score in scores_dictionary_list:
        if int(score["index"]) >= int(start_index) and int(score["index"]) <= int(end_index):
            score["problem1"] = 0
            score["problem2"] = 0
            score["problem3"] = 0

# replace 4 P2 or P3 or P5 with 5 – replace the score obtained by participant 4 at P2 with 5

def replace_score(scores_dictionary_list, index_to_be_replaced: int, score_to_be_replaced: int, new_score: int):
    for score in scores_dictionary_list:
        if int(score["index"]) == index_to_be_replaced:
            if score_to_be_replaced == "P1":
                score["problem1"] = new_score
            elif score_to_be_replaced == "P2":
                score["problem2"] = new_score
            elif score_to_be_replaced == "P3":
                score["problem3"] = new_score

def replace_score_at_index(scores_dictionary_list, index_to_be_replaced: int, problem_score_to_be_replaced: str, new_score: int):
    for score in scores_dictionary_list:
        if int(score["index"]) == int(index_to_be_replaced):
            if problem_score_to_be_replaced == "P1":
                score["problem1"] = new_score
            elif problem_score_to_be_replaced == "P2":
                score["problem2"] = new_score
            elif problem_score_to_be_replaced == "P3":
                score["problem3"] = new_score

def calculate_average(scores_dictionary_list):
    for score in scores_dictionary_list:
        score["average"] = (int(score["problem1"]) + int(score["problem2"]) + int(score["problem3"])) / 3
        score["average"] = round(score["average"], 2)

def sort_scores_list_by_index(scores_dictionary_list):
    scores_dictionary_list.sort(key = lambda score: int(score["index"]))

def sort_scores_list_by_average(scores_dictionary_list):
    scores_dictionary_list.sort(key = lambda score: int(score["average"]))

def display_all_scores(scores_dictionary):
    for score in scores_dictionary:
        print(f"Index:{score['index']} ,Score1: {score['problem1']}, Score2: {score['problem2']}, Score3: {score['problem3']}, Average: {score['average']}")

def display_all_scores_without_average(scores_dictionary):
    for score in scores_dictionary:
        print(f"Index:{score['index']} ,Score1: {score['problem1']}, Score2: {score['problem2']}, Score3: {score['problem3']}")

def display_all_scores_sorted_by_average(old_scores_dictionary_list, new_scores_dictionary_list):
    new_scores_dictionary_list = old_scores_dictionary_list
    new_scores_dictionary_list.sort(key = lambda score: score["average"])
    #new_scores_dictionary_list = old_scores_dictionary_list.sort(key = lambda score: score["average"])
    #return new_scores_dictionary_list
    display_all_scores(new_scores_dictionary_list)

def display_all_scores_sorted_by_average2(scores_dictionary_list):
    new_scores_dictionary_list = scores_dictionary_list
    new_scores_dictionary_list.sort(key = lambda score: score["average"])
    #new_scores_dictionary_list = old_scores_dictionary_list.sort(key = lambda score: score["average"])
    #return new_scores_dictionary_list
    display_all_scores(new_scores_dictionary_list)

def display_list_with_property(scores_dictionary_list, input_splitted_list):

    list_property = []

    if input_splitted_list[symbol_element] == "<":
        for score in scores_dictionary_list:
            if score["average"] < float(input_splitted_list[the_element_in_list_that_shows_average]):
                list_property.append(score)
                #print(f"Index:{score['index']} ,Score1: {score['problem1']}, Score2: {score['problem2']}, Score3: {score['problem3']}, Average: {score['average']}")
    elif input_splitted_list[symbol_element] == ">":
        for score in scores_dictionary_list:
            if score["average"] > float(input_splitted_list[the_element_in_list_that_shows_average]):
                list_property.append(score)
                #print(f"Index:{score['index']} ,Score1: {score['problem1']}, Score2: {score['problem2']}, Score3: {score['problem3']}, Average: {score['average']}")
    elif input_splitted_list[symbol_element] == "=":
        for score in scores_dictionary_list:
            if score["average"] == float(input_splitted_list[the_element_in_list_that_shows_average]):
                list_property.append(score)
                #print(f"Index:{score['index']} ,Score1: {score['problem1']}, Score2: {score['problem2']}, Score3: {score['problem3']}, Average: {score['average']}")
    display_all_scores(list_property)

def display_top(scores_dictionary_list, top_number: int):
    new_scores_dictionary_list = scores_dictionary_list
    new_scores_dictionary_list.sort(key = lambda score: score["average"])
    new_scores_dictionary_list.reverse()
    top_list = []
    for score in new_scores_dictionary_list:
        top_list.append(score)
        if len(top_list) == top_number:
            break
    display_all_scores(top_list)

def display_top_at_certain_problem(scores_dictionary_list, top_number: int, problem: str):
    new_scores_dictionary_list = scores_dictionary_list
    if problem == "P1":
        new_scores_dictionary_list.sort(key = lambda score: score["problem1"])
    elif problem == "P2":
        new_scores_dictionary_list.sort(key = lambda score: score["problem2"])
    elif problem == "P3":
        new_scores_dictionary_list.sort(key = lambda score: score["problem3"])
    new_scores_dictionary_list.reverse()
    top_list = []
    for score in new_scores_dictionary_list:
        top_list.append(score)
        if len(top_list) == top_number:
            break
    #top_list.sort(reverse=True, key = lambda score: score["index"])
    top_list.reverse()
    display_all_scores(top_list)

def remove_all_participants_with_property(scores_dictionary_list, input_splitted_list):
    list_property = []
    if input_splitted_list[symbol_element] == "<":
        for score in scores_dictionary_list:
            if score["average"] < float(input_splitted_list[symbol_element]):
                list_property.append(score)
    elif input_splitted_list[symbol_element] == ">":
        for score in scores_dictionary_list:
            if score["average"] > float(input_splitted_list[symbol_element]):
                list_property.append(score)
    elif input_splitted_list[symbol_element] == "=":
        for score in scores_dictionary_list:
            if score["average"] == float(input_splitted_list[symbol_element]):
                list_property.append(score)
    for score in list_property:
        #scores_dictionary_list.remove(score)
        score["problem1"] = 0
        score["problem2"] = 0
        score["problem3"] = 0
        score["average"] = 0
    #display_all_scores(scores_dictionary_list)


def undo(scores_dictionary, undo_stack):
    if not undo_stack:
        print("Nothing to undo")
        return

    previous_state = undo_stack.pop()
    scores_dictionary.clear()
    #scores_dictionary.update(previous_state)
    scores_dictionary.extend(previous_state)
