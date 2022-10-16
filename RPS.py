# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
  opponent_history.append(prev_play)
  guess = {'P': 'S', 'R': 'P', 'S': 'R'}
  if prev_play=='P':
    return guess['P']
  elif prev_play=='R':
    return guess['R']
  else:
    return guess['S']

  # guess = "R"
  # if len(opponent_history) > 2:
  #     guess = opponent_history[-2]

  # return guess
