import os
from enum import Enum
import subprocess
import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

class Mutation(Enum):
    BINARY_OP = 1
    UNARY_OP = 2
    REQUIRE = 3
    ASSIGNMENT = 4
    DELETE_EXPRESSION = 5
    FUNCTION_CALL = 6
    IF_STATEMENT = 7
    SWAP_ARGUMENTS_FUNCTION = 8
    SWAP_ARGUMENTS_OPERATOR = 9
    SWAP_LINES = 10
    ELIM_DELEGATE = 11

class Mutator():
    def __init__(self, mutation, line, contents):
        self.mutation = mutation
        self.line = line
        self.contents = contents
    
    def binary_op(self):
        line_to_change = self.contents[self.line] # because array stats at one it should implicitly grab the line below the comment
        if '+' in line_to_change:
            line_to_change.replace('+', '-')
        elif '-' in line_to_change:
            line_to_change.replace('-', '+')
        elif '*' in line_to_change:
            line_to_change.replace('*', '/')
        elif '/' in line_to_change:
            line_to_change.replace('/', '*')
        elif '%' in line_to_change:
            line_to_change.replace('%', '/')
        else:
            raise Exception("Binary_op mutation failed on line {}", self.line+1)

    def unary_op(self):
        pass

    def require(self):
        pass    

    def assignment(self):
        pass    

    def delete_expression(self):
        pass

    def function_call(self):
        pass

    def if_statement(self):
        pass

    def swap_arguments_function(self):
        pass

    def swap_arguments_operator(self):
        pass

    def swap_lines(self):
        pass

    def elim_delegate(self):
        pass

class Contract:
    def __init__(self, path, contents, mutations):
        self.path = path
        self.contents = contents
        self.mutations = mutations

class Project:
    def load_contract(self, contract_path) -> Contract:
        contract_contents = open(contract_path, "r").read()
        contract_lines = open(contract_path, "r").readlines()
        mutations = []

        for count, line in enumerate(contract_lines):
            if line.startswith("# @Jade:"):
                mutation = line.split(":")[1].strip()
                match mutation:
                    case "BINARY_OP":
                        mutations.append((Mutation.BINARY_OP, count))
                    case "UNARY_OP":
                        mutations.append((Mutation.UNARY_OP, count))
                    case "REQUIRE":
                        mutations.append((Mutation.REQUIRE, count))
                    case "ASSIGNMENT":
                        mutations.append((Mutation.ASSIGNMENT, count))
                    case "DELETE_EXPRESSION":
                        mutations.append((Mutation.DELETE_EXPRESSION, count))
                    case "FUNCTION_CALL":
                        mutations.append((Mutation.FUNCTION_CALL, count))
                    case "IF_STATEMENT":
                        mutations.append((Mutation.IF_STATEMENT, count))
                    case "SWAP_ARGUMENTS_FUNCTION":
                        mutations.append((Mutation.SWAP_ARGUMENTS_FUNCTION, count))
                    case "SWAP_ARGUMENTS_OPERATOR":
                        mutations.append((Mutation.SWAP_ARGUMENTS_OPERATOR, count)) 
                    case "SWAP_LINES":
                        mutations.append((Mutation.SWAP_LINES, count))
                    case "ELIM_DELEGATE":
                        mutations.append((Mutation.ELIM_DELEGATE, count))

        contract = Contract(contract_path, contract_contents)
        return contract

    def load_project(self, dir_path):
        colorama_init(autoreset=True)

        contracts = []
        for path in os.listdir(dir_path):
            if path.endswith(".vy"):
                self.load_contract(dir_path, path)
                print(f"Loaded Contract from {Fore.MAGENTA}{path}{Style.RESET_ALL}")

        self.contracts = contracts

    def __init__(self, dir_path, test_cmd):
        self.load_project(dir_path)
        self.test_cmd = test_cmd

    def run_tests(self):
        for contract in self.contracts:
            print(f"Running tests for {Fore.MAGENTA}{contract.path}{Style.RESET_ALL}")
            if len(contract.mutations) == 0:
                print(f"{Fore.RED}No mutations found for {contract.path}{Style.RESET_ALL}")
                continue
            for mutation in contract.mutations:
                (mutation_type, line) = mutation
                print(f"Running mutation {Fore.GREEN}{mutation_type}{Style.RESET_ALL} on line {Fore.GREEN}{line}{Style.RESET_ALL}")
                contract_lines = open(contract, "r").readlines()
                mutator = Mutator(mutation_type, line, contract_lines)
            subprocess.run(self.test_cmd)