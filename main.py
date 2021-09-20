if __name__ == '__main__':
    print_info()
    while True:
       lietotaja_ievade()
      # rekins = rekins.Rekins()
       run_again = input('Vai velies sagatavot rekinu velreiz? JAA - 1, NEE - 0')
       if run_again == 1:
           continue
       else:
           exit(0)