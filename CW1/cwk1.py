"""
Introduction to Programming Coursework 1

@author: Thomas peel
"""


def valid_puzzle(puzzle: list) -> bool:
    len_1_item = len(puzzle[0]) #this is the refrence, I will compare The 
    #rest of the items in the list to this
    
    
    for item in puzzle:
        length_item = len(item) # finding the length of the item in the for loop
        if length_item != len_1_item: # comparing the length of the item with hte 1st one
            return False

    return True 


def similarity_grouping(data: list) -> list:
    final_list = []
    for item in data:
        found_item = False #checking if item is in the data
        
        for sublists in final_list:
            if item in sublists:
                sublists.append(item)
                found_item = True # telling system the data has been found add it to the sublist witin the final list
        if found_item is False:
            final_list.append([item]) #if item isnt already found/ a new item in the data create a new sublist within final list
    return final_list
    


def highest_count_items(data: str) -> list:
   item_count = {}
   
   result = []
   
   items = [item.strip() for item in data.split(",")]
   
   max_count = 0
   
   for item in items:
       if item in item_count:
           item_count[item] += 1
       else:
           item_count[item] = 1
           
       max_count = max(max_count, item_count[item])
    

   
   for item, count in item_count.items():
     if count == max_count:
            result.append([item,count])
            
   return result


def valid_char_in_string(popList: list, charSet: list) -> bool:
    for char in charSet:
        if len(char) != 1:
            return False
    
    for element in popList:
        for char in element:
            if char not in charSet:
                return False

    return True


def total_price(unit: int) -> float:
    total = 0
    
    if unit > 6:
        multipler = unit // 6
        total += multipler * 5 
        leftover_units = unit % 6
        
        if leftover_units > 0:
            total += leftover_units * 1.25
            
        if total > 20: 
            total -= total * 0.1

    elif unit < 6:
        total += unit * 1.25

    elif unit == 6:
        total += 5
        

    return total
        


if __name__ == "__main__":
    # sample test for task 1.1
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    puzzle2 = ['NAROUNDDL', 'EDCIT', 'UWSWEDZYA', 'OTCONVOYV',
               'BOSEVRUCI', 'BLLCGLPBD', 'TEENAGEDL', 'TREWZLCGY',
               'RAPLEBAYG', 'ATYTBIWRA', 'YEMROFINU']

    puzzle3 = ['RUNAROU', ['EDCITOA'], ('ZYUWSWE'), 'AKOTCYV',
               'LSBOSEI', 'BOBLLCG', 'LKTEENA', 'ISTREWY',
               'AURAPLE', 'RDATYTB', 'TEYEMRO']
    puzzle4 = 'roundandround'

    print(valid_puzzle(puzzle1))
    print(valid_puzzle(puzzle2))
    print(valid_puzzle(puzzle3))
    print(valid_puzzle(puzzle4))

    # sample test for task 1.2
    data1 = [2, 1, 2, 1]
    data2 = [5, 4, 5, 5, 4, 3]
    data3 = [1, 2, 1, 3, 'a', 'b', "a",  'c']
    print(similarity_grouping(data1))
    print(similarity_grouping(data2))
    print(similarity_grouping(data3))

    # sample test for task 1.3
    data4 = ("3, 13, 7, 9, 3, 3, 5, 7, 12, 13, 11, 13, 8, 7, 5, 14, 15, 3, 9,"
             "7, 5, 9, 14, 3, 8, 2, 5, 5, 8, 14, 11, 11, 12, 8, 5, 3, 3, 10,"
             "3, 10, 7, 7, 10, 10, 2, 7, 4, 8, 1, 5")
    data5 = ("British Gas, British Gas, Ovo, Igloo, Igloo, Octopus, Bulb,"
             "Shell, E.ON, Npower, British Gas, Octopus, Igloo, Npower, Igloo,"
             "Shell, Scottish Power, Bulb, EDF, Bulb, EDF, Bulb,"
             "Scottish Power, Octopus, Scottish Power, Octopus, Octopus, EDF,"
             "Ovo, Shell, Octopus, E.ON, British Gas, Bulb, Npower, Shell,"
             "Scottish Power, Npower, Scottish Power, Npower")
    data6 = ("aac, ctt, gat, ccc, gcc, ctg, gtc, tcg, ccg, cca, ata, cca,"
             "tat, ata, cac, gcg, cca, gta, gtg, gac, taa, ata, gtc, aat, gct,"
             "gta, ggc, tgc, tca, ctt, tgt, ata, acc, tgc, gac, cgc, atc, cgt,"
             "tac, agg, ctt, cgc, cgc, tgg, gcg, tgg, taa, cta, aaa, tgc, cgt,"
             "tgc, gac, tta, aag, taa, act, cca, tac, agg, cgc, gtg, cca, gcg,"
             "gtt, gag, tca, aca, tct, gta, ata, ctt, gat, tcg, tcg, cac, cgt,"
             "tac, caa, aac, ctg, tgt, aag, ttc, ccc, tcc, ctc, cct, aga, gtt,"
             "tga, gaa, cct, ctc, tct, ggt, gcc, tct, ccc, agt, caa, gac, ccc,"
             "cgc")
    print(highest_count_items(data4))
    print(highest_count_items(data5))
    print(highest_count_items(data6))

    # sample test for task 1.4
    popList1 = ['00000', '00001', '00010', '00011', '00100']
    popList2 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc', 'tcg',
                'ccg', 'cca', 'ata']
    popList3 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc']
    charSet1 = ['0', '1']
    charSet2 = ['a', 'c', 't', 'g']
    charSet3 = ['a', 'c']
    charSet4 = '01'
    print(valid_char_in_string(popList1, charSet1))
    print(valid_char_in_string(popList2, charSet2))
    print(valid_char_in_string(popList3, charSet3))
    print(valid_char_in_string(popList1, charSet4))

    # sample test for task 1.5
    print(total_price(3))
    print(total_price(12))
    print(total_price(15))
    print(total_price(26))


