let count = 0;

function cc(card) {
    // Only change code below this line
    const plusOne = [2,3,4,5,6];
    const minusOne = [10,"J","K","Q", "K", "A"];
    
    if (plusOne.includes(card)){
        count++;
    }
    else if (minusOne.includes(card)){
        count--;
    }

    if (count > 0){
        return count + "Bet";
    }
    else {
        return count + "Hold";
    }
    
    // Only change code above this line
}

cc(2); cc(3); cc(7); cc('K'); cc('A');