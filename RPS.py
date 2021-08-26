from random import choice

ideal_response = {'P': 'S', 'S': 'R', 'R': 'P'}
options = ['R', 'P', 'S']

def player(prev_play, opponent_history=[], sequence={}):

  if prev_play != '':
    opponent_history.append(prev_play)

  seq_length = 4

  if len(opponent_history) < seq_length:
    return choice(options)

  if len(opponent_history) > seq_length:
    opponent_history.pop(0)

  seq = ''.join(opponent_history)
  sequence[seq] = sequence.get(seq, 0) + 1

  seq = ''.join(opponent_history[-(seq_length-1):])
  predict_next_play = max([seq+'R', seq+'P', seq+'S'], key = lambda k: sequence.get(k, 0))[-1]

  return ideal_response[predict_next_play]

