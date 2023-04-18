# 🐉💎🟢 Jade 🐉💎🟢

Vyper Mutation Testing Framework

## Guide

To run the demo
```
cd Foundry-Vyper
python3 ../src/cli.py --path ./vyper_contracts
```

and it will run a mutation test on a simplestore contract

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
above an affectable statement

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