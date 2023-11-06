#!/usr/bin/python3

from 8_multiple_returns import multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)

print("Length: {:d} - First character: {}".format(length, first))
