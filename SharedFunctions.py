from colorama import Fore as F

def scoring(PlayerScore, CpuScore):
  #checks if player wins, loses or draws and returns the answer
  if int(PlayerScore) > int(CpuScore):
    return(F.WHITE + "You got {} and the Cpu got {}\n".format(PlayerScore,CpuScore)+F.GREEN+"You win")
  elif int(PlayerScore) < int(CpuScore):
    return(F.WHITE + "You got {} and the Cpu got {}\n".format(PlayerScore,CpuScore)+F.RED+"You Lose")
  elif int(PlayerScore) == int(CpuScore):
    return(F.WHITE + "You got {} and the Cpu got {}\n".format(PlayerScore,CpuScore)+F.RED+"You Lose")
