def calc_average(list_to_avg):

    # Förhindrar division med 0
    if len(list_to_avg) == 0: 
        return 0
    
    # Ränka ut genomsnittet och runda till två decimaler 
    avg = round(float(sum(list_to_avg) / len(list_to_avg)), 2)

    return avg