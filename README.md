# 🐉💎🟢 Jade 🐉💎🟢

A Vyper Mutation Testing Framework

Jade uses mutation testing, which injects modifications into your code, then re-runs your test suite. The goal is to ensure your tests fail when breaking changes are made to your code, and if not the mutation test will fail.

Currently Vyper is written in such a way where Mutations are manually added, but the goal is to eventually support Vyper AST crawling to auto-inject mutations during testing.

## Guide

- [ ] - Support package publishing, and running as a binary

To run the demo
```
cd Foundry-Vyper
python3 ../src/cli.py --path ./vyper_contracts
```

and it will run a mutation test on a simplestore contract. 

## Usage

Insert mutations tests into your Vyper contract by adding

```
# @Jade:<MUTATION>
```

So for example, to add a BINARY_OP mutation, simply add
```
    # @Jade:BINARY_OP
    variable = 5 + 5
```

## Progess

Supported 
- [x] - BINARY_OP
- [x] - UNARY_OP
- [x] - REQUIRE (Assert in this case)
- [ ] - ASSIGNMENT
- [ ] - DELETE_EXPRESSION
- [ ] - FUNCTION_CALL
- [x] - IF_STATEMENT
- [ ] - SWAP_ARGUMENTS_FUNCTION
- [ ] - SWAP_ARGUMENTS_OPERATOR
- [x] - SWAP_LINES
- [ ] - ELIM_DELEGATE
